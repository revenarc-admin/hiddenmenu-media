#!/usr/bin/env bash
# Publish a carousel to @thehiddenmenu.io with the Instagram Graph API (Business portfolio + system user token).
#
# Usage:
#   ./post_carousel.sh <slides_folder> <caption_file> <public_base_url>
#
# Example:
#   ./post_carousel.sh carousels/01_no_dollar_signs captions/day01.txt \
#     https://raw.githubusercontent.com/<user>/hiddenmenu-media/main/01_no_dollar_signs
#
# Requirements:
#   - Instagram professional (Creator) account
#   - System user token with instagram_basic + instagram_content_publish
#   - Token saved as a credential for graph.facebook.com (sent as a Bearer header)
#   - Slides converted to JPEG and reachable at <public_base_url>/slide_01.jpg ...
#
# Set DRY_RUN=1 to build and check containers without publishing.

set -euo pipefail

FOLDER="${1:?slides folder}"
CAPTION_FILE="${2:?caption file}"
BASE_URL="${3:?public base url}"
API="https://graph.facebook.com/v26.0"
CRED="${IG_CRED:?set IG_CRED to the credential handle}"
IG_ID="${IG_ID:-17841466730681099}"   # @thehiddenmenu.io

ig() { pplx credentials run "$CRED" -- curl -sS --fail-with-body "$@"; }
json() { python3 -c "import sys,json; print(json.load(sys.stdin)$1)"; }

# 1. Convert PNG slides to JPEG (the API accepts JPEG only)
python3 - "$FOLDER" <<'EOF'
import sys, glob, os
from PIL import Image
for p in sorted(glob.glob(os.path.join(sys.argv[1], "slide_*.png"))):
    Image.open(p).convert("RGB").save(p[:-4] + ".jpg", "JPEG", quality=95)
EOF
mapfile -t SLIDES < <(ls "$FOLDER"/slide_*.jpg | sort)
echo "Slides: ${#SLIDES[@]}"
[ "${#SLIDES[@]}" -ge 2 ] && [ "${#SLIDES[@]}" -le 20 ] || { echo "Carousels need 2-20 images"; exit 1; }

# 2. Check that every image is publicly reachable
for s in "${SLIDES[@]}"; do
  url="$BASE_URL/$(basename "$s")"
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  [ "$code" = "200" ] || { echo "Not public ($code): $url"; exit 1; }
done

# 3. Confirm the token can see the account
USERNAME=$(ig "$API/$IG_ID?fields=username" | json "['username']")
echo "Posting as: @$USERNAME ($IG_ID)"

# 4. Create one container per slide
CHILDREN=()
for s in "${SLIDES[@]}"; do
  id=$(ig -X POST "$API/$IG_ID/media" \
        --data-urlencode "image_url=$BASE_URL/$(basename "$s")" \
        -d "is_carousel_item=true" | json "['id']")
  CHILDREN+=("$id"); echo "Item $(basename "$s"): $id"
done

# 5. Create the carousel container
CAROUSEL=$(ig -X POST "$API/$IG_ID/media" \
  -d "media_type=CAROUSEL" \
  -d "children=$(IFS=,; echo "${CHILDREN[*]}")" \
  --data-urlencode "caption@$CAPTION_FILE" | json "['id']")
echo "Carousel container: $CAROUSEL"

# 6. Wait until ready (check once a minute, max 5 minutes)
for i in 1 2 3 4 5 6; do
  status=$(ig "$API/$CAROUSEL?fields=status_code" | json "['status_code']")
  echo "Status: $status"
  [ "$status" = "FINISHED" ] && break
  [ "$status" = "ERROR" ] || [ "$status" = "EXPIRED" ] && { echo "Container failed"; exit 1; }
  sleep 60
done
[ "$status" = "FINISHED" ] || { echo "Timed out"; exit 1; }

if [ "${DRY_RUN:-0}" = "1" ]; then echo "DRY_RUN: not publishing"; exit 0; fi

# 7. Publish
POST_ID=$(ig -X POST "$API/$IG_ID/media_publish" -d "creation_id=$CAROUSEL" | json "['id']")
echo "Published. Media ID: $POST_ID"
ig "$API/$POST_ID?fields=permalink" | json "['permalink']"

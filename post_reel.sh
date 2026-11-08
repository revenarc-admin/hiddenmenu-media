#!/usr/bin/env bash
# Publish one Reel (Reels tab only, not the grid) to @thehiddenmenu.io.
# Usage: ./post_reel.sh <public_mp4_url> <caption_file>
set -euo pipefail
URL="${1:?public mp4 url}"; CAP="${2:?caption file}"
API="https://graph.facebook.com/v26.0"
CRED="${IG_CRED:-custom-cred:f87a7d1d-8eb8-4026-b27a-d2011c9fc8fc@graph.facebook.com}"
IG_ID="${IG_ID:-17841466730681099}"
ig() { pplx credentials run "$CRED" -- curl -sS --fail-with-body "$@"; }
code=$(curl -sL -o /dev/null -w "%{http_code}" "$URL"); [ "$code" = "200" ] || { echo "Not public ($code): $URL"; exit 1; }
CID=$(ig -X POST "$API/$IG_ID/media" -d "media_type=REELS" --data-urlencode "video_url=$URL" -d "share_to_feed=false" --data-urlencode "caption@$CAP" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
echo "Reel container: $CID"
for i in $(seq 1 60); do
  s=$(ig "$API/$CID?fields=status_code" | python3 -c "import sys,json;print(json.load(sys.stdin)['status_code'])")
  echo "Status: $s"; [ "$s" = "FINISHED" ] && break; [ "$s" = "ERROR" ] && exit 1; sleep 10
done
MID=$(ig -X POST "$API/$IG_ID/media_publish" -d "creation_id=$CID" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
echo "Reel published. Media ID: $MID"

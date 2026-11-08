#!/usr/bin/env bash
# Publish one image Story to @thehiddenmenu.io. Usage: ./post_story.sh <public_image_url>
set -euo pipefail
URL="${1:?public jpg url}"
API="https://graph.facebook.com/v26.0"
CRED="${IG_CRED:-custom-cred:f87a7d1d-8eb8-4026-b27a-d2011c9fc8fc@graph.facebook.com}"
IG_ID="${IG_ID:-17841466730681099}"
ig() { pplx credentials run "$CRED" -- curl -sS --fail-with-body "$@"; }
code=$(curl -s -o /dev/null -w "%{http_code}" "$URL"); [ "$code" = "200" ] || { echo "Not public ($code): $URL"; exit 1; }
CID=$(ig -X POST "$API/$IG_ID/media" --data-urlencode "image_url=$URL" -d "media_type=STORIES" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
echo "Story container: $CID"
for i in $(seq 1 30); do
  s=$(ig "$API/$CID?fields=status_code" | python3 -c "import sys,json;print(json.load(sys.stdin)['status_code'])")
  echo "Status: $s"; [ "$s" = "FINISHED" ] && break; [ "$s" = "ERROR" ] && exit 1; sleep 5
done
MID=$(ig -X POST "$API/$IG_ID/media_publish" -d "creation_id=$CID" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
echo "Story published. Media ID: $MID"

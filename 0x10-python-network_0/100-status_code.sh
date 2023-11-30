#!/bin/bash
# Send GET request and display
curl -so /dev/null -w '%{http_code}' "$1"

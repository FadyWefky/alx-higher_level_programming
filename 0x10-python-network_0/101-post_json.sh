#!/bin/bash
# post a json file to web server
curl -sH "Content-Type: application/json" -d "@$2" "$1"

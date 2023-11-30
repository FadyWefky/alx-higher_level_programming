#!/bin/bash
# Methot
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'

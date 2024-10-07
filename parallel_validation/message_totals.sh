#!/usr/bin/env bash

# Extracts the message summary information from a group of validation reports
# and returns the total number of messages in each category

set -e

TEMPFILE=$(mktemp)

grep -h -A100 'Message Types:' "$@" | grep '^ *\d' > "$TEMPFILE"

for i in $(awk '{print $2}' "$TEMPFILE" | uniq | sort | uniq); do
    total=$(grep "$i" "$TEMPFILE" | awk '{sum+=$1} END{print sum;}')
    echo "$total $i"
done

rm "$TEMPFILE"
#!/usr/bin/env bash
set -e

# Extracts the summary information from a group of validation reports
# and returns the total number of products in each category

TEMPFILE=$(mktemp)

grep -h -A4 "Product Validation Summary" "$@" > "$TEMPFILE"

for i in passed failed skipped total; do
    total=$(grep "product(s) $i" "$TEMPFILE" | awk '{sum+=$1} END{print sum;}')
    echo "$total product(s) $i"
done

rm "$TEMPFILE"
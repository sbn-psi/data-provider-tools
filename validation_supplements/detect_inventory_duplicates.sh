#! /usr/bin/env bash
set -e
FILENAME=$1

if [ -z "$FILENAME" ]; then
    echo usage: detect_inventory_duplicates.sh inventory_csv_filename
fi

cat $FILENAME | awk -F ',' '{print $2}' | sort  | uniq -c | grep -v ' 1 '

#!/usr/bin/env bash

usage()
{
    echo "usage: validate_worker.sh config_file catalog_file report_dir file_to_validate..."
    exit 1
}

CONFIG_FILE="$1"; shift
CATALOG_FILE="$1"; shift
REPORT_DIR="$1"; shift

set -e

[ -n "$CONFIG_FILE" ] || (echo "Config file not provided"; usage)
[ -n "$CATALOG_FILE" ] || (echo "Catalog file not provided"; usage)
[ -n "$REPORT_DIR" ] || (echo "Report directory not provided"; usage)
[ -d "$REPORT_DIR" ] || (echo "Report directory does not exist"; usage)

RUNDATE=$(date +'%Y%m%dT%H%M%S')
REPORT_FILE=$(mktemp "$REPORT_DIR/validation.$RUNDATE".XXXXXX.txt)

validate -c "$CONFIG_FILE" -C "$CATALOG_FILE" -t "$@" > "$REPORT_FILE"
mv "$REPORT_FILE" "$REPORT_DIR/complete"

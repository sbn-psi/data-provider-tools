#!/usr/bin/env bash

set -e

usage()
{
    echo "usage: validate_worker.sh config_file catalog_file report_dir file_to_validate..."
    exit 1
}

CONFIG_FILE="$1"; shift || (echo "Config file not provided"; usage)
CATALOG_FILE="$1"; shift || (echo "Catalog file not provided"; usage)
REPORT_DIR="$1"; shift || (echo "Report directory not provided"; usage)

[ -d "$REPORT_DIR" ] || (echo "Report directory does not exist"; usage)

RUNDATE=$(date +'%Y%m%dT%H%M%S')
REPORT_FILE=$(mktemp "$REPORT_DIR/validation.$RUNDATE".XXXXXX.txt)

validate -c "$CONFIG_FILE" -C "$CATALOG_FILE" -t "$@" > "$REPORT_FILE"
mv "$REPORT_FILE" "$REPORT_DIR/complete"

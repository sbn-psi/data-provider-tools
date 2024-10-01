#!/usr/bin/env bash
RUNDATE=$(date +'%Y%m%dT%H%M%S')

CONFIG_FILE=$1
shift
CATALOG_FILE=$1
shift
REPORT_DIR=$1
shift

REPORT_FILE=$(mktemp $REPORT_DIR/validation."$RUNDATE".XXXXXX.txt)

validate -c "$CONFIG_FILE" -C "$CATALOG_FILE" -t "$@" > "$REPORT_FILE"
mv "$REPORT_FILE" "$REPORT_DIR/complete"
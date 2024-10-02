#! /usr/bin/env bash
set -e


usage()
{
    echo "usage: validate_parallel.sh validation_directory config_file catalog_file report_dir [workers] [batch_size]"
    exit 1
}


DIRNAME=$1
CONFIG_FILE=$2
CATALOG_FILE=$3
REPORT_DIR=$4
WORKERS=${5-4}
BATCH_SIZE=${6-1000}


[ -n "$DIRNAME" ] || (echo "Directory name not provided" && usage)
[ -d "$DIRNAME" ] || (echo "Directory name not a directory" && usage)
[ -n "$CONFIG_FILE" ] || (echo "Config file not provided" && usage)
[ -n "$CATALOG_FILE" ] || (echo "Catalog file not provided" && usage)
[ -n "$REPORT_DIR" ] || (echo "Report directory not provided" && usage)

mkdir -p "$REPORT_DIR/complete"

find "$DIRNAME" -name "*.xml" -print0 | xargs -0 -n"${BATCH_SIZE}" -P"${WORKERS}" ./validate_worker.sh "$CONFIG_FILE" "$CATALOG_FILE" "$REPORT_DIR"



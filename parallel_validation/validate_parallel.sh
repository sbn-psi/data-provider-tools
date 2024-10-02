#! /usr/bin/env bash
set -e


DIRNAME=$1
CONFIG_FILE=$2
CATALOG_FILE=$3
REPORT_DIR=$4
WORKERS=${5-4}
BATCH_SIZE=${6-1000}


usage()
{
    echo "usage: validate_parallel.sh validation_directory config_file catalog_file report_dir [workers] [batch_size]"
    exit 1
}


if [ -z "$DIRNAME" ]; then
    echo 'no validation direcotry specified'
    usage
fi


if [ -z "$CONFIG_FILE" ]; then
    echo 'no config file specified'
    usage
fi


if [ -z "$CATALOG_FILE" ]; then
    echo 'no catalog file specified'
    usage
fi


if [ -z "$DIRNAME" ]; then
    echo 'no report directory specified'
    usage
fi


mkdir -p "$REPORT_DIR/complete"

[ -n "$DIRNAME" ] || (echo "Directory name not provided" && exit 1)
[ -d "$DIRNAME" ] || (echo "Directory name not a directory" && exit 1)

find "$DIRNAME" -name "*.xml" -print0 | xargs -0 -n"${BATCH_SIZE}" -P"${WORKERS}" ./validate_worker.sh "$CONFIG_FILE" "$CATALOG_FILE" "$REPORT_DIR"



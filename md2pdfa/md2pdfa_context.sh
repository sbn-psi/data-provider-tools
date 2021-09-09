MDFILE=$1
DOCX_FILE=${MDFILE/.md/.docx}
PDFA_FILE=${MDFILE/.md/.pdf}
OUTDIR=`dirname $1`

VERAPDF_CMD=~/verapdf/verapdf

pandoc -t context --variable=pdfa:1b:2005 --variable=mainfont:times -o $PDFA_FILE $MDFILE 

if [ -e "$VERAPDF_CMD" ]; then
    echo "Running verapdf..."
    $VERAPDF_CMD --format text "${PDFA_FILE}"
else
    echo "verapdf not found. Your conversion probably succeeded, but it cannot be validated."
fi

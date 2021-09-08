MDFILE=$1
DOCX_FILE=${MDFILE/.md/.docx}
PDFA_FILE=${MDFILE/.md/.pdf}
VERAPDF_CMD=~/verapdf/verapdf

pandoc -o $DOCX_FILE $MDFILE
soffice --headless --convert-to pdf:"writer_pdf_Export:SelectPdfVersion=1" --outdir ./ $DOCX_FILE

if [ -e "$VERAPDF_CMD" ]; then
    echo "Running verapdf..."
    $VERAPDF_CMD --format text "${PDFA_FILE}"
else
    echo "verapdf not found. Your conversion probably succeeded, but it cannot be validated."
fi

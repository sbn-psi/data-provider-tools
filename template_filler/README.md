# SBN Template Filler

## About

Template Filler is a tool that will use an existing PDS4 label (that has been converted into a template) and a CSV file to generate PDS4 labels for you. This is useful if you have a large number of files that need labels, especially if you have an existing sample label.

## Running the template filler

### Invocation

`/path/to/template_filler.py [-h] --template-file TEMPLATE_FILE --csv-file CSV_FILE --output-path OUTPUT_PATH [--filename-column FILENAME_COLUMN] [--product-id-column PRODUCT_ID_COLUMN] [--data-file-column DATA_FILE_COLUMN]`

The script will take the template file, inject values from the CSV file, and write it to an output directory.

#### Required Parameters

* `--template-file`: This is is the file that will serve as the base for your generated labels.
* `--csv-file`: This file will provide the values that will be injected into the template file
* `--output-dir`: This is the directory where the generated labels will go.

#### Advanced Parameters

* `--filename-column`: This is the name of the field/placeholder for the label file name. It is "filename" by default.
* `--product-id-column`: This is the name of the field/placeholder for the product id. It is "productId" by default.
* `--data-file-id-column`: This is the name of the field/placeholder for the data file name. It is "dataFile" by default.

### Prerequisites

* Python 3
* Jinja2

### Installing Jinja

The easiest way to install Jinja is using pip, either on its own or with the provided requirements file:

* `pip3 install jinja2` or
* `pip3 install -r requirements.txt`

Depending on your platform, you might need to run `pip` instead of `pip3`.

## Writing a template

Template Filler uses the Jinja2 templating lanuage. The template designer documentation is at (https://jinja.palletsprojects.com/en/3.1.x/templates/). Jinja2 is a very powerful language, but in most cases, you don't actually need that. All you need to do do is take an existing label, and add `{{ fieldname }}` as a placeholder anywhere where you want a value from the csv file to be used.

There are a few special values that can be inferred from the data file name ("dataFile" by default) if you don't want to provide them yourself.

* label file name (usually "filename"): This is the name of the data file, but with an extension of `.xml` instead of the original exension
* product id (usually "productId"): This is the name of the data file, but with periods converted to underscores

## Writing a CSV file

Template filler uses standard CSV files to populate it templates. A specification of the CSV format is at (https://www.rfc-editor.org/rfc/rfc4180.html). However, you can generally use a spreadsheet and export it to CSV. It's probably a good idea to write the field names in `camelCase` or `snake_case`, to make the template easier to write.

You will want one line per label that you want to generate. The "filename" field will determine the name of the label file. If you don't provide one, template filler will try to guess the label file name based on the data file name.

## Similar tools

### PDS MILabel

(https://nasa-pds.github.io/mi-label/)

MILabel generates PDS4 labels using a template and existing PDS3 labels. However, it can only use existing PDS3 labels as source inputs, and does not support CSV files.

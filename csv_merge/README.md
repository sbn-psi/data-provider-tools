# CSVMerge

This script will merge two CSV files together, in a way similar to left joining two tables.

## Rules:

The join column is the first column of each table. So this means if you had two tables with metadata about a file, then you would want the file name to be the first column of each table.
The second table's columns take precedence over the first table's columns, even if they are blank.
Only rows in the first table are considered. Any rows in the second table that do not match up with the first table are discarded.


## Example

```bash
./csvmerge.py test.csv add.csv result.csv
cat result.csv
```

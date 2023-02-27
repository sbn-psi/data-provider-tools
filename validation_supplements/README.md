# Supplements to validate

These are additional tools that provide additional validations that are not supported by validate.

## Duplicate inventory LIDVID detection

Currently, validate is unable to detect duplicate lidvids in a collection.

https://github.com/NASA-PDS/validate/issues/476

In the meantime, we can detect duplicate LIDs using the `detect_inventory_duplicates.sh` script:

```
user@pc Desktop % ./detect_inventory_duplicates.sh collection_gbo.ast.sawyer.spectra_document_inventory.csv
   2 urn:nasa:pds:gbo.ast.sawyer.spectra:document:observatory.mcdonald::1.0
```

for all of the collections in a bundle:

```
find dirname -name "collection*.csv" -exec ./detect_inventory_duplicates.sh '{}' \;
```
#!/usr/bin/env bash

# Extracts the individual product validations from a group of validation reports

sed -n '/Product Level Validation Results/,/Summary:/p' "$@" | grep -v 'Summary:' | grep -v 'Product Level Validation Results'

# Parallel Validation

## Introduction

## Is parallel validation right for you?

### What can parallel validation speed up?

### What can't parallel validation speed up?

## How to use the parallel validator script

Options:
* validation directory - this where all of the files that you want to validate are stored. It doesn't matter if this is a bundle, collection, or even a subset of a collection.
* validate configuration - this is where you will specify options for the validate command, instead of on the command line. This makes the configurations reusable, and also simplifies the script.
* catalog file - this will redirect all of the requests for schema and schematron files to another location, preferably on your local filesystem. It is important to have one of these, since the validator will reach out to the internet to reload the catalogs on a regular basis otherwise, degrading performance.
* report directory - this is where all of the output files are stored. This directory will be automatically created if if does not exist.
* workers - this specifies how many instances of validate you want to run at once. If you don't provide this, the script will default to 4. See below to get the correct value.
* batch size - this specifies how many products each validate instance will process. If you don't providde this, the script will defauly to 1000. This should probably be left as-is. Going higher will likely exceed the maximum argument list length, and will get clamped back down anyway.

### How many processes do I need?

Generally, you can support as many processes as you have CPU cores. There is a good chance that each validator instance will utilize the entire core, so there is generally no need to
run with more cores. In fact, if the validator does not use the entire core, there is a good chance that you are I/O bound at this point, and can probably reduce the number of cores that you are using.

You may also want to leave one core free so that the OS can use it for other tasks. The OS should actually schedule things so that this is not a problem, but I like to
leave one free anyway.

### Why are there so many files?

## How to interpret the results

### Combining overall statistics

### Combining message statistics

### Combining product-level messages


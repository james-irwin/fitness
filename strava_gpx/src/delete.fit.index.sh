#!/bin/bash

curl -XDELETE "http://127.0.0.1:9200/fit/?pretty"
sh -x ./fit.mapping.fixer.sh

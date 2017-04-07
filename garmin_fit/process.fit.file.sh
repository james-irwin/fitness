#!/bin/bash

./decode $1 | sed -n -e "/timestamp/p" > docs.json
echo Doing $1
time ./push.fit.docs.to.es.py docs.json

curl "http://localhost:9200/_cat/indices?v"

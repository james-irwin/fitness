for i in data/*gpx; do node src/gpx.to.json.js $i > foo.json; src/push.gpx.docs.to.es.py foo.json; done


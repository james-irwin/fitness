curl -XPUT "http://127.0.0.1:9200/fit/?pretty" -d '{
     "settings" : {
         "number_of_shards" : 3
     },
    "mappings" : {
      "wes" : {
        "properties" : {
          "position" : {
            "type" : "geo_point"
          },
          "timestamp" : {
            "type" : "date"
          }
        }
      }
    }
}'

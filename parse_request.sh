#!/bin/bash  

# CURL='/usr/bin/curl -X POST'

# curl -d '{
# 	"region": "1711",
# 	"environmental_type": "weather"
#     }' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/api/stations
data='{"id":[6,27,16,73,74,126,125,210,211,224,259,258,257]}'
# echo $data
# echo ${data[@]}


for id in "${data[@]}"; do

    KEY="${id%%:*}"

    VALUE="${id#*:}"

    # echo $VALUE

done


for i in "${VALUE[@]}"; do

    x="${i#*:}"

    echo $x

done


# for animal in "${ARRAY[@]}" ; do
#     KEY="${animal%%:*}"
#     VALUE="${animal##*:}"
#     printf "%s likes to %s.\n" "$KEY" "$VALUE"
# done
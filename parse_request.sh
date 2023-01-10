#!/bin/bash  

CURL='/usr/bin/curl -X POST'

# Realiza a chamada na API para gerar os arquivos e inserir no banco de dados
var='{
    "station_id": '$1',
    "region": "'$2'",
    "environmental_type": "'$3'"
}'

status_code=$(curl -d "$var" -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/api/forecast_records --write-out %{http_code} --silent --output /dev/null )


while true
do
    if [[ "$status_code" -eq 200 ]] ; then
        echo "Status code is $status_code - Success Request"
        break
    else
        echo "Status code is $status_code - Fail Request and trying again"
        status_code=$(curl -d "$var" -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/api/forecast_records --write-out %{http_code} --silent --output /dev/null )
    fi
    sleep 10
done

# # Entra no diretorio
# cd src/services/output/ 

# mkdir zip

# #compactada e move para a pasta zip
# zip -r teste.zip . 
# mv teste.zip zip/

# cd ..
# # Executa a funcao para envio do zip para cloud
# python3 utils.py

# cd output/

# rm -rf zip *.txt





# curl -d '{
# 	"region": "1711",
# 	"environmental_type": "weather"
#     }' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/api/stations
# data='{"id":[6,27,16,73,74,126,125,210,211,224,259,258,257]}' 
# echo $data | grep -o '"[^"]*"\s*:\s*"[^"]*"'

# echo ${data[@]}
# echo ${data[@]}


# for id in "${data[@]}"; do

#     KEY="${id%%:*}"

#     VALUE="${id#*:}"

#     # echo $VALUE

# done


# for i in "${VALUE[@]}"; do

#     x="${i#*:}"

#     echo $x

# done


# for animal in "${ARRAY[@]}" ; do
#     KEY="${animal%%:*}"
#     VALUE="${animal##*:}"
#     printf "%s likes to %s.\n" "$KEY" "$VALUE"
# done
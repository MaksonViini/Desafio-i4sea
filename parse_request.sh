#!/bin/bash  

CURL='/usr/bin/curl -X POST'

# Realiza a chamada na API para buscar todas as estações
data=$(curl -d '{
	"region": "1711",
	"environmental_type": "weather"
    }' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/api/stations)


declare -ai array

array=($(echo $data | grep -o  '[0-9]\+'))


len=${#array[@]}
i=0

while [ $i -lt $len ];
do

# Realiza a chamada na API para gerar os arquivos e inserir no banco de dados
var='{
    "station_id": '${array[i]}',
    "region": "'$2'",
    "environmental_type": "'$3'"
}'



status_code=$(curl -d "$var" -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/api/forecast_records --write-out %{http_code} --silent --output /dev/null )


#Verifica se a resposta http e sucesso, se nao tenta novamente fazer a requisição
# while true
# do
#     if [[ "$status_code" -eq 200 ]]; then
#         echo "Status code is $status_code - Success Request"
#         break
#     else
#         echo "Status code is $status_code - Fail Request and trying again"
#     fi
# done


let i++

done

hoje=$(date +'%d-%m-%Y')

# Entra no diretório
cd src/services/output/ 

mkdir zip

#compactada e move para a pasta zip
zip -r $hoje.zip . 
mv $hoje.zip zip/

cd ..
# Executa a função para envio do zip para cloud
python3 utils.py

cd output/

# limpa o diretório
rm -rf zip *.json

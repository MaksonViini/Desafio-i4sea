#!/bin/bash  

# Para executar em background
# bash runtime.sh &


if [ -d /logs/ ];
then
    echo "Sim, existe!"
else
    echo "Nao existe! Criando..."
    mkdir logs
fi

while true  
do  
  bash parse_request.sh $1 $2 $2 >> logs/logs.txt
  sleep 10  
done
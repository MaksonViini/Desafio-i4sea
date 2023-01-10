# Desafio-i4sea
 
# A aplicação
A aplicação fornece endpoints para buscar registros na base de dados NoSQL, endpoint para criar um registro, para buscar a previsão de uma determinada station, de acordo com a região juntamente com o ambiente especificado, como por exemplo clima [weather]. E a possibilidade de buscar todos os id's de uma determinada station.
 
- Execucao shell script
  Para executar a aplicação, é necessário executar o shell script `runtime.sh` como `bash runtime.sh &`, ele vai realizar a agenda de execução em background temporizada do script `parse_request.sh`, o qual vai executar a API por meio de um `curl`. Os parâmetros podem ser definidos separadamente no script `parse_request.sh` por meio da linha de comando `bash parse_request.sh 27 "1711" "weather"` por exemplo. O runtime também pode receber os parâmetros por meio da mesma definição.

   Executando, é salvo em um json na pasta output os dados, por meio do shell script todos os arquivos são compactados, adicionados à pasta zip, enviados a um bucket na Google Cloud e posteriormente excluídos, foi uma opção de projeto que optei para integrar mais a aplicação a um ambiente cloud, e evitar transferência de arquivos constantes e perdas, além da cloud prover segurança e de fácil acesso. A infraestrutura foi criada por meio de infra-as-a-code com terraform.
   
    - link do bucket: https://console.cloud.google.com/storage/browser/i4sea-bucket
   - Execucao Docker
     Para executar o container, pode-se executar o comando `docker-compose up -d`, onde o container vai iniciar em modo daemon.


 
OBS: Em minha opinião, este não é o melhor método de execução, porém e o solicitado e atende a demanda, o ideal para este tipo de agenda de Eng. de Dados por meio de endpoints e usando a ferramenta da Apache, Airflow juntamente com um ambiente em cloud tendo um gerenciamento que escala e se utilizando da vantagem de servicos serverless ao invés apenas de uma computer engine.


### ENDPOINTS

### 1 - Busca registros armazenados no banco

 ```
 METHOD: GET
 ENDPOINT: api/records
 ```

Exemplo de retorno:

```json	
[
	{
		"station_id": 27,
		"station_name": "POB",
		"station_depth": "null",
		"station_depth_unit": "m",
		"station_lat": -24.009433,
		"station_lon": -46.332399,
		"macro_region": "san",
		"region": "1711",
		"region_timezone": "America/Bahia",
		"data_type": "forecast",
		"environmental_type": "weather",
		"environmental_data": [
			{
				"date": "2023-01-08T21:00:00-03:00",
				"environmental_variable": "wind_vel",
				"value": 10.76887321472168,
				"units": "knots"
			}
		]
    }
  ]
```

### 2 - Busca todos os ID's de uma station

 ```
 METHOD: POST
 ENDPOINT: api/stations
 ```

Exemplo de entrada:

```json
{
	"region": "1711",
	"environmental_type": "weather"
}
```

Exemplo de retorno:
```json
{
	"id": [
		6,
		27,
		16,
		73,
		74,
		126,
		125,
		210,
		211,
		224,
		259,
		258,
		257
	]
}
```

### 3 - Busca todos os ID's de uma station

 ```
 METHOD: POST
 ENDPOINT: api/forecast_records
 ```

Exemplo de entrada:

```json
{
	"station_id": 27,
	"region": "1711",
	"environmental_type": "weather"
}
```

Exemplo de retorno:
```json
[
	{
		"station_id": 27,
		"station_name": "POB",
		"station_depth": null,
		"station_depth_unit": "m",
		"station_lat": -24.009433,
		"station_lon": -46.332399,
		"macro_region": "san",
		"region": "1711",
		"region_timezone": "America/Bahia",
		"data_type": "forecast",
		"environmental_type": "weather",
		"environmental_data": [
			{
				"date": "2023-01-09T21:00:00-03:00",
				"environmental_variable": "wind_vel",
				"value": 8.572334289550781,
				"units": "knots"
			},
			{
				"date": "2023-01-09T21:00:00-03:00",
				"environmental_variable": "wind_vel_80m",
				"value": 10.282913208007812,
				"units": "knots"
			},...]}]
```


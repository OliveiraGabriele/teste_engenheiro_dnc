import requests
import json
import boto3
from datetime import datetime, timedelta
import os
import uuid

def verify_keys(api_key, s3_bucket):
    if not api_key:
        raise ValueError("API_KEY não encontrada. Certifique-se de que está configurada nas variáveis de ambiente do Lambda.")
    if not s3_bucket:
        raise ValueError("S3_BUCKET não encontrado. Certifique-se de que está configurado nas variáveis de ambiente do Lambda.")

def get_weather_data(api_key, lat, lon,timestamp):
    url_base = f"https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'lat': lat,
        'lon': lon,
        'dt': timestamp,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'
    }
    response = requests.get(url_base, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Falha na requisição: {response.status_code}, {response.text}")
        return None

def save_to_s3(s3_client, s3_bucket, s3_key, data):
    try:
        s3_client.put_object(
            Bucket=s3_bucket,
            Key=s3_key,
            Body=json.dumps(data),
            ContentType='application/json'
        )
    except Exception as e:
        print(f"Erro ao salvar no S3: {e}")

def lambda_handler(event, context):
    api_key = 'apikey-autentication'    
    s3_bucket = 'bkt-name'
    
    lat = -23.5475
    lon = -46.6361
    city = 'São Paulo'
    
    try:
        verify_keys(api_key, s3_bucket)
    except ValueError as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
            
    s3_client = boto3.client('s3')
    data_atual = datetime.now()

    for dias_atras in range(1, 21):
        data_passada = data_atual - timedelta(days=dias_atras)
        weather_data_for_day = []
        
        for hour in range(0, 24, 3):
            timestamp = int((data_passada + timedelta(hours=hour)).timestamp())
            weather_data = get_weather_data(api_key, lat, lon, timestamp)
            
            if weather_data:
                weather_data_for_day.append(weather_data)
            else:
                print(f"Falha ao obter dados meteorológicos para {data_passada.strftime('%Y-%m-%d')} às {hour}:00")
        

        if weather_data_for_day:
            unique_id = str(uuid.uuid4()) 
            s3_key = f"dados_entrada/clima/anomesdia={data_passada.strftime('%Y%m%d')}/file_openweathermap_{data_passada.strftime('%Y%m%d')}_{unique_id}.json"
            save_to_s3(s3_client, s3_bucket, s3_key, weather_data_for_day)
            print(f'Dados meteorológicos para {data_passada.strftime("%Y-%m-%d")} salvos no S3.')
        else:
            print(f"Falha ao obter dados meteorológicos para {data_passada.strftime('%Y-%m-%d')}")
            return {
                'statusCode': 500,
                'body': "Erro ao obter dados históricos."
            }
            
    return {
        'statusCode': 200,
        'body': json.dumps('Dados meteorologicos carregados com sucesso no S3.')
    }

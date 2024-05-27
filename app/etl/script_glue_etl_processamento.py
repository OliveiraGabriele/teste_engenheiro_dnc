import boto3
import awswrangler as wr
from datetime import datetime
import pandas as pd

def ler_json_do_s3(bucket, key, dias):
    dfs = []
    caminho_base_s3 = f"s3://{bucket}/{key}"
    
    for dia in dias:
        caminho_completo = f"{caminho_base_s3}{dia}/"
        df = wr.s3.read_json(path=caminho_completo)
        dfs.append(df)
    
    df_final = pd.concat(dfs, ignore_index=True)
    return df_final

def parse_date(df):
    print('Tratamento de datas')
    df['dt'] = pd.to_datetime(df['dt'], unit='s')
    return df
    
def process_data(df):
    print('testando essa aqui')
    #cria aqui as regras que pedem no escopo do projeto
    df = parse_date(df)
    return df

def write_table(df,db,tb_output,bucket,key):
    print('Escrevendo dados no bucket')
    data_atual = datetime.now()
    ano, mes, dia = data_atual.year, data_atual.month, data_atual.day
    path = f"s3://{bucket}/{key}{ano}{mes}{dia}/"
    
    wr.s3.to_parquet(
        df=df,
        database=db,
        table=tb_output,
        dataset=True,
        path=path,
        mode='overwrite',
        partition_cols=['dt']
    )

if __name__ == "__main__":
    bucket = "bucket-name"
    caminho_bucket_entrada = "dados_entrada/clima/anomesdia="
    dias = ["20240505", "20240506", "20240507","20240508","20240509","20240510","20240511","20240512","20240513","20240514","20240515","20240516","20240517","20240518","20240519","20240520","20240521","20240522","20240523","20240524"]

    db_destino = 'db_workspace_shared_account'
    tb_destino = 'tb_dados_api_openweathermap'
    caminho_bucket_saida = f"dados_saida/clima_processado/{tb_destino}/anomesdia="
    
    df = ler_json_do_s3(bucket,caminho_bucket_entrada,dias)
    print('DataFrame resultante da API:')
    print(df.head())
    print('Informações do DataFrame:')
    print(df.info())
    
    print('processar dados da api')
    df_clean = process_data(df)
    
    print('escrever dados no bucket')
    write_table(df_clean,db_destino,tb_destino,bucket,caminho_bucket_saida)

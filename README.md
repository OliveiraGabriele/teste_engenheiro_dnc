# Repo do desafio ESCOLA DNC


# Desafio de Engenheiro de Dados - Zebrinha Azul

Contexto
A Zebrinha Azul é uma startup inovadora que se destaca no mercado por sua expertise em lidar com dados de clima e tráfego. Este repositório contém a solução para o desafio proposto, que envolve a extração, transformação, modelagem e visualização de dados de clima e tráfego.

# Ferramentas e Tecnologias Utilizadas

Agendamento e Monitoramento:
AWS EventBridge, AWS CloudTrail, AWS CloudWatch.

Ingestão:
AWS Lambda.

Processamento:
AWS Step Functions (Workflow), AWS Glue.

Armazenamento:
Amazon S3.

Análise:
AWS Glue Catalog, Amazon Athena.

# Configuração e Execução

Pré-requisitos
Python 3.8 ou superior, 
AWS CLI configurado, 
Conta na AWS com as devidas permissões para as ferramenas escolhidas,
Chave de API da OpenWeatherMap:https://openweathermap.org/api


# Configuração das Variáveis de Ambiente
Configure as seguintes variáveis de ambiente no AWS Lambda:

API_KEY - Sua chave de API da OpenWeatherMap.

S3_BUCKET - Nome do bucket S3 onde os dados serão armazenados.

# Código de Ingestão de Dados (Lambda Function):
Código do Lambda para coletar dados de clima da OpenWeatherMap

# Código de ETL
Código para execução de ETL e escrita no Amazon S3

# Código de workflow
 Código que define a sequência de etapas para realizar o processo de ETL (Extração, Transformação e Carga) dos dados coletados da OpenWeatherMap. Ele inicia um job no AWS Glue, que executa as tarefas de transformação e carga dos dados no Amazon S3. Essa abordagem automatizada e escalável simplifica a execução do ETL.

# Scripts SQL para Análise de Dados
Contem alguns scripts SQL que podem ser úteis para análise dos dados armazenados no Amazon S3. As consultas podem ser executados no Amazon Athena para extrair insights valiosos dos dados.

Arquitetura do Sistema
A seguir está o diagrama da arquitetura do sistema:
![image](https://github.com/OliveiraGabriele/teste_engenheiro_dnc/assets/79588089/9f65456d-7ab6-4997-8eed-4e2d00a6a86b)

## Escolha das Ferramentas e Tecnologias

### Agendamento e Monitoramento:
Optei por utilizar AWS EventBridge, AWS CloudTrail e AWS CloudWatch devido à integração direta com outros serviços da AWS, facilidade de configuração e escalabilidade.

### Ingestão:
Escolhi a AWS Lambda para a ingestão de dados devido à sua capacidade de execução de código sem a necessidade de provisionamento de servidores, o que proporciona flexibilidade e economia de recursos.

### Processamento:
Para o processamento dos dados, optei por usar AWS Step Functions para orquestração de fluxos de trabalho e AWS Glue para execução de tarefas de ETL (Extração, Transformação e Carga). Essas ferramentas oferecem escalabilidade, automação e integração com outros serviços da AWS.

### Armazenamento:
Amazon S3 foi selecionado como o local de armazenamento devido à sua durabilidade, escalabilidade e baixo custo. Além disso, sua integração com outros serviços da AWS facilita o processamento e análise de dados.

### Análise:
Para análise de dados, optei por utilizar AWS Glue Catalog para metadados e Amazon Athena para consultas SQL sobre os dados armazenados no S3. Essas ferramentas fornecem uma maneira eficiente e escalável de realizar análises em grande escala.



Este README fornece uma visão geral da solução proposta para o desafio da Zebrinha Azul, incluindo as ferramentas e tecnologias utilizada. 

# waf-log-to-opensearch

Con este repositorio podras:
- Desplegar un cluster de Opensearch
- Enviar logs existentes desde un bucket S3 a Opensearch
- Configurar la rotacion de logs
- Configurar Opensearch para el analisis de los datos recolectados
- Visualizar los datos

Requiere tenet configurada AWS CLI

## Desplegar Opensearch

Para desplegar Opensearch ejecutar el script deploy-opensearch-cluster.sh o configurar la variables en domain.json y ejecutar la ultima linea del script.
El script solicita que ingreses los parametros para la creacion del cluster, luego desde aws cli se despliega.
Para definir parametros de tamaNo y caracteristicas para el cluster, consultar [documentacion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html)
## Enviar log desde S3 a Opensearch



## Configurar rotacionde log

## Configurar Opensearch para recibir logs

## 



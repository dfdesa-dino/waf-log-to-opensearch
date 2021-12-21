# waf-log-to-opensearch

Con este repositorio podras:
- Desplegar un cluster de Opensearch
- Enviar logs existentes desde un bucket S3 a Opensearch
- Configurar la rotacion de logs
- Configurar Opensearch para el analisis de los datos recolectados
- Visualizar los datos

Requiere tener configurada AWS CLI y default zone 

## Desplegar Opensearch

Para desplegar Opensearch ejecutar el script deploy-opensearch-cluster.sh o configurar las variables en domain.json y ejecutar la ultima linea del script.
El script solicita que ingreses los parametros para la creacion del cluster, luego desde aws cli lo despliega.
Para definir parametros de tamaNo y caracteristicas para el cluster, consultar [documentacion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html)

## Enviar log desde S3 a Opensearch




## Configurar rotacionde log

## Configurar Opensearch para recibir logs
Procedemos a loguearnos a la GUI de nuestro cluste http://OPENSEARCH-DOMAIN/_dashboard/  y en Menu > Dev Tools , pegamos el contenido de file://opensearch/index-template.json y lo ejecutamos. 
![Template](/assets/DevToolsOpenSearch.png)

## Importar Dashboards y Vizualizaciones

Con el server ya configurado y con logs indexados. Procedemos a importar los daschboards y las vizualizaciones desde Menu > Stack Management > Saved Objects Import, Seleccionamos Request action on conflict y procedemos a importar seleccionando el nombre de nuestro index pattern.
Las dashboards son credisto [de](https://github.com/aws-samples/aws-waf-ops-dashboards)


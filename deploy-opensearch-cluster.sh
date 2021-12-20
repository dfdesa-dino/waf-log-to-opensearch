
#!/bin/bash


read -p "Ingresa el nombre del Dominio (Opensearch Cluster): " domain 
export ES_DOMAIN_NAME=$domain

# Elasticsearch version
export ES_VERSION="OpenSearch_1.0"

echo  "Ingresar tipo de instancia : \n " 
cat instance.txt
echo "\n"
read  ins_type

export TYPE=$ins_type

read -p "Ingresa numero de nodos: " count
export NODE_COUNT=$count

read -p "Ingresa el tamaNo por nodo: " vol_size
export VOL_SIZE=$vol_size

read -p "Ingresa nombre de usuario de Opensearch :" user
export ES_DOMAIN_USER=$user

read -p "Ingresa una password :" pass
export ES_DOMAIN_PASSWORD=$pass


envsubst < domain.json > domain.json
aws opensearch create-domain --cli-input-json  file://domain.json


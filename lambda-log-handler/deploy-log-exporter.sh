# Install Dependancies

apt update && apt -y install python-pip zip
pip3 install virtualenv

 
mkdir -p s3-to-es 
virtualenv s3-to-es
cd s3-to-es && source bin/activate
pip3 install requests_aws4auth -t .
pip3 install requests -t .
pip3 freeze > requirements.txt

cp ../log-exporter.py .

chmod 754 log-exporter.py
# Package the lambda runtime
zip -r ../log-exporter.zip *


##aws lambda update-function-code --function-name $EXPORTER --zip-file fileb://../log-exporter.zip

ssh -i sbh-cloudproject3-ec2-emr-key-pair.pem "$1" "export PYSPARK_PYTHON=/usr/bin/python3; spark-submit ~/prediction.py"

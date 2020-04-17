ssh -i ../sbh-cloudproject3-ec2-emr-key-pair.pem hadoop@ec2-54-215-207-33.us-west-1.compute.amazonaws.com "export PYSPARK_PYTHON=/usr/bin/python3; spark-submit prediction.py"


scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem ../sbh-cloudproject3-ec2-emr-key-pair.pem "$1":~
scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem launch_predictor.sh "$1":~
scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem bootstrap.sh "$1":~
scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem post_script.py "$1":~

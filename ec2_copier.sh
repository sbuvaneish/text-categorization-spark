scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem ../sbh-cloudproject3-ec2-emr-key-pair.pem "$1":~
scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem launch_predictor.sh "$1":~

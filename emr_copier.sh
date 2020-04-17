scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem bootstrap.sh "$1":~
scp -i ../sbh-cloudproject3-ec2-emr-key-pair.pem prediction.py "$1":~
ssh -i ../sbh-cloudproject3-ec2-emr-key-pair.pem "$1" "bash ~/bootstrap.sh"
exit

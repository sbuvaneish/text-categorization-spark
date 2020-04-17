curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
echo "export PATH=~/.local/bin:$PATH" >> ~/.bash_profile
source ~/.bash_profile
export PYSPARK_PYTHON=/usr/bin/python3
pip install keras
pip install boto3

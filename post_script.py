import re
import sys
import subprocess

public_dns = sys.argv[1]
request_id = sys.argv[2]

pat = r'.*?(\{.*}).*'
output = subprocess.check_output(['bash', 'launch_predictor.sh', public_dns, request_id]).decode('utf-8')
match = re.search(pat, output)
result = match.group(1)
print(result)

#Executing from main
from w3c import get_version, test_data_model_v1
import sys
import json
json_str=sys.argv[1] 
vc = json.loads(json_str)
print(get_version(vc))
print('\n',test_data_model_v1(vc))

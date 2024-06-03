from .w3c import test_data_model_v1
import sys
import json

def main():
    args = sys.argv[1:]
    vc = json.loads(args[0])
    results = json.dumps(test_data_model_v1(vc), indent=2)
    print(results)

if __name__ == '__main__':
    main()

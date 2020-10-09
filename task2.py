import argparse
import json

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('input', nargs='?')
parser.add_argument('output', nargs='?')
args = parser.parse_args()

with open(args.__getattribute__('input')) as e:
    data = json.load(e)

json_end = []
for sr in data["exchangeRate"]:
    if sr["saleRateNB"] > 15.0:
        json_end.append(sr["currency"])

print(data)
print(json_end)
with open(args.__getattribute__('output'), "w") as f:
    json.dump(json_end, f)


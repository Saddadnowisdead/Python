import json
with open("exchange1.json") as e:
  data = json.load(e)

json_end = []
for sr in data["exchangeRate"]:
  if sr["saleRateNB"] > 15.0:
    json_end.append(sr["currency"])


print(data)
print(json_end)
with open("exchange.json", "w") as f:
  json.dump(json_end, f)


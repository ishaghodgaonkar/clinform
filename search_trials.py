import requests

resp = requests.post("https://clinicaltrialconnect.dev/graphql/")

if resp.status_code != 200:
    # This means something went wrong.
    print("error", resp.status_code)
    exit()

for item in resp.json():
    print(item)

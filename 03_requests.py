import requests
res = requests.get("http://google.com")
res.raise_for_status()

print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)

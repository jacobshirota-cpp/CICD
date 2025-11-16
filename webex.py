import requests, json

accessToken = "Bearer MDFiYWYzYzUtOWMxNS00ZDRlLWFmNzUtM2ViMjY2ZjcxNTY3ZGNkYTcyOWUtNzJj_P0A1_13494cac-24b4-4f89-8247-193cc92a7636"

r = requests.post("https://webexapis.com/v1/messages",
    data = json.dumps({
        "roomId":"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZDQwNjU1YjAtYzJhNi0xMWYwLWI1NTAtYTE2YmE0ZGQ0ZTE2",
        "text":"Jenkins has completed a build."
    }),
    headers = {
        "Authorization":accessToken,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
)

print(r.text)

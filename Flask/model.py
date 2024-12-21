from urllib import request
import json

def get_meme():
    url="https://meme-api.com/gimme"
    req=request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as response:
        response_text=response.read().decode("utf-8")
        response_text=json.loads(response_text)
        preview= response_text["preview"][-2]
        subreddit=response_text["subreddit"]
        return preview,subreddit
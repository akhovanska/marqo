#using not usual request -> httpx
import httpx
r = httpx.get('https://www.marqo.ai/')

print(r)

print(r.status_code)

print(r.headers['content-type'])

print(r.text)

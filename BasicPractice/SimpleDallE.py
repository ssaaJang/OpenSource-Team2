#Simple DallE practice

# 출처 : https://medium.com/codingthesmartway-com-blog/mastering-dall-e-api-in-python-beginners-guide-257aceaff7b7

import openai
import os

openai.api_key = "insert OpenAPI Key"


response = openai.Image.create(
  prompt="white dog",
  model="image-alpha-001",
  n=1,
  size="1024*1024",
  response_format="url"
)

link = response['data'][0]["url"]
print(link)




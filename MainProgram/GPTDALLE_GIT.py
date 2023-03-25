
import openai
import os

openai.api_key = "insert API KEY"

messages = []
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip() # chatGPT 에게 받은 대답

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    #print(f"GPT : {assistant_content}")
    response = openai.Image.create(
        prompt=assistant_content,
        model="image-alpha-001",
        n=1,
        size="256x256",
        response_format="url"
    )
    link = response['data'][0]["url"]
    print(link)











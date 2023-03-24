# Chatbot program
# 출처 : https://blog.naver.com/kimflstudio/223045193407

# 1. API Key, import openai https://jakely.tistory.com/4

# 2. code
import openai

openai.api_key = "insert OpenAPI Key"

messages = []
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip() # chatGPT 에게 받은 대답

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")



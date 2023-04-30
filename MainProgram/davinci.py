# turbo 모델 트래픽 오류
# davinci 모델로 바꿈
# 첫문장만, 불용어 제거, 

import os
import openai
from PIL import Image
import streamlit as st
from openai.error import InvalidRequestError

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import re
regex = r"[^a-zA-Z0-9 ]"

def StopWord(sentence):
    subst = ""
    sentence = re.sub(regex, subst, sentence)
    print(sentence)

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(sentence)

    result = []
    for word in word_tokens:
        if word not in stop_words:
            result.append(word)

    print('불용어 제거 전:',word_tokens)
    print('불용어 제거 후:',result)

    print(result[0])

    st = ",".join(result)
    print(st)
    return st




openai.api_key = 'insert API KEY'
messages = []
#tt= []
#chatGPT

def openai_completion(prompt):
    response = openai.Completion.create(
      #model="gpt-3.5-turbo",
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      temperature=0.5
    )
    return response['choices'][0]['text']

#DALLE
def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=2,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url



try:
    input_text = st.text_area("Please enter text here... 🙋",height=50)
    
    input_button = st.button("Go answer")
    openai_answer = openai_completion(input_text)
    
    tt = openai_answer

    if input_button:
        #st.write(openai_answer)
        st.write(tt)
    

    #if input_button and input_text.strip() != "":
    #        with st.spinner("Loading...💫"): 
    #            st.success(openai_answer)            
    #if input_text.strip() != "":
    #st.markdown(openai_answer)
    print('ONE!!',openai_answer)
    print('tt',tt)
    #print('tt',tt)
    #image_button = st.button("Generate Image 🚀")

    if st.button("Generate Image 🚀"):
        #image_url = openai_image(openai_answer)
        print('imga tt',tt)
        
        # 첫 문장만 가져오기
        ll = tt.split('.')  
        # 중간에 tt를 텍스트 마이닝 => 함수 넣기
        print('fisrt text',ll[0])
        tt = StopWord(ll[0])
        print('StopWord tt',tt)

        
        image_url = openai_image(tt)
        print(image_url)
        st.image(image_url, caption='Generated by DALLE')
    else:
        st.warning("Please enter something! ⚠")

    #if image_button and input_text.strip() != "":
    #    with st.spinner("Loading...💫"):
    #        print('TWO!!',openai_answer)
           
    #        image_url = openai_image(openai_answer)
            #chatgpt_answer = openai_completion(input_text)
            #st.success(chatgpt_answer)
    #        print(image_url)
    #        st.image(image_url, caption='Generated by DALLE')
    #else:
    #    st.warning("Please enter something! ⚠")
except InvalidRequestError as e:
    print('error!!!')
    st.markdown("It looks like this request may not follow DALL-E content policy.  \nAsk me the question again")
    

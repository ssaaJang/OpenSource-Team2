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

#keyword
import numpy as np
import itertools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


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

def KeyWordFun(doc):
    n_gram_range = (3, 3)
    stop_words = "english"

    count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
    candidates = count.get_feature_names_out()

    #print('trigram 개수 :',len(candidates))
    #print('trigram 다섯개만 출력 :',candidates[:5])

    model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)

    top_n = 3
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]

    ss = ",".join(keywords)
    print(ss)
    print(keywords)
    return ss

openai.api_key = 'insert key'
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
    

    format_type = st.sidebar.selectbox('Choose Option',["Basic","First Sentence & StopWord","KeyWord","First Sentence","Summary"])

   #Basic : 정제 안함
    if format_type == "Basic":
        st.title("Basic")
        input_text = st.text_area("**텍스트를 입력하세요** 🙋",height=60)
        
        input_button = st.button("확인!")
        openai_answer = openai_completion(input_text)
        
        tt = openai_answer

        if input_button:
            #st.write(openai_answer)
            st.write(tt)
        

       
        print('ONE!!',openai_answer)
        print('tt',tt)

        if st.button("이미지 생성하기... 🎞 🚀"):
            print('imga tt',tt)            
            image_url = openai_image(tt)
            print(image_url)
            st.image(image_url, caption='Generated by DALLE')
        else:
            st.warning("텍스트를 입력하세요! ⚠")        
    
    # First Sentence & StopWord : 첫문장 선택 + 불용어 제거 (단어만)
    elif format_type == "First Sentence & StopWord":
        st.title("First Sentence & StopWord")
        input_text = st.text_area("**텍스트를 입력하세요** 🙋",height=60)
        
        input_button = st.button("확인!")
        openai_answer = openai_completion(input_text)
        
        tt = openai_answer

        if input_button:
            #st.write(openai_answer)
            st.write(tt)
        

     
        print('ONE!!',openai_answer)
        print('tt',tt)
        

        if st.button("이미지 생성하기... 🎞 🚀"):
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
            st.warning("텍스트를 입력하세요! ⚠")        
        
    
    #KeyWord : 핵심키워드 추출 (, 로 연결)
    elif format_type == "KeyWord" :
        st.title("KeyWord")
        input_text = st.text_area("**텍스트를 입력하세요**🙋",height=60)
        input_button = st.button("Go answer")
        openai_answer = openai_completion(input_text)
        
        tt = openai_answer

        if input_button:
            #st.write(openai_answer)
            st.write(tt)
        

     
        print('ONE!!',openai_answer)
        print('tt',tt)
        

        if st.button("이미지 생성하기... 🎞 🚀"):
            #image_url = openai_image(openai_answer)
            print('imga tt',tt)
            
            tt = KeyWordFun(tt)
            print('Keyword',tt)
            image_url = openai_image(tt)
            print(image_url)
            st.image(image_url, caption='Generated by DALLE')
        else:
            st.warning("텍스트를 입력하세요! ⚠")
    
    #First Sentence : 첫문장만 선택
    elif format_type == "First Sentence":
        st.title("First Sentence")
        input_text = st.text_area("**텍스트를 입력하세요** 🙋",height=60)
        
        input_button = st.button("Go answer")
        openai_answer = openai_completion(input_text)
        
        tt = openai_answer

        if input_button:
            #st.write(openai_answer)
            st.write(tt) 
        print('ONE!!',openai_answer)
        print('tt',tt)
        if st.button("이미지 생성하기... 🎞 🚀"):
            #image_url = openai_image(openai_answer)
            print('imga tt',tt)
            
            # 첫 문장만 가져오기
            ll = tt.split('.')  
            # 중간에 tt를 텍스트 마이닝 => 함수 넣기
            print('fisrt text',ll[0])
            tt = ll[0]

            
            image_url = openai_image(tt)
            print(image_url)
            st.image(image_url, caption='Generated by DALLE')
        else:
            st.warning("텍스트를 입력하세요! ⚠")
        


    # Summary : 자연어 결과 요약 => chatGPT 에 물어보기?
    else :
        inputex = ''


except InvalidRequestError as e:
    print('error!!!')
    st.markdown("It looks like this request may not follow DALL-E content policy.  \nAsk me the question again")
    
    
    
    
    이재영 형태소를 분석하는  POS Tagging
    
    추가적인 코드 입니다. 출처 sumit Raj 파이썬으로 챗봇 만들기 저자 
    
    nlp = spacy.load('en') // spacy 영어 모델을 파이썬 오브젝트에 로드
    doc = nlp(u'I am learning how to build chatbots') // 토큰을 위한 doc 오브젝트 생성
    for token in doc:
            print(token.text,token.pos_)   // 토큰과 형태소 결과를 출력
    

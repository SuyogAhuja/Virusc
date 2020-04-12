from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
from flask import Flask, escape, request, render_template
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

article = Article('https://www.mayoclinic.org/diseases-conditions/coronavirus/symptoms-causes/syc-20479963')
article.download()

article.parse()
article.nlp()
corpus = article.text
#print(corpus)
text = corpus
sent_tokens = nltk.sent_tokenize(text) 

#remove punctuations
remove_punct_dict = dict(  ( ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))


GREETING_INPUTS = ["hi", "hello", "hola", "greetings", "wassup", "hey"]
GREETING_RESPONSES=["howdy", "hi", "hey", "hello", "hey there"]

#Function to return a random greeting response to a users greeting
def greeting(sentence):
  for word in sentence.split():
    if word.lower() in GREETING_INPUTS:
      return random.choice(GREETING_RESPONSES)



#main function
def response(user_response):
  user_response = user_response.lower() 
  robo_response = ''
  sent_tokens.append(user_response)

  TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words='english')

 
  tfidf = TfidfVec.fit_transform(sent_tokens)

  vals = cosine_similarity(tfidf[-1], tfidf)
 
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  score = flat[-2]

  if(score == 0):
    robo_response = robo_response+"I apologize, I don't understand."
  else:
    robo_response = robo_response+sent_tokens[idx]
  
  sent_tokens.remove(user_response)
  
  return robo_response

def run(response2):
 flag = True
 
 while(flag == True):
   print(response2)
   user_response = response2.lower()
   if(user_response != 'bye'):
     if(user_response == 'thanks' or user_response =='thank you'):
      flag=False
      s="VirusCBot: You are welcome !"
      return render_template ('chatbot.html', response1=s)
     else:
       if(greeting(user_response) != None):
           b="VirusCBot: "+greeting(user_response)
           return render_template ('chatbot.html', response1=b)
       else:
           c="VirusCBot: "+response(user_response)
           return render_template ('chatbot.html', response1=c)   
   else:
    flag = False
    d="VirusCBot: Thank You Chat with you later !"
    return render_template ('chatbot.html', response1=d)
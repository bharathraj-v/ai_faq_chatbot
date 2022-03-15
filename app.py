import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
from tkinter import *
import numpy as np

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result
def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg!="":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "\nYou: " + msg + '\n\n')
        ChatLog.config(foreground="#000000", font=("Verdana", 12 ))
        res = chatbot_response(msg)
        ChatLog.insert(END, ""+ res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("Capital Bank - Assistant")
base.geometry("800x600")
base.resizable(width=FALSE, height=FALSE)
logo = PhotoImage(file = "winicon.png")
base.iconphoto(False, logo)
ChatLog = Text(base, bd=0, bg="#ffffff", height="16", width="100", font="Arial 10 bold")
ChatLog.config(state=DISABLED)
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="24", height=5,
                    bd=0, bg="#000000", activebackground="#404040",fg='#ffffff',
                    command= send )
EntryBox = Text(base, bd=0, bg="white",width="58", height="5", font="Arial")

scrollbar.place(x=782,y=6, height=525)
ChatLog.place(x=6,y=6, height=525, width=776)
SendButton.place(x=520, y=545, height=45)
EntryBox.place(x=10, y=545, height=45, width=500)
base.mainloop()

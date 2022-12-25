# Bank FAQ Chatbot
A generic chatbot that answers frequently asked questions for a bank. Built using Dense Neural Network. The Dense Neural Network is trained upon the intents from intents.json file that contains answers for Frequently Asked Questions The intents are preprocessed using Natural Language Toolkit. The preprocessing done using NLTK are Tokenization and Lemmatization. 


**Dense Neural Networks**: 

A dense neural network, also known as a fully connected neural network, is a type of neural network in which all the nodes in one layer are connected to all the nodes in the next layer. This means that each node in the input layer is connected to every node in the hidden layer, and each node in the hidden layer is connected to every node in the output layer. In a dense neural network, there are no skipped connections or disconnected nodes.

**Natural Language Toolkit**:

https://www.nltk.org/

NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.


## Running the Chatbot
1. ```pip install keras```
2. ```pip install nltk```
3. ```pip install tensorflow```
4. In the Python Terminal, ```import nltk``` and call ```nltk.download()``` and download the NLTK data
5. ```pip install numpy```
6. Run app.py file

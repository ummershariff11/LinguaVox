##  Due to storage crunch in github, you can access all the rest of files including datasets and code on the below path

https://mylambton-my.sharepoint.com/personal/c0796681_mylambton_ca/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fc0796681%5Fmylambton%5Fca%2FDocuments%2FLinguaVox%5FInsight%5FInspectors



## Abstract 

As we all know, physically challenged people especially the hearing and speaking have difficulty communicating effectively in their daily lives. We have created a web-based application to translate sign language to text and vice versa because most people do not learn sign language, and interpreters are few. Using neural networks, the sign language for fingerspelling-based American sign language is detected in real-time, and text is translated to sign language. When the user chooses the sign language to text option, the user's hand is first filtered. Following that, our approach is sent via a classifier, which predicts the class of hand motions that will be used to show the appropriate letter. When the user selects text to sign language, the text is processed and translated into appropriate sign language video. Our method is 95.7 percent accurate for the alphabet's 26 letters.

Keywords: American Sign Language, Neural Networks, Artificial Intelligence

## Introduction

The number of hearing and speaking impaired people worldwide is staggeringly high and roughly calculated to be millions. Of these 63 percent, they are said to be born deaf. The others lose their hearing by different accidents. Over one percent of Canada's population or approximately half a million people are physically challenged. In Ontario, an estimated 211,250 such individuals. 
Since more than 90 percent of deaf children are born to hearing parents, many adults need to learn sign language, but it is practically impossible. There are few reliable statistics on which signed languages are most spoken or widespread. Still, the top 3 candidates are American Sign Language (ASL), British Sign Language (BSL), or Australian Sign Language (Auslan). 
ASL is a good contender for the title; hence we will be using it for our project as it is used in the U.S. And Canada (with some regional differences). We created a program that converts sign language to text and vice versa. The sign language for fingerspelling-based American sign language is detected in real-time using neural networks. When the user chooses the sign language to text option, the user's hand is first filtered. 
It is then sent via a classifier in our technique, which predicts the class of the hand motions to reveal the matching letter. We intend to develop a model that can recognize Fingerspelling-based hand motions and combine them to make a whole word. The gestures that we want to improve are depicted in the image below Figure 1.
 When The text to sign language option is selected, the text is processed and translated into an appropriate sign language video. On the next page, we have a figure that shows the symbolic representation of American Sign Language. 

![alt text](https://github.com/ummershariff11/linguavox/blob/master/others/Picture%201.jpg?raw=true)

Figure : ASL Letters



## Methods

We wanted to implement a product that would be useful to everyone who wants to communicate with specially-abled people. We wanted to create an application that will integrate Sign Language to Text and Text to Sign Language Detection. So, we have divided our project into two different modules – 

1: Sign Language to Text 
2: Text to Sign Language

These two modules are an integral part of our project, and they are available to users on the landing page of our website itself. We have also represented our LinguaVox architecture below.

![alt text](https://github.com/ummershariff11/linguavox/blob/master/others/Picture%202.png?raw=true)

Figure : LinguaVox Architecture



## Sign to Text


In the first module, we wanted to detect sign language and then capture the sign language portrayed by the user and convert it to text which other users can understand.
![alt text](https://github.com/ummershariff11/linguavox/blob/master/others/Picture%203.png?raw=true)

Figure : Sign Language To Text Workflow

To achieve this, the flow we have followed is we identified characters, words, and sentences from video input; on top of that, we also included some word suggestions for the signs.




## Text to Sign 

We have discussed the translation of sign language to text, and in our product, we facilitate the translation vice versa, i.e., text to sign language. We will be translating the text in English to ASL and displaying the text from the user as a sign language video. The below flowchart describes the flow of text to sign language translation.

![alt text](https://github.com/ummershariff11/linguavox/blob/master/others/Picture%2010.png?raw=true)

Figure: Text to Sign Language Workflow



## Results

We developed a user-friendly UI available on the web and standalone desktop applications as a final deliverable. Users can download the two applications one time and use them without having internet access. The below screenshots illustrate our web application and functional overview of it.


![alt text](https://github.com/ummershariff11/linguavox/blob/master/others/Picture%2013.png?raw=true)


Figure: LinguaVox Functionality Description



The above image shows how the website looks like. When a user lands on the website, one has two options: Text to Sign and Sign to Text. Upon clicking on either a respective pop-up will open and take input as text or sign and show the predicted result.
Once a user clicks on the Sign Language to Text, we get a pop-up that displays user images to portray the ASL and get their desired results.
If the user wants to use our Text to Sign Language module, once they click on the hyperlink given on the website, the below pop-up opens up. The user can type down their desired text and receive their result played in a video format.




## Conclusions and Future Work


We intend to increase accuracy even in cluttered backgrounds by experimenting with various background removal approaches. We're also thinking about improving the Pre-Processing to make predicting gestures in low-light conditions much easier. The present work only works with ASL, but that might be extended to work with other native sign languages with the correct data and training. Although fingerspelling translator is used in this project, sign languages are also spoken in context, with each gesture indicating an item or a sentence. As a result, detecting contextual signing would demand further processing and natural language processing (NLP).



## References

Bhatia, R. (2018). Neural Networks Do Not Work Like Human Brains – Let's Debunk The Myth. Analytics India.
https://analyticsindiamag.com/neural-networks-not-work-like-human-brains-lets-debunk-myth/

Byeongkeun K., Subarna T., Truong Q. (2015). Real-Time Sign Language Fingerspelling Recognition Using Convolutional Neural Networks From Depth Map – 3rd IAPR Asian Conference on Pattern Recognition (ACPR).

N. Mukai, N. Harada and Y. Chang. (2017). Japanese Fingerspelling Recognition Based on Classification Tree and Machine Learning. Kyoto, Japan, 2017, pp. 19-24.

Pierson, L. (2019). Python for Data Science Essential Training Part 1 [MOOC]. LinkedIn Learning.
https://www.linkedin.com/learning/python-for-data-science-essential-training-part-1?u=56968457

Pierson, L. (2019). Python for Data Science Essential Training Part 2 [MOOC]. LinkedIn Learning.
https://www.linkedin.com/learning/python-for-data-science-essential-training-part-2?u=56968457

Pigou L., Dieleman S., Kindermans PJ., Schrauwen B. (2015). Sign Language Recognition Using Convolutional Neural Networks. Computer Vision - ECCV 2014 Workshops. ECCV 2014. Lecture Notes in Computer Science, vol 8925.






## Group Members and Project Collaborators:
Avinash Ravi: https://github.com/avinash-ravi

Ankur Rokad: https://github.com/ankurrokad

Sahista Patel: https://github.com/Sahista-Patel

Ummer Shariff: https://github.com/ummershariff11

Vishal Sabarinath: https://github.com/vishal9849


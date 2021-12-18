## Abstract 
As we all know, vocally and hearing-impaired people face difficulties in their daily lives to communicate effectively. Because most individuals do not learn sign language and interpreters are few, we developed an application for translating sign language to text and vice versa. The sign language is detected in real-time for fingerspelling-based American sign language using neural networks and translating text to sign language. If the user selects the sign language to text option, the hand is initially passed through a filter. Our method, following which, is passed through a classifier, which predicts the class of the hand motions to show the corresponding letter. When the user selects text to sign language, the text is processed and translated to related sign language videos. For the 26 letters of the alphabet, our method is 95.7 percent accurate.
Keywords: American Sign Language, Neural Networks, Artificial Intelligence

## Introduction
The number of hearing and speaking impaired people worldwide is staggeringly high and roughly calculated to be millions. Of these 63 percent, they are said to be born deaf. The others lose their hearing by different accidents. Over one percent of Canada's population or approximately half a million people are physically challenged. In Ontario, an estimated 211,250 such individuals. 
Since more than 90 percent of deaf children are born to hearing parents, many adults need to learn sign language, but it is practically impossible. There are few reliable statistics on which signed languages are most spoken or widespread. Still, the top 3 candidates are American Sign Language (ASL), British Sign Language (BSL), or Australian Sign Language (Auslan). 
ASL is a good contender for the title; hence we will be using it for our project as it is used in the U.S. And Canada (with some regional differences). We created a program that converts sign language to text and vice versa. The sign language for fingerspelling-based American sign language is detected in real-time using neural networks. When the user chooses the sign language to text option, the user's hand is first filtered. 
It is then sent via a classifier in our technique, which predicts the class of the hand motions to reveal the matching letter. We intend to develop a model that can recognize Fingerspelling-based hand motions and combine them to make a whole word. The gestures that we want to improve are depicted in the image below Figure 1.
 When The text to sign language option is selected, the text is processed and translated into an appropriate sign language video. On the next page, we have a figure that shows the symbolic representation of American Sign Language. 

![alt text](https://github.com/ummershariff11/linguavox/blob/master/others/Picture%201.jpg?raw=true)

Figure 1: ASL Letters


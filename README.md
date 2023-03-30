# Legal Innovation and Technology Submisison Group 8
## Team Members: Howsikan Kugathasan, Vaishnavan Srikumaraguru, Frid Mughal

### Introduction
This contains the codebase and documentation to our submission to the 2023 Legal Innovation Technology (LIT) competition. If you want to skip the technical stuff and see our code in action, go to this YouTube video here: LINK URL.

### An Overview
Our code does three main things
1. It reads Twitter and TikTok URLs.
  - From Twitter, it gets the text from tweets using Selenium browser automation.
  - From TikTok, it downloads the video from the TikTok, converts it to an audio file, which is then transcribed to text.
2. With the text from either of these programs, spacy does natural language processing (NLP) to get a summary of the meaning and sentiment of the message.
3. If the message is harmful (relates to an eating disorder, encourages suicide etc), the program produces a warning message which is displayed on the web page via Flask.

### Requirements
This program runs in Python 3 on Windows operytating systems. Please make sure that you have Google Chrome (version 111) and ffmpeg installed on your operating systems. Please also have chromedriver.exe in the same directory as app.py. The program runs in a Python virtual environment with the following dependencies: 
- flask
- selenium
- yt-dlp
- SpeechRecognition
- spacy

If you are running this program in Linux, ensure that the line of code which instantiates the browser is edited to say r'chromedriver' instead of r'chromedriver.exe'.

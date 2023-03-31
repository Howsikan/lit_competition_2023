#Package imports
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from yt_dlp import YoutubeDL
import speech_recognition as sr
import spacy, os, random

#This function gets a tweet's text from a given twitter.
def get_tweet_text(tweet_url):
    
    #Set up Selenium browser testing.
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(r'chromedriver.exe', options=options)
    driver.implicitly_wait(10)


    #Open tweet, get the tweet text.
    driver.get(tweet_url)
    tweet_div = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
    span_element = tweet_div.find_element(By.TAG_NAME, 'span')
    return span_element.text


#This function gets TikTok Videos.
def get_tiktok_transcript(video_url):
    
    #Get and download the TikTok MP4 video.
    url_in_list = [video_url]
    filename_random_number = random.randint(1, 1000000)
    filename = 'static/videos/{}.mp4'.format(filename_random_number)

    youtube_dl_options = {'outtmpl': filename}
    with YoutubeDL(youtube_dl_options) as ydl:
        ydl.download(url_in_list)

    #Convert the MP4 to MP3.
    mp3_filename = 'static\\audio\\' + filename.split('/')[-1].split('.')[0] + '.mp3'
    wav_filename = 'static\\audio\\' + filename.split('/')[-1].split('.')[0] + '.wav'
    mp3_command_string = f'ffmpeg -i {filename} {mp3_filename}'
    wav_command_string = f'ffmpeg -i {mp3_filename} {wav_filename}'
    os.system(mp3_command_string)
    os.system(wav_command_string)

    #Get the text from the video using text recognition.
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(wav_filename)
    with audio as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    
    #Clean up the server's space by deleting mp3/mp4/wav files
    files_to_delete = [filename, mp3_filename, wav_filename]
    for file in files_to_delete:
        os.remove(file)
    
    return text    


#This function does NLP with tweet texts or TikTok transcripts.
def parse_text(text):
    
    #Tokenization.
    nlp = spacy.load('en')
    tokenized_text = nlp(text)

    #Lemmatization.
    for token in tokenized_text:
        print(token.lemma)

    #Meaning recognition.

#Set up the Flask forms.
class URLForm(FlaskForm):
    #These fields need 'name' attributes.
    url_field = StringField('Your URL', validators=[DataRequired()])
    submit_field = SubmitField('Submit')

#Create the Flask app here.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Q;ny?Epj_20xI,4'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    return render_template('index.html', form=form)

#Tests for functions below.
#print(get_tweet_text('https://twitter.com/AlfonsoThrillFr/status/1641084402598813698'))
#print(get_tiktok_transcript('https://www.tiktok.com/@carnivoremd2/video/7215689099640933674'))
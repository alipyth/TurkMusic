import streamlit as st
import requests
import json
from bs4 import BeautifulSoup
from requests_html import HTMLSession

st.title("New Turkish Music")

with st.form('find song'):
    submited = submited = st.form_submit_button("Get New Hot Turkish Song")

    if submited:
        r = requests.get('https://muzikmp3indir.com/')
        soup = BeautifulSoup(r.text,'html.parser')
        musics = []
        for i in soup.select('#icerik > div > div:nth-child(1) > div:nth-child(3) > div > div.podcasts-container > div.episodes > div > div.col-10 > a'):
            musics.append(i['href'])
        hotlist = []
        for m in musics:
            s = requests.get(m)
            soup2 = BeautifulSoup(s.text , 'html.parser')
            for x in soup2.select('audio'):
                hotlist.append(x['src'])
        for songs in hotlist:
            st.audio(songs)

        
        
st.write("By Ali Jahani - satreyek@gmail.com")

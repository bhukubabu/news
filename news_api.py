import time
import streamlit as st
from newsapi import NewsApiClient

newsapi=NewsApiClient(api_key='ba889a8914344a208ea4d7db94664718')
st.subheader("Get top crime news 📰")
col1,col2=st.columns(2)
with col1:
    city=st.selectbox(placeholder="Select city",options=["",'Kolkata','Mumbai','delhi','bombay'],label='None')
with col2:
    news_type=st.selectbox(placeholder="select news type",options=["",'Crime','Accident','Theft','Suicide'],label='None')


if city=="" or news_type=="":
      st.markdown("i will fetch news for you")
else:
    all_articles=newsapi.get_everything(
    q=f"{news_type} {city}",
    sort_by='relevancy',
    page_size=5,
)
    total=len(all_articles['articles'])
    with st.spinner(f"Scrapping recent {news_type} news of {city} for you........"):
        time.sleep(3)
        for i in range(total-1,-1,-1):
            with st.container(height=600,border=True):
                    try:
                        img=all_articles['articles'][i]['urlToImage']
                        st.image(img,use_column_width=True)
                    except:
                        st.write("🖼")
                    t=all_articles['articles'][i]['title']
                    d=all_articles['articles'][i]['description']
                    
                    st.subheader(f"{t}")
                    st.markdown(f"{d}")
                    url=t=all_articles['articles'][i]['url']
                    st.markdown(f"Read More {url}")
            #st.write(f"")
#for i in range(total):


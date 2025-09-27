import streamlit as st 

import requests


st.set_page_config(page_title="MushafWEBAPP", page_icon="📖")

st.title("Mushaf APP 📖 ")

st.sidebar.title("Controls")
st.sidebar.write("Select an surah ")


surah_list = requests.get("http://api.alquran.cloud/v1/surah").json()["data"]
surah_names = [f"{s['number']}.{s['englishName']}.({s['name']})" for s in surah_list]


selected_Surah=st.sidebar.selectbox("choose surah", surah_names)
selected_surah_num=int(selected_Surah.split(".")[0])

search_keyword=st.sidebar.text_input("Surah Kewords search")

show_translation=st.sidebar.checkbox("Show Translation")
translation_choice =st.sidebar.selectbox("Choose Translation",["ur.maududi","ur.junagarhi", "ur.jalandhry"])



recitation_url=f"https://api.alquran.cloud/v1/surah/{selected_surah_num}/ar.alafasy"

recitation_response= requests.get(recitation_url).json()
arabic_ayah=recitation_response["data"]["ayahs"]

if show_translation:
    translation_url=f"https://api.alquran.cloud/v1/surah/{selected_surah_num}/{translation_choice}"
    translation_response= requests.get(translation_url).json()
    translated_ayahs=translation_response["data"]["ayahs"]
else:
    translated_ayahs=[None]*len(arabic_ayah)





if search_keyword.strip():
    filter_ar=[]
    filter_tr=[]
    for i, ayah in enumerate(arabic_ayah):
        if search_keyword in ayah["text"]:
            filter_ar.append(ayah)
            filter_tr.append(translated_ayahs[i])
    arabic_ayah=filter_ar
    translated_ayahs=filter_tr


st.subheader(selected_Surah)

for i , ayah in enumerate(arabic_ayah):
        st.markdown(f"**{ayah['numberInSurah']}** - {ayah['text']}")
        if 'audio' in ayah  and ayah ["audio"]:
            st.audio(ayah["audio"], format="audio/mp3")
        if show_translation and translated_ayahs[i]:
            st.info(translated_ayahs[i]["text"])


st.markdown("----")
st.markdown("Developed by SMAS")
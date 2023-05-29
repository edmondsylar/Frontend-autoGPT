import streamlit as st
from audiorecorder import audiorecorder
from engine import transcribe
import string
import random
import os
from streamlit_webrtc import webrtc_streamer

# function to create randome filename.
def random_filename():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))


st.title("AI Powered surveys")

def record():
    audio = audiorecorder("Start", "Stop", "Save")  

    if len(audio) > 0:

        st.audio(audio.tobytes())

        file_name = "recording_"+random_filename()
        # save the audion file as an mp3
        mp3_file = open(f"recordings/{file_name}.wav", "wb")
        mp3_file.write(audio.tobytes())
        mp3_file.close()
        if mp3_file:
            # transcribe the audio
            transcription = transcribe(f"recordings/{file_name}.wav")
            print(transcription)

            # write the response into a text file
            with open(f"recordings/{file_name}.txt", "w") as f:
                f.write(transcription)
                # update the transcription



def main():
   
#    create columns to arrange the main view
    c_1, c_2 = st.columns([0.2, 0.8])

    with c_1:
        # webrtc_streamer(key="main_cam")
        record()

        # recordings.
        st.markdown("##### Records")


    with c_2:
        st.subheader("Transcription | Reporting")       
        
        tab_1, tab_2 = st.tabs(["Survey Instructions", "Reports and analytics"])

        # populate the tabs
        with tab_1:

            home, assistant = st.columns([0.6, 0.4])
            with home:
                st.markdown("""
                    ### Survery Questionaire.
                    **Note:** This is an ai system and ensures your conversation stays natuaral. Have a converstaion with your interviewee and just ensure to ask all the questions listed in whichever order the conversation allows.   

                    1. How often do you use this type of light bulb?   
                    2. How satisfied are you with the brightness, color, and lifespan of this light bulb?   
                    3. How important are these features to you when choosing a light bulb: energy efficiency, durability, price, design, brand?   
                    4. How does this light bulb compare to other brands or products you have used before?   
                    5. How likely are you to recommend this light bulb to others?   
                    6. What do you like most and least about this light bulb?   
                    7. What improvements or suggestions do you have for this light bulb?   
                """)
            
            with assistant:
                st.subheader("Transcription")
                st.markdown("---")

        with tab_2:
            st.write('The reports generated in respect to the different transcriptions made')
            

main()
import streamlit as st
#import cv2
import pywhatkit as kit
import os

os.environ['DISPLAY'] = ':0'


def main():

    st.title("IOTE")
    st.text("Built with automation")

    activities = ["whatsapp automater"]
    choice = st.sidebar.selectbox("Select Acttivity", activities)

    if choice  == 'whatsapp automater':
        st.subheader("Whatsapp Automater")
        x = st.text_area('Enter number with Country Code (Example: +91)')
        y = st.text_area('Enter message')
        z = st.number_input('Hours', 0, 24)
        j = st.number_input('Mins', 0, 60)
        if st.button("Send Message"):  

            kit.sendwhatmsg(x, y, z,j)
            st.success("Message Sent")

 
        #except:
   
            # handling exception
            # and printing error message
            #st.error("An Unexpected Error!")




    elif choice  =='About':
        st.subheader("About")



if __name__ == '__main__':
    main()	

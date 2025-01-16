from PIL import Image
import streamlit as st 

st.set_page_config(page_title="SERA LENS | REAL ESTATE MEDIA SERVICES", page_icon=":camera:", layout="wide")

imag = Image.open("images/1.jpg")
imag_resized =imag.resize((700, 600))

log = Image.open("images/lg.png")
log_resized = log.resize((280,250))


#local css code to design the contact information
def design_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
design_css("style/s.css")

with st.container():
    left_column, right_column = st.columns([3,1])
    with left_column:
        st.subheader("S | L")
        st.title("SERA LENS | REAL ESTATE MEDIA SERVICES")
        st.write("lets do it")
        st.write("[cheak out out instagram page >](https://www.instagram.com/s_l_realestmedia?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==)")
    with right_column:
        st.image(log_resized)


with st.container():
    # inster a divider
    st.write("---")
    #insert the left column and right column
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        #to add on some space 
        # st.write("#")
        st.write("Provide media servides for real estates(still images and cinematic RE listing Video)\n\n"
                 "**Services & Pricing;**\n\n"
                 "For still Images:\n\n"
                 "- 500sq - 2500sq|25i +-| $175\n"
                 "- 2500sq - 4000sq | 30i +- | $237\n"
                 "- 4000sq - 5500sq | 40i +- | $299\n\n"
                 "For cinematic RE listing video:\n\n"
                 "- 500 sq - 2500sq | $197\n"
                 "- 2500sq - 4000sq | $269\n"
                 "- 4000sq - 5500sq | $315\n\n"
                 "Agent WalkThrough | $189 | $247 | $299\n\n"
                 "Social Media Highlight | $77\n\n"
                 "Twilight Images | $45/i\n\n"
                 "lifestyle Images | $10/i\n\n"
                 "Virtual Staging | $47/ Room\n\n"
                 "Pool/water Replacement | 39\n\n"
                 "Object Removal | $25\n\n"
                 " Green | $25\n\n")
                 
    with right_column:
        st.image(imag_resized)
        st.write("##")
        st.text("You will be charged $4.50/image for each additional image. Vice versa, you will be reimbursed $4.50/image, if you don't use or want the number of images given.")

#contact 
with st.container():
    st.write("---")
    st.header("Contact us;")
    st.write("##")

    contact_info = """<form action="https://formsubmit.co/seralens@outlook.com" method="POST">
     <input type= "hidden" name="_catcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_info, unsafe_allow_html=True)
with right_column:
    st.empty()
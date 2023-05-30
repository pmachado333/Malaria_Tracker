import streamlit as st
from PIL import Image


st.write("# Team Members")

patrick = Image.open('./image_dependencies/patrick.jpg')
col1, col2 = st.columns([1,4])
image_size = (100, 100)
with col1:
   st.header(" ")
   st.image(patrick.resize(image_size))

with col2:
   st.write("### **Patrick Pereira Machado**")
   st.write("Experienced Geoscientist/ Production Engineer with a demonstrated history of working in the oil & energy industry. Skilled in Python, C++, matlab, Software development, CFD, Flow Assurance and Petrophysics evaluation. Strong research professional with a Master focused in Chemical Engineering. . ")

kjetil = Image.open('./image_dependencies/kjetil.jfif')
col1, col2 = st.columns([1,4])
image_size = (100, 100)
with col1:
   st.header(" ")
   st.image(kjetil.resize(image_size))

with col2:
   st.write("### **Kjetil Westre**")
   st.write("I have a mixed background from G&G and data management, both techincal, sales -and business development . Topay I'm part of the innovation Factori team in Norway and working on digital projects. I'm super motivated to learn more in Data Science, which obvioulsy will be very benefical in my day to day work. This journey is super exciting and I'm honered to be given this opportunity to join the program. ")

mohamed = Image.open('./image_dependencies/mohamed.png')
col1, col2 = st.columns([1,4])
image_size = (100, 100)
with col1:
   st.header(" ")
   st.image(mohamed.resize(image_size))

with col2:
   st.write("### **Mohamed Nabeel Saif**")
   st.write("Aiming to add value in the oil and gas industry, and the energy industry in general, by applying the concepts of Data Analytics, Machine Learning and AI.")

xu = Image.open('./image_dependencies/xu.jfif')
col1, col2 = st.columns([1,4])
image_size = (100, 100)
with col1:
   st.header(" ")
   st.image(xu.resize(image_size))

with col2:
   st.write("### **Xu Zhang**")
   st.write("I'm from Beijing, China. Master in Geology domain. Borehole geologist in SLB since 2014. "
         "Good at borehole image data processing and interpretation, and Techlog software training. ")

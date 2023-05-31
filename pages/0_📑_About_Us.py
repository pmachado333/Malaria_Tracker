import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd
from PIL import Image

st.set_page_config(initial_sidebar_state='expanded', layout='wide')
#### Header Section ###
st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)
#st.sidebar.image('logo.jpg', width=80)


st.markdown('# The Team')
st.write(
'Malaria do not care about country borders - neither do the team. Together, we harness '
'the power of our global team to excel in innovation and deliver unique data science '
'projects. The interplay of our diverse background and experience fosters a dynamic environment that encourages '
'out-of-the-box thinking.')
st.write(
'The application of Data Science in Malaria detection empowers healthcare professionals and policymakers with '
'actionable insights, aiding in the efficient allocation of resources and targeted interventions. Ultimately, '
'our goal is to significantly reduce the number of Malaria-related casualties and minimize its impact on '
'public health at a global scale.')



#### World Map ###

image = Image.open("team1.jpg")
desired_width = 200
aspect_ratio = image.width / image.height
desired_height = int(desired_width / aspect_ratio)


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

pin_locations = [
    {"name": "Kjetil", "latitude": 58.969975, "longitude": 5.733107},
    {"name": "Xu", "latitude": 39.916668, "longitude": 116.383331},
    {"name": "Patrick", "latitude": -22.9008333, "longitude": -43.196388},
    {"name": "Mohamed", "latitude": 26.1460, "longitude": 50.3659},
]

pins = gpd.GeoDataFrame(pin_locations, geometry=gpd.points_from_xy(
    [pin["longitude"] for pin in pin_locations],
    [pin["latitude"] for pin in pin_locations]
))

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_axis_off()
world.plot(ax=ax, color='lightgrey')
pins.plot(ax=ax, marker='o', color='darkorange', markersize=50, edgecolor='darkorange', linewidth=1)

#label the pins
for x, y, label in zip(pins.geometry.x, pins.geometry.y, pins["name"]):
    ax.text(x, y, label, fontsize=9, ha='right', va='bottom')

plt.imshow(image, extent=[-180, 180, -90, 90], alpha=0.15, aspect='auto', zorder=3)
st.pyplot(fig)


#### Team  ###

patrick = Image.open("patrick.jpg")
xu = Image.open("xu.jpg")
kjetil = Image.open("kjetil.jpg")
mohamed = Image.open("mohamed.jpg")

image_size = (100, 100)
col1, col2 = st.columns([1,4])

with col1:
   st.header(" ")
   st.image(patrick.resize(image_size))
with col2:

    st.write('')
    st.write('')
    st.write('')
    st.write("<span style='color: blue;'>Patrick Pereira Machado</span>  - Experienced Geoscientist/ Production Engineer with a demonstrated history of working in "
            'the oil & energy industry. Skilled in Python, C++, matlab, Software development, CFD, '
            'Flow Assurance and Petrophysics evaluation. Strong research professional with a Master '
            'focused in Chemical Engineering.', unsafe_allow_html=True)
    st.write('')

with col1:
    st.header(" ")
    st.image(xu.resize(image_size))
with col2:

    st.write('')
    st.write('')
    st.write('')
    st.write("<span style='color: blue;'>Xu Zhang</span>  - Located in Beijing, China. Master in Geology domain. Borehole geologist in SLB since 2014. "
         'Good at borehole image data processing and interpretation, and Techlog software training.', unsafe_allow_html=True)

with col1:
    st.header(" ")
    st.image(kjetil.resize(image_size))
with col2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write("<span style='color: blue;'>Kjetil Westre</span> - Has a mixed background from G&G and data management, both technical,"
             ' sales -and business development . Today he is part of the Innovation Factori team in Norway, working on digital projects '
             'applying Data Science technologies. ', unsafe_allow_html=True)

with col1:
   st.header(" ")
   st.image(mohamed.resize(image_size))
with col2:
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write("<span style='color: blue;'>Mohamed Nabeel Saif</span>  - Aiming to add value in the oil and gas industry,"
            'and the energy industry in general, by applying the concepts of Data Analytics, Machine Learning and AI.',
            unsafe_allow_html=True)

#importing necessary libraries

import streamlit as st
import datetime
import pickle

# streamlit header
st.header('	:sponge: Copper Price Prediction')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

# Arranging widgets into 4 columns
col11, col12, col13, col14 = st.columns(4)

# defining min and max date for date input widget
min_date = datetime.datetime(2020,1,1)
max_date = datetime.date(2025,12,31)

# placing date input widget and extracting month and year from it
with col11:    
    a_date = st.date_input("Pick a date", min_value=min_date, max_value=max_date)
    
month=a_date.month
year=a_date.year  

# placing application widget
with col12:
    application = st.selectbox('Select application',list(range(1,100)))
 
# placing country widget
with col13:
    country= st.selectbox('Select country', [25,26,27,28,30,32,38,39,40,77,78,79,80,84,113])

#placing item_type widget
with col14:
    item_type = st.selectbox('Select item type',['IPL','Others','PL','S','SLAWR','W','WI'])
 
# defining 3 columns to arrange widgets
col21,col22,col23=st.columns(3)

# placing quantity in tons
with col21:
    quantity=st.number_input('Quantity in tons (0.01 to 5000)', min_value=0.01, max_value=5000.0)

#placing thickness widget    
with col22:
    thickness=st.number_input('Thickness (0.1 to 30)',min_value=0.1, max_value=30.0)
 
#placing width widget
with col23:
    width=st.number_input('Width (20 to 3000',min_value=20, max_value=3000)
    

# defining a list which will be updated with entered values and passed into model
x_test=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# updating the list with entered values
x_test[0]=quantity
x_test[1]=country
x_test[2]=application
x_test[3]=thickness
x_test[4]=width
x_test[5]=year
x_test[6]=month

# updating the last 7 Booleans in the list as per the item_type selected
if item_type=='IPL':
    x_test[7]=1
elif item_type=='Others':
    x_test[8]=1
elif item_type=='PL':
    x_test[9]=1
elif item_type=='S':
    x_test[10]=1
elif item_type=='SLAWR':
    x_test[11]=1
elif item_type=='W':
    x_test[12]=1
elif item_type=='WI':
    x_test[13]=1

# drawing a divider and defining a button
st.divider()
button=st.button('Submit')

if button==True:
    
# loading the pickle regressor model
    with open('C:\\Users\\Admin\\Documents\\Project_copper\\regressor','rb') as f:
        model_regressor=pickle.load(f)
        
# predicting value with the model
    y_pred=model_regressor.predict([x_test])

# displaying the result
    st.subheader(f'The predicted price is {round(y_pred[0],2)}')

# loading the pickle classifier
    with open('C:\\Users\\Admin\\Documents\\Project_copper\\classifier','rb') as f:
        model_classifier=pickle.load(f)
        
# predicting value with the model
    y_pred=model_classifier.predict([x_test])

# changing back binary to categorical    
    if y_pred==1:
        status='Win'
    else:
        status='Lose'

# displaying the result
    st.subheader(f'And the predicted status is "{status}"')
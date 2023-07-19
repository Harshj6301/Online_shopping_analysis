import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Ecommerce Data Analysis")

DATA_PATH = ("assets/Retail.OrderHistory.Clean.csv")

def load_data(nrows=None):
  data = pd.read_csv(DATA_PATH,nrows=nrows,encoding='utf8',encoding_errors='ignore')
  data.drop(columns=['Purchase Order Number','Gift Message','Gift Sender Name','Gift Recipient Contact Details','Unnamed: 19'],inplace=True)
  data['Ship Date'] = pd.to_datetime(data['Ship Date'])
  data['Order Date'] = pd.to_datetime(data['Order Date'])
  return data
data = load_data()
def feature_cleaner(feature_list,dataset):
    """The function replaces ','(comma) and '''(quote) in the entries and later converts all records into float64 """
    for feature in feature_list:
        dataset[feature] = dataset[feature].str.replace(',','')
        dataset[feature] = dataset[feature].str.replace("'",'')
   # print('Data cleaned..\nConverting to numeric type')
    dataset[features_to_float] = dataset[features_to_float].astype('float64')
    return dataset[features_to_float]
  
features_to_float = ['Unit Price','Unit Price Tax','Total Discounts','Total Owed','Shipment Item Subtotal','Shipment Item Subtotal Tax']
data = feature_cleaner(feature_list=features_to_float,dataset=data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Pie chart')
fig1 = px.pie(data_frame=data[:10],values='Price',hover_data=['Product Name'],names='shorted_names',hole=0.5)
st.plotly_chart(fig1, theme='streamlit', use_container_width=True)

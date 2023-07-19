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
data1 = feature_cleaner(feature_list=features_to_float,dataset=data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Pie chart for Top 10 prodcuts')
fig1 = px.pie(data_frame=data[:10],values='Unit Price',hole=0.5, hover_data=['Product Name'])
st.plotly_chart(fig1, theme='streamlit', use_container_width=True)

st.subheader('Pie chart for Last 20 prodcuts')
fig2 = px.pie(data_frame=data[:19],values='Unit Price',hole=0.5,hover_data=['Product Name'])
st.plotly_chart(fig2, theme='streamlit', use_container_width = True)

st.subheader('Orders over time')
fig3 = px.line(x='Order Date', y='Total Owed',data_frame=data,
       title='Orders through the time',hover_data=['Product Name'],labels={'Total Owed':'Price'},color='Quantity',line_dash_sequence=['dot'],markers=True)
st.plotly_chart(fig3, theme='streamlit', use_container_width = True)

st.subheader('Tax of the products')
c = ['Unit Price Tax','Unit Price']
fig4 = px.bar(data_frame=data,y='Unit Price',hover_data=['Unit Price Tax','Unit Price'],x='Product Name',opacity=0.7,color='Unit Price Tax',
       title='Products with their Price and Tax')
st.plotly_chart(fig4, theme='streamlit', use_container_width = True)

fig5 = px.scatter(data_frame=data, x='Order Date', y='Total Owed', color='Total Owed',
           labels={'Total Owed': 'Price'},hover_data=['Product Name'],size='Quantity')
st.plotly_chart(fig5, theme='streamlit', use_container_width = True)

st.subheader('A 3d chart for more interactivity')
fig6 = px.scatter_3d(data_frame=data, x='Order Date', z='Total Owed',y='Quantity',hover_data=['Product Name'],
                     labels={'Total Owed':'Price'},color='Quantity',width=800,height=750)
st.plotly_chart(fig6, theme='streamlit', use_container_width = True)

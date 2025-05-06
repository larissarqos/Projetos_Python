import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('Machine Learning App')

st.info('Esse aplicativo construiu um modelo de machine learning!')

# Exibindo dados
with st.expander('Dados'):
  st.write('**Dados Brutos**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

# Todos os dados, com exceção da variável target (variáveis preditoras)
with st.expander('X'):
  st.write('**Variáveis Preditoras**')
  X = df.drop('species', axis=1)
  X

# Variável target
with st.expander('y'):
  st.write('**Variável Target**')
  y = df.species
  y

# Criando gráfico
with st.expander('Visualização dos dados'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Preparando dados
with st.sidebar:
  st.header('Insira informações')
  island = st.selectbox('Ilha', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gênero', ('male', 'female'))
  # em bill_length_mm estão os valores máximo, mínimo e médio
  bill_length_mm = st.slider('Comprimento do Bico (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))


  




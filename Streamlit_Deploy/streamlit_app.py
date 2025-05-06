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






import streamlit as st
import numpy as np

def riskPred():
    mipi = st.number_input('MIPI risk category at dignosis (LOW,INTERMED, HIGH)')
    st.write('Your MIPI risk category is ', mipi)
    
    ki67 = st.number_input('Ki67 at diagnosis >= 30 (Yes, No)')
    st.write('Your Ki67 at diagnosis >= 30 is ', ki67)

    blas = st.number_input('Blastoid/pleomorphic at diagnosis (Yes, No)')
    st.write('Your Blastoid/pleomorphic at diagnosis is ', blas)
    
    tobtki = st.number_input('Time to 2L BTKi (months)')
    st.write('Your Time to 2L BTKi (months) is ', tobtki)

riskPred()

## (base) lcrmac02:~ aijiang$ cd Desktop
## (base) lcrmac02:Desktop aijiang$ cd AJworking/NovDec2022/Diego_NovDec2022
## to run the file (assume I am in the correct folder): python -m streamlit run python_try_risk.py
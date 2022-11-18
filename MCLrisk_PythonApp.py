import streamlit as st
import numpy as np
import math

def riskPred():

    st.subheader("Estimated 2-year PFS2 with 2L BTKi in R/R MCL") 
    
    mipi = st.selectbox('MIPI risk category at dignosis', ('LOW','INTERMED', 'HIGH'))
    ki67 = st.selectbox('Ki67 at diagnosis >= 30', ('Yes', 'No'))
    blas = st.selectbox('Blastoid/pleomorphic at diagnosis', ('Yes', 'No'))
    tobtki = st.number_input('Time to 2L BTKi (months)')
    
    ### data transformation
    mipi_m = 0
    mipi_h = 0
    if mipi == 'INTERMED':
      mipi_m = 1
    elif mipi == "HIGH":
      mipi_h = 1
    
    blasy = 0
    if blas == "Yes":
      blasy = 1
    
    ki67y = 0
    if ki67 == "Yes":
      ki67y = 1
   
    ## model with spline
    sres = 0.5261312+0.17477834*mipi_m + 0.24310161*mipi_h+0.12879252*blasy+0.59915019*ki67y-0.068082474*tobtki+4.7572897e-05*max(tobtki-2,0)**3-7.4391067e-05*max(tobtki-14,0)**3+2.6606845e-05*max(tobtki-34.95,0)**3+ 2.113245e-07*max(tobtki-77.7,0)**3 
    ## cumhaz at 2 years was calcualted from rms R package
    haz2 = 0.9456698
   
    sprob = math.exp(-haz2*math.exp(sres)) 

    if st.button('Calculate'):
      st.text("")
      st.write("Your spline model score is ", round(sres,3)) ## remove later, but show it for now
      st.write("Your 2 years PFS probability based on spline model is ", round(sprob, 3))
      
riskPred()

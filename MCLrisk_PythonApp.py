
import streamlit as st
import numpy as np
import math

def riskPred():

    st.subheader("Estimated 2-year PFS2 with 2L BTKi in R/R MCL")  
    
    mipi = st.selectbox('MIPI risk category at diagnosis', ('LOW','INTERMEDIATE', 'HIGH'))
    ki67 = st.selectbox('Ki67 at diagnosis', ('>=30%', '<30%'))
    blas = st.selectbox('Blastoid/pleomorphic at diagnosis', ('Yes', 'No'))
    tobtki = st.number_input('Time to 2L BTKi (months)')
    
    ### data transformation
    mipi_m = 0
    mipi_h = 0
    if mipi == 'INTERMEDIATE':
      mipi_m = 1
    elif mipi == "HIGH":
      mipi_h = 1
    
    blasy = 0
    if blas == "Yes":
      blasy = 1
    
    ki67y = 0
    if ki67 == ">=30%":
      ki67y = 1
   
    ## models with spline
    sres = 0.5261312+0.17477834*mipi_m + 0.24310161*mipi_h+0.12879252*blasy+0.59915019*ki67y-0.068082474*tobtki+4.7572897e-05*(max(tobtki-2,0)**3)-7.4391067e-05*(max(tobtki-14,0)**3)+2.6606845e-05*(max(tobtki-34.95,0)**3)+ 2.113245e-07*(max(tobtki-77.7,0)**3) 
    haz2 = 0.91930212  
    sprob = math.exp(-haz2*math.exp(sres))  
    riskgr = "intermediate"
    if sprob <= 0.3:
      riskgr = "high"
    elif sprob >= 0.6:
        riskgr = "low"
      
    ores = 0.21199219+0.045028918*mipi_m+0.83757694*mipi_h +0.28606937*blasy+0.33543194*ki67y-0.044884898*tobtki+4.1977467e-05*(max(tobtki-2,0)**3)-7.9279546e-05*(max(tobtki-14,0)**3)+4.379913e-05*(max(tobtki-34.95,0)**3)-6.4970514e-06*(max(tobtki-77.7,0)**3) 
    ohaz2 = 0.374791572 
    oprob = math.exp(-ohaz2*math.exp(ores))
    
    if st.button('Calculate'):
      st.text("")
      out = str(round(sprob*100,2)) + "%"
      st.write("The 2 year PFS2 probability based on spline model is ", out, ".")
      st.write("The risk level is " + riskgr + ".")  
      oout = str(round(oprob*100,2)) + "%"
      st.text("")
      st.write("The 2 year OS2 probability based on spline model is ", oout, ".")

riskPred()









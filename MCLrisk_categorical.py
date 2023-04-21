import streamlit as st
import numpy as np
import math

def riskPred():

    st.subheader("Estimated 2-year PFS2 with 2L BTKi in R/R MCL")  
    
    pod = st.selectbox('POD categories', ('POD>24','POD6-24', 'POD6'))
    ki67 = st.selectbox('Ki67 at diagnosis', ('>=30%', '<30%'))
    mipi = st.selectbox('MIPI at diagnosis', ('LOW','INTERMEDIATE', 'HIGH'))
      
   
    ### data transformation
    pod6 = 0
    pod6to24 = 0
    if pod == "POD6":
        pod6 = 1
    elif pod == "POD6-24":
        pod6to24 = 1

    ki67y = 0
    if ki67 == ">=30%":
        ki67y = 1

    mipi_ih = 1
    if mipi == 'LOW':
        mipi_ih = 0
   
    ## models 
    sres  = -0.82432193+0.78561281*pod6to24+1.5738312*pod6+0.3843381*ki67y+0.1664444*mipi_ih
    haz2 = 1.08297747132296
    sprob = math.exp(-haz2*math.exp(sres))  
    riskgr = "intermediate"
    if sprob <= 0.3:
        riskgr = "high"
    elif sprob >= 0.6:
        riskgr = "low"
      
    ores = -0.75143452+1.0572744*pod6to24+1.657246*pod6+0.35761732*ki67y-0.06961106*mipi_ih
    ohaz2 = 0.516876764860384
    oprob = math.exp(-ohaz2*math.exp(ores))
    
    if st.button('Calculate'):
      st.text("")
      out = str(round(sprob*100,2)) + "%"
      st.write("The 2 year PFS2 probability is ", out, ".")
      st.write("The risk level is " + riskgr + ".")  
      oout = str(round(oprob*100,2)) + "%"
      st.text("")
      st.write("The 2 year OS2 probability is ", oout, ".")

riskPred()


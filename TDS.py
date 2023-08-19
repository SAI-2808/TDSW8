import streamlit as st
st.title('Greatest of three number')
n1=st.number_input("Enter n1:")
n2=st.number_input("Enter n2:")
n3=st.number_input("Enter n3:")
result=max(n1,n2,n3)
st.write("Maximum among the theree is:",result)

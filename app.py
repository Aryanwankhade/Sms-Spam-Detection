import streamlit as st
import pickle
model = pickle.load(open("model.pkl", 'rb'))
cv=pickle.load(open("vectorizer.pkl", 'rb'))
st.title('SmS Spam classifier')
st.markdown('Made By Aryan Wankhade')
st.write("This is a machine learning model to detect whether a message is spam or not")
user_input=st.text_area("Enter or Paste the message",height =100)
if st.button("classify") :
    if user_input:
        data=[user_input]
        vectorized=cv.transform(data).toarray()
        result=model.predict(vectorized)
        if result[0]==1:
            st.write("spam message")
        else:
            st.write("not a spam message")
    else:
        st.write("Please Enter a message to classify")
st.write("Thank you")
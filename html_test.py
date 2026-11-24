import streamlit as st

st.set_page_config(page_title="HTML Test")

st.markdown("""
<style>
.test-box {
    background: linear-gradient(120deg, #51418F, #A091DB);
    padding: 40px;
    border-radius: 20px;
    color: white;
}
.test-box h1 {
    color: white;
    font-size: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="test-box">
    <h1>FRAME THE DATA.</h1>
    <p>This HTML should appear as a purple card, not raw HTML text.</p>
</div>
""", unsafe_allow_html=True)

st.success("HTML rendering test completed.")
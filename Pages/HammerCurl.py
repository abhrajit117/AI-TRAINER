import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="AI Trainer",
    page_icon="💪",
)
# import streamlit.components.v1 as components
st.markdown(
    """
    <a href="http://localhost:8501/" >
        <button style=" background-color: green;
    border: 4px solid green;
    border-radius: 10px;
    color: #bcff96;
    box-shadow: 10px;
    padding: 10px 20px ; cursor: pointer;">
            Go to Home
        </button>
    </a>
""",
    unsafe_allow_html=True,
)


st.write(
    """
# Hammer Curl Exercise AI Traier�💪
"""
)
# st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# variable1 = "Start Exercise"
# variable2 = "End Exercise"
# def handleClick():
#     st.write("""Video on""")
# variable = "End Exercise"
# click = st.button(variable1, on_click=handleClick)
# if click == True:
#     variable = "End Exercise"
#     st.write("video started running")
# df = pd.DataFrame(np.random.randn(10, 2), columns=["col1", "col2"])
# data1 = df.to_csv().encode("utf-8")
# st.download_button(
#     label="Download file", data=data1, file_name="newfile.csv", mime="text/csv"
# )

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
placeholder.empty()

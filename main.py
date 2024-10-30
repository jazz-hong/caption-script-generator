import streamlit as st
from utils import generate_caption


st.header("CAPTION GENERATOR 爆款社交媒体助手 ✏️")
# with st.sidebar:
#     openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
#     st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

theme = st.text_input("TITLE 主题 ")
submit = st.button("GET IT NOW 开始写作 ")

# if submit and not openai_api_key:
#     st.info("请输入你的OpenAI API密钥")
#     st.stop()
if submit and not theme:
    st.info("PLEASE ENTER YOUR SUBJECT 请输入生成内容的主题")
    st.stop()
if submit:
    # with st.spinner("AI正在努力创作中，请稍等..."):
    #     result = generate_caption(theme)
    # st.divider()
    # left_column, right_column = st.columns(2)
    # with left_column:
    #     # st.markdown("##### 小红书标题")
    #     # st.write(result.titles[0])
    #     # st.markdown("##### 小红书标题2")
    #     # st.write(result.title[1])
    #     # st.markdown("##### 小红书标题3")
    #     # st.write(result.title[2])
    #     # st.markdown("##### 小红书标题4")
    #     # st.write(result.title[3])
    #     # st.markdown("##### 小红书标题5")
    #     # st.write(result.title[4])
    # with right_column:
    #     st.markdown("##### 小红书正文")
    #     st.write(result.content)

    with st.spinner("AI is Thinking... 正在努力创作中，请稍等..."):
        result = generate_caption(theme)
        st.markdown("##### YOUR CAPTION TITLE! 你的标题已出炉!")
        st.write(result)

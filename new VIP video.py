import streamlit as st
import webbrowser

# 页面配置
st.set_page_config(page_title="VIP追剧神器", page_icon="🎬", layout="centered")

# 标题
st.title("🎬 VIP追剧神器")
st.markdown("---")

# 输入框
video_url = st.text_input("输入视频网址：", placeholder="请粘贴爱奇艺/腾讯/优酷等视频链接")

# 按钮区
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("爱奇艺", use_container_width=True):
        webbrowser.open("https://www.iqiyi.com")

with col2:
    if st.button("腾讯视频", use_container_width=True):
        webbrowser.open("https://v.qq.com")

with col3:
    if st.button("优酷视频", use_container_width=True):
        webbrowser.open("https://www.youku.com/")

with col4:
    if st.button("播放VIP视频", type="primary", use_container_width=True):
        if video_url:
            webbrowser.open(f"https://jx.xmflv.com/?url={video_url}")
        else:
            st.warning("⚠️ 请先输入视频网址！")

# 清空按钮
if st.button("清空输入框", use_container_width=True):
    st.experimental_rerun()  # 刷新页面清空输入

# 提示语
st.markdown("---")
st.warning("⚠️ 提示：本案例仅供学习使用，不可作为他用。")
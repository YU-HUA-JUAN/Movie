import streamlit as st

# 页面配置
st.set_page_config(page_title="VIP追剧神器", page_icon="🎬", layout="centered")

# 标题
st.title("🎬 VIP追剧神器")
st.markdown("---")

# 输入框
video_url = st.text_input("输入视频网址：", placeholder="请粘贴爱奇艺/腾讯/优酷等视频链接")

# 按钮区（用 Streamlit 原生按钮 + 前端跳转方案）
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("爱奇艺", use_container_width=True):
        # 生成前端跳转链接，自动点击
        st.markdown('<meta http-equiv="refresh" content="0; url=https://www.iqiyi.com" />', unsafe_allow_html=True)

with col2:
    if st.button("腾讯视频", use_container_width=True):
        st.markdown('<meta http-equiv="refresh" content="0; url=https://v.qq.com" />', unsafe_allow_html=True)

with col3:
    if st.button("优酷视频", use_container_width=True):
        st.markdown('<meta http-equiv="refresh" content="0; url=https://www.youku.com/" />', unsafe_allow_html=True)

with col4:
    if st.button("播放VIP视频", type="primary", use_container_width=True):
        if video_url:
            # 拼接解析链接，自动跳转
            parse_url = f"https://jx.xmflv.com/?url={video_url}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={parse_url}" />', unsafe_allow_html=True)
        else:
            st.warning("⚠️ 请先输入视频网址！")

# 清空按钮
if st.button("清空输入框", use_container_width=True):
    st.rerun()  # 刷新页面清空输入（新API，无警告）

# 提示语
st.markdown("---")
st.warning("⚠️ 提示：本案例仅供学习使用，不可作为他用。")
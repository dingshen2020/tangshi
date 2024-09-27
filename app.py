import streamlit as st
from PIL import Image, ImageDraw

def generate_image(poem):
    # 这里可以替换为实际的图像生成逻辑
    img = Image.new('RGB', (400, 200), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 10), poem, fill=(0, 0, 0))
    return img

st.title("唐诗生成图像")

# 更显眼的输入框
st.markdown("<h3 style='color: blue;'>请输入唐诗：</h3>", unsafe_allow_html=True)
user_input = st.text_area("", height=150)  # 增加输入框高度

if st.button("生成图像"):
    if user_input:
        img = generate_image(user_input)
        st.image(img, caption='生成的图像', use_column_width=True)
    else:
        st.warning("请先输入唐诗。")

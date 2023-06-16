import streamlit as st

st.title("나의 파이썬 웹페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠?")
st.write("가자고 취업해야지")
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")  # 유튜브 링크
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
st.image("https://i.imgur.com/jorp5JH.png")  # 인터넷 링크
st.image("data:image/jpeg;base64,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", use_column_width=True)
st.image("data:image/jpeg;base64,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", width=100)

#제목 마크다운
st.write("""
# 가장 큰 제목 텍스트 h1 : st.title
## 그다음 h2 : st.header
### 그다다음 일반적으로 여기까지 씁니다 h3 : st.subheader
#### 그그다다음 h4
##### 언제까지 작아지려나 h5
###### 과연? h6
####### 띠용 h7은 없어
""")


#서식
text = """
기울임 *별표*나 _언더바_ 요렇게 하나씩 주면 기울임

진하게 **별표** 를 두개

둘다는 ***별표*** 세개

취소선은 ~물결표~

줄바꿈은 엔터 두번

------------여기까지 st.write(text)-----------------

밑줄 : <u>밑줄</u> 마크다운, 태그 허용 옵션 적용

형광펜 : <mark>형광펜</mark>
"""
# st.write(text)
# 태그를 허용하는 옵션
st.markdown(text, unsafe_allow_html=True)

#레이아웃
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 탭 누르고 들여쓰기
            * 탭 누르고 들여쓰기
    - 대쉬도 똑같아
    - 대쉬도 똑같아
    - 대쉬도 똑같아
    
    #### 순서가 있는 리스트
    
    1. 순서가
    2. 있는
    3. 리스트
    1. 1을 넣어도
    1. 증가되어
    1. 나간다
    
""")
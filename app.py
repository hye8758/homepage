import streamlit as st

def get_conversation_chain(_db, _model, user_question, _press_release_info):
    # Search the DB.
    #st.write(user_question)

    qestion_first = user_question.strip()[0]
    if qestion_first == '@':
        st.write("@표시에 따라 학생이라 가정하고 답변드리겠습니다.")
        
    elif qestion_first == '#':
        st.write("#표시에 따라 보도자료가 아닌 일반적인 내용을 토대로 답변드리겠습니다.")
        
    else :
        st.write("보도자료가 아닌 일반적인 내용을 토대로 답변을 원하시면 질문 앞에 #를 붙여주세요.")
          
def start(_db, _model, _press_release_info):
    #st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.write("저의 홈페이지에 오신것을 환영합니다.")
    
    user_question = st.text_input("질의사항 입력", placeholder="여기에 입력해 주세요(입력 후 엔터)")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    if user_question == None:
        st.write("아직 질문 내용이 없습니다")
    else:
        pass
        #st.write(user_question)
        
    if user_question:
        st.session_state.conversation = get_conversation_chain(_db, _model, user_question, _press_release_info)


if __name__ == "__main__": 
    _db = ""
    _model =""
    _press_release_info = ""
    start(_db, _model, _press_release_info)

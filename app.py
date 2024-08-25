from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

# Define a function to get the documentation from the LLM
def get_gemini_response(code_snippet):
    prompt = f"""You are an advanced AI language model capable of generating comprehensive and 
    accurate documentation for code snippets. Your task is to read a given code snippet and produce 
    detailed documentation, explaining the purpose, functionality, parameters, return values, and any 
    other relevant information.:\n\n{code_snippet}
    Follow these guidelines:
    Purpose: Describe what the code does.
    Functionality: Explain how the code works, including any important logic or algorithms used.
    Parameters: List and describe each parameter, including its type and purpose.
    Return Values: Detail what the code returns, including its type and purpose.
    Examples: Provide examples of how the code might be used, if applicable.
    Edge Cases: Mention any edge cases or potential errors and how the code handles them.
    """
    response = model.generate_content([prompt])
    return response.text

#######################################################################################################################
# Streamlit app layout
st.set_page_config(page_title="CodeDocAI", layout="wide")

st.title("CodeDocAI")
avs.add_vertical_space(1)

col1, col2 = st.columns([1, 3])  
with col1:
    img = Image.open("images/icon.png")
    st.image(img)
 
with col2:    
    st.header("Effortless Code Documentation at Your Fingertips")
    st.markdown("""<p style='text-align: justify;'>
                    Introducing CodeDocAI, an advanced project powered by a Large Language Model (LLM) that 
                    effortlessly generates comprehensive and accurate documentation from code snippets. Designed 
                    to simplify the documentation process, CodeDocAI provides developers with detailed explanations 
                    of their code, enhancing understanding and maintainability without the need for manual comments. 
                    Whether you are a software developer seeking high-quality documentation, a code reviewer aiming 
                    to quickly understand and improve code, or an educator helping students learn coding concepts, 
                    CodeDocAI offers robust solutions tailored to your needs. Experience seamless code documentation 
                    with CodeDocAI and transform the way you interact with your code.
                    </p>""", unsafe_allow_html=True)



col1, col2, col3 = st.columns([1, 2, 1])  
with col2:
    img1 = Image.open("images/icon1.png")
    st.image(img1, width = 400)
    
avs.add_vertical_space(8)

col1, col2 = st.columns([2, 3])

with col1:
    img2 = Image.open("images/icon2.png")
    st.image(img2)

with col2:
    st.header("Wide Range of Offerings")
    st.write("- Seamless documentation generation from code snippets")
    st.write("- Detailed explanations of code logic and functionality")
    st.write("- Enhanced understanding and maintainability of code")
    st.write("- No need for extensive manual comments")
    st.write("- Suitable for software development, code review, and educational purposes")
    st.write("- High-quality documentation effortlessly obtained")
    st.write("- Improved code readability and collaboration")
    st.write("- Time-saving for code reviewers")
    st.write("- Enhanced learning experience for students")
    st.write("- Intuitive and effective documentation process")



avs.add_vertical_space(8)


col1, col2 = st.columns([2, 1])
with col1: 
    st.header("Present Your Code Slice")
    st.subheader("- Explore code snippets effortlessly")
    st.subheader("- Simplify complex code comprehension")
    st.subheader("- Enhance code documentation in just a few clicks")

with col2: 
    img3 = Image.open("images/icon3.png")
    st.image(img3, width = 250)

code_snippet = st.text_area("Paste your code snippet here", height=300)

if st.button("Generate Documentation"):
    if code_snippet:
        with st.spinner("Generating documentation..."):
            documentation = get_gemini_response(code_snippet)
            st.subheader("Generated Documentation")
            st.write(documentation)
    else:
        st.error("Please enter a code snippet to generate documentation.")


avs.add_vertical_space(8)


col1, col2 = st.columns([2, 3])

with col1:
    avs.add_vertical_space(5)
    img4 = Image.open("images/icon4.png")
    st.image(img4, use_column_width=True)

with col2:
    st.write("Q: What is CodeDocAI?")
    st.write("""A: CodeDocAI is an advanced project powered by a Large Language Model (LLM) 
             designed to generate comprehensive documentation from code snippets automatically.""")
    avs.add_vertical_space(3)
    st.write("Q: How does CodeDocAI simplify the documentation process?")
    st.write("""A: CodeDocAI allows developers to obtain detailed explanations of their code 
             without needing to write extensive comments manually, thereby enhancing understanding 
             and maintainability.""")
    avs.add_vertical_space(3)
    st.write("Q: In what scenarios can CodeDocAI be used?")
    st.write("""A: CodeDocAI can be utilized across various scenarios, including software development, 
             code review, and educational purposes.""")






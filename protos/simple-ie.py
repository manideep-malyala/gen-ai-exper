import streamlit as st
import os

# Function to get the list of directories containing prompt files
def get_prompt_directories():
    return [d for d in os.listdir() if os.path.isdir(d)]

# Function to get the list of prompt files in the selected directory
def get_prompt_files(prompt_dir):
    return [f for f in os.listdir(prompt_dir) if f.endswith('.txt')]

def get_response(prompt, input_data):
    # Simulated response based on the prompt and input data
    return f"Response to your prompt: {prompt}\n\nWith input data: {input_data}"

def main():
    st.title("Inference Engine")
    st.divider()

    # Initialize session state variables
    if 'prompt_text' not in st.session_state:
        st.session_state['prompt_text'] = ""
    if 'input_text' not in st.session_state:
        st.session_state['input_text'] = ""
    if 'response' not in st.session_state:
        st.session_state['response'] = ""

    # Row 1: Prompt Selection
    st.subheader("1. PROMPT")
    load_prompt = st.toggle("Load prompt from directory")
    
    if load_prompt:
        prompt_dirs = get_prompt_directories()
        selected_prompt_dir = st.selectbox("Choose a prompt directory", prompt_dirs)
        
        if selected_prompt_dir:
            prompt_files = get_prompt_files(selected_prompt_dir)
            selected_prompt_file = st.selectbox("Choose a prompt file", prompt_files)
            
            if selected_prompt_file:
                with open(os.path.join(selected_prompt_dir, selected_prompt_file), 'r') as file:
                    prompt_content = file.read()
                st.session_state['prompt_text'] = st.text_area("Prompt", prompt_content, height=150)
            else:
                st.session_state['prompt_text'] = st.text_area("Prompt", height=150)
        else:
            st.session_state['prompt_text'] = st.text_area("Prompt", height=150)
    else:
        st.session_state['prompt_text'] = st.text_area("Prompt", height=150)
    
    st.divider()

    # Row 2: Input Data
    st.subheader("2. DATA")
    
    use_file_input = st.toggle("Use file upload for input data")
    
    if use_file_input:
        uploaded_file = st.file_uploader("Upload a file (optional)", type=["txt", "csv"])
        
        if uploaded_file is not None:
            st.session_state['input_text'] = uploaded_file.read().decode("utf-8")
            st.text_area("Input Data", st.session_state['input_text'], height=150)
    else:
        st.session_state['input_text'] = st.text_area("Enter your input data", height=150)
    
    st.divider()

    # Row 3: Generate Response
    st.subheader("3. RESPONSE")
    if st.button("Generate Response"):
        st.session_state['response'] = get_response(st.session_state['prompt_text'], st.session_state['input_text'])

    # Display the response from session state
    if st.session_state['response']:
        response_text_area = st.text_area("Response", st.session_state['response'], height=150)

        # Provide a download button for the response
        st.download_button(
            label="Download Response",
            data=st.session_state['response'],
            file_name="response.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()

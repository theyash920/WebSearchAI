import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    """

    ##Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: failed to laod user input from the ui")
        return
    
    user_message = st.chat_input("Enter your message:")

    #if user_message:
    #    try:
            #load groq llm 
        #    obj_llm_config = GroqLLM(user_controls_input = user_input)
        #    model = obj_llm_config.get_llm_model()

          #  if not model:
          #      st.error("Error: llm model could not be initialized.")
        #        return

            #initialize and set up the graph absed on use case
          #  usecase = user_input.get("selected_usecase")
          # if not usecase:
          #    st.error("Error:No usecase selected.")
          #    return
            
    
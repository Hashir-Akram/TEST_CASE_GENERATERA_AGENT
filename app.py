import streamlit as st

from agents.test_generation_agent import (
    TestGenerationAgent
)

from tools.file_writer import save_test_file


st.set_page_config(
    page_title="AI QA Agent",
    layout="wide"
)

st.title("AI-Powered QA Test Generation Agent")

st.markdown(
    "Generate pytest + Selenium automation scripts using AI."
)

# User Input
requirement = st.text_area(
    "Enter Testing Requirement",
    height=250,
    placeholder="""
Example:

Test login functionality.

Test Cases:
- Valid login
- Invalid login
- Empty credentials
- Verify dashboard redirection
"""
)

# Generate Button
if st.button("Generate Automation Test"):

    if requirement.strip():

        with st.spinner("AI Agent Generating Test Cases..."):

            # Initialize Agent
            agent = TestGenerationAgent()

            # Generate Test
            generated_test = agent.generate_test(
                requirement
            )

            # Display Output
            st.subheader("Generated Automation Script")

            st.code(
                generated_test,
                language="python"
            )

            # Save File
            file_path = save_test_file(generated_test)

            st.success(
                f"Test saved successfully at: {file_path}"
            )

    else:

        st.warning(
            "Please enter a testing requirement."
        )
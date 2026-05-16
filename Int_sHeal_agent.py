import streamlit as st

from agents.flaky_analyzer_agent import (
    FlakyAnalyzerAgent
)

from agents.self_healing_agent import (
    SelfHealingAgent
)

from failures.sample_failure import (
    failed_locator,
    error_message
)

from ui_elements.sample_dom import (
    available_elements
)


st.set_page_config(
    page_title="AI Flaky Test Analyzer",
    layout="wide"
)

st.title(
    "AI-Powered Flaky Test & Self-Healing System"
)

st.markdown("""
This demo simulates:

- Flaky Selenium test analysis
- AI-powered root cause investigation
- Self-healing locator recommendation
""")

if st.button("Analyze Flaky Test"):

    # Initialize Agents
    flaky_agent = FlakyAnalyzerAgent()

    healing_agent = SelfHealingAgent()

    # Step 1: Analyze Failure
    with st.spinner(
        "AI Analyzing Selenium Failure..."
    ):

        flaky_analysis = (
            flaky_agent.analyze_failure(
                error_message
            )
        )

    st.subheader("Flaky Test Analysis")

    st.write(flaky_analysis)

    # Step 2: Heal Locator
    with st.spinner(
        "AI Recovering Locator..."
    ):

        healing_result = (
            healing_agent.heal_locator(
                failed_locator,
                available_elements
            )
        )

    st.subheader("Self-Healing Recommendation")

    st.write(healing_result)
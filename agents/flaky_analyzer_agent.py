from llm.llm_client import generate_response

from prompts.flaky_prompt import (
    build_flaky_prompt
)


class FlakyAnalyzerAgent:

    def __init__(self):

        self.agent_name = "AI Flaky Test Analyzer"

    def analyze_failure(self, error_details):

        print(
            f"\n[{self.agent_name}] "
            f"Investigating Test Failure...\n"
        )

        # Step 1: Create Prompt
        prompt = build_flaky_prompt(
            error_details
        )

        print("[INFO] Failure Prompt Created\n")

        # Step 2: Send To LLM
        llm_response = generate_response(prompt)

        print("[INFO] Failure Analysis Completed\n")

        return llm_response
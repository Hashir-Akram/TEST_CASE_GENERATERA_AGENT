from llm.llm_client import generate_response

from prompts.test_generation_prompt import (
    build_test_generation_prompt
)


class TestGenerationAgent:

    def __init__(self):

        self.agent_name = "AI QA Test Generation Agent"

    def generate_test(self, requirement):

        print(f"\n[{self.agent_name}] Processing Requirement...\n")

        # Step 1: Build Prompt
        prompt = build_test_generation_prompt(requirement)

        print("[INFO] Prompt Created Successfully\n")

        # Step 2: Send Prompt To LLM
        llm_response = generate_response(prompt)

        print("[INFO] Test Generated Successfully\n")

        return llm_response
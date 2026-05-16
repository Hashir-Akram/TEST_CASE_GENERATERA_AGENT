from llm.llm_client import generate_response

from prompts.healing_prompt import (
    build_healing_prompt
)


class SelfHealingAgent:

    def __init__(self):

        self.agent_name = "AI Self-Healing Agent"

    def heal_locator(
        self,
        failed_locator,
        available_elements
    ):

        print(
            f"\n[{self.agent_name}] "
            f"Analyzing Failed Locator...\n"
        )

        # Step 1: Build Prompt
        prompt = build_healing_prompt(
            failed_locator,
            available_elements
        )

        print("[INFO] Healing Prompt Created\n")

        # Step 2: Send To LLM
        llm_response = generate_response(prompt)

        print("[INFO] Locator Recovery Completed\n")

        return llm_response
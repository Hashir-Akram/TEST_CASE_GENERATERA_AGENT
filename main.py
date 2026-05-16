from agents.test_generation_agent import (
    TestGenerationAgent
)

from tools.file_writer import save_test_file


def main():

    requirement = """
    Test the signup page functionality.

    Test Cases:
    - Valid signup
    - Invalid signup
    - Empty username/password
    - Verify dashboard redirection after signup
    """

    # Initialize Agent
    agent = TestGenerationAgent()

    # Generate Test
    generated_test = agent.generate_test(requirement)

    print("\n========== GENERATED TEST ==========\n")

    print(generated_test)

    # Save Generated Test
    file_path = save_test_file(generated_test)

    print(f"\n[INFO] Test Saved At: {file_path}")


if __name__ == "__main__":

    main()
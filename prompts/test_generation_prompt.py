def build_test_generation_prompt(requirement):

    prompt = f"""
You are an expert QA Automation Engineer.

Your task is to generate:

1. Test scenarios
2. pytest Selenium automation script
3. Assertions

Application Feature:
{requirement}

Instructions:
- Use pytest
- Use Selenium
- Use proper assertions
- Follow Page Object Model principles
- Add comments in code
- Generate clean and readable automation code
"""

    return prompt
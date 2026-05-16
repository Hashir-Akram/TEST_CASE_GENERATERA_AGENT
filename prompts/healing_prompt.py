def build_healing_prompt(
    failed_locator,
    available_elements
):

    prompt = f"""
You are an expert QA Automation Engineer.

A Selenium locator has failed.

Failed Locator:
{failed_locator}

Available Elements On Page:
{available_elements}

Your task:
1. Identify the most likely replacement locator
2. Explain why it matches
3. Suggest better locator strategy
4. Provide Selenium locator recommendation

Return clear bullet-point response.
"""

    return prompt
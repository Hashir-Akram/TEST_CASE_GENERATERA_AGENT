def build_flaky_prompt(error_details):

    prompt = f"""
You are an expert QA Automation Engineer 
specialized in Selenium, pytest, 
and flaky UI test analysis.

Analyze the following Selenium test failure.

Your tasks:
1. Identify the possible flaky test reason
2. Explain the probable root cause
3. Suggest recommended fixes
4. Mention whether retrying the test may help
5. Suggest best practices to avoid similar flaky tests

Failure Details:
{error_details}

Instructions:
- Keep explanation simple and clear
- Focus on UI automation failures
- Provide practical recommendations
- Use bullet points
"""

    return prompt
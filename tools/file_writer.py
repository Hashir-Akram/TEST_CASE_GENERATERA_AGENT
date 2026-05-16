import os


def save_test_file(content, filename="test_signup.py"):

    output_folder = "generated_tests"

    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, filename)

    with open(file_path, "w", encoding="utf-8") as file:

        file.write(content)

    return file_path
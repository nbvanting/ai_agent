from functions.get_file_content import get_file_content

def run_tests():
    print("Running tests for get_file_content...\n")

    print("Test 1: main.py")
    print(get_file_content("calculator", "main.py"))

    print("Test 2: pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("Test 3: /bin/cat/")
    print(get_file_content("calculator", "/bin/cat/"))

if __name__ == "__main__":
    run_tests()
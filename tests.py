from functions.get_files_info import get_files_info

def run_tests():
    print("Test 1: get_files_info('calculator', '.')")
    result = get_files_info("calculator", ".")
    print(result)
    print()

    print("Test 2: get_files_info('calculator', 'pkg')")
    result = get_files_info("calculator", "pkg")
    print(result)
    print()

    print("Test 3: get_files_info('calculator', '/bin')")
    result = get_files_info("calculator", "/bin")
    print(result)
    print()

    print("Test 4: get_files_info('calculator', '../')")
    result = get_files_info("calculator", "../")
    print(result)
    print()

if __name__ == "__main__":
    run_tests()
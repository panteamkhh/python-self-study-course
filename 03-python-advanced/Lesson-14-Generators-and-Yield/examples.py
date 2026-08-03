"""
Lesson 14 - Generators and Yield
All three examples from lesson.md, ready to run as-is.
"""


# --- Example 1: A Simple Number Generator -----------------------------------

def simple_numbers():
    yield 1
    yield 2
    yield 3


# --- Example 2: Generating an Infinite Sequence (with a Limit) -------------

def even_numbers():
    n = 0
    while True:
        yield n
        n += 2


# --- Example 3: Reading a Large File Line by Line (simulated) --------------

def read_important_lines(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()


def main():
    print("--- Example 1 ---")
    for num in simple_numbers():
        print(num)

    print("\n--- Example 2 ---")
    gen = even_numbers()
    for _ in range(5):
        print(next(gen))

    print("\n--- Example 3 ---")
    log_lines = [
        "INFO: server started",
        "ERROR: disk full",
        "INFO: request handled",
        "ERROR: connection lost",
    ]
    for important_line in read_important_lines(log_lines):
        print(important_line)


if __name__ == "__main__":
    main()

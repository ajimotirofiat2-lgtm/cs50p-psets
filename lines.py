import sys


def get_filename():
    """Validate command-line arguments."""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    return sys.argv[1]


def is_code(line):
    """True if the line is neither blank nor a comment."""
    stripped = line.lstrip()
    return stripped != "" and not stripped.startswith("#")


def count_lines(filename):
    try:
        with open(filename) as file:
            return sum(1 for line in file if is_code(line))
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    print(count_lines(get_filename()))


if __name__ == "__main__":
    main()

def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data


def validate_asc(line: str) -> bool:
    l = list(map(int, line.split()))
    s = sorted(l)
    return l == s


def validate_desc(line: str) -> bool:
    l = list(map(int, line.split()))
    s = sorted(l, reverse=True)
    return l == s


def validate_diff(line: str, diff: int) -> bool:
    l = list(map(int, line.split()))
    for i in range(len(l) - 1):
        if abs(l[i] - l[i + 1]) > diff:
            return False
    return True


def validate_set(line: str) -> bool:
    l = list(map(int, line.split()))
    s = set(l)
    return len(l) == len(s)


def main():
    safe = 0
    lines = read_input()
    for line in lines:
        if validate_asc(line) or validate_desc(line):
            if validate_set(line) and validate_diff(line, 3):
                safe += 1
        else:
            print(f"{line} is not safe")
    print(safe)


if __name__ == "__main__":
    main()

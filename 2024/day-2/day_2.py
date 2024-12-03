def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data


def validate_asc(l: list[int]) -> bool:
    s = sorted(l)
    return l == s


def validate_desc(l: list[int]) -> bool:
    s = sorted(l, reverse=True)
    return l == s


def validate_diff(l: list[int], diff: int) -> bool:
    for i in range(len(l) - 1):
        if abs(l[i] - l[i + 1]) > diff:
            return False
    return True


def validate_set(l: list[int]) -> bool:
    s = set(l)
    return len(l) == len(s)


def main():
    safe = 0
    diff = 3
    lines = read_input()
    for line in lines:
        l = list(map(int, line.split()))
        if validate_asc(l) or validate_desc(l):
            if validate_set(l) and validate_diff(l, diff):
                safe += 1
        else:
            print(f"{l} is not safe, need a further validation!")

    print(safe)


if __name__ == "__main__":
    main()

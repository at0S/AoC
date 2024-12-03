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

def ultimate_validator(l: list[int], diff: int) -> bool:
    return (validate_asc(l) or validate_desc(l)) and validate_diff(l, diff) and validate_set(l)


def main():
    result = {
            "safe":0, "original":0, "dampner":0, "total":0}
    diff = 3
    lines = read_input()
    for line in lines:
        result["total"] += 1
        l = list(map(int, line.split()))
        if ultimate_validator(l, diff):
            result["safe"] += 1
            result["original"] += 1
        else:
            for i in range(len(l)):
                popped = l.copy()
                popped.pop(i)
                if ultimate_validator(popped, diff):
                    result["safe"] += 1
                    result["dampner"] += 1
                    break

    print(f"FINAL RESULT:{result}")


if __name__ == "__main__":
    main()

def read_input() -> str:
    data = ''
    with open('input') as f:
        data = f.readlines()
    return data

def process(line: str) -> tuple[int, int]:
    left, right = line.split()
    return int(left), int(right)

def calculate(left: list, right: list) -> int:
    final = 0
    left = sorted(left)
    right = sorted(right)
    for i in range(len(left)):
        final = final + abs(right[i] - left[i])
    return final

def similarity(number: int, right: list) -> int:
    score = 0
    for i in range(len(right)):
        if number == right[i]:
            score = score + 1
    return number * score

def similarity_score(left: list, right: list) -> int:
    similarity_score = 0
    for i in range(len(left)):
        similarity_score = similarity_score + similarity(left[i], right)
    return similarity_score

def main():
    left, right = [], []
    lines = read_input()
    for line in lines:
        l, r = process(line)
        left.append(l)
        right.append(r)

    print(calculate(left, right))
    print(similarity_score(left, right))

if __name__ == '__main__':
    main()


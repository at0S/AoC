def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data

def simple_multiply(line:str) -> int:  
    print(f"line: {line}")
    simple_multiply = 0
    samples = line.split("mul(")
    del samples[0]
    for sample in samples:
        khunk = sample.split(")")[0]
        nums = khunk.split(",")
        left, right = 0, 0
        if len(nums) == 2:
            if nums[0].isdigit():
                left = int(nums[0])
            if nums[1].isdigit():
                right = int(nums[1])
        simple_multiply += left * right
    return simple_multiply

def more_complex_processing(line: str) -> str:
    acc = ""
    samples = line.split("don't()")
    if len(samples) > 1:
        acc = samples[0]
    for sample in samples[1:]:
        do_samples = sample.split("do()")
        acc = acc + "".join(do_samples[1:])
    return acc

def complex_processing(line:str, decision: str, acc:str = ""):
    print(f"line: {line}; decision: {decision}; acc: {acc}")
    if decision in line:
        left, right = line.split(decision, 1)
        if decision == "do()":
            acc += right
            return complex_processing(left, "don't()", acc)
        if decision == "don't()":
            acc += left
            return complex_processing(right, "do()", acc)
    else:
        return acc

def main():
    lines = read_input()
    line = "".join(lines)
    result = simple_multiply(line)
    print(f"simple_multiply: {result}")
    line = more_complex_processing(line)
    result = simple_multiply(line)
    print(f"complex_processing: {result}")

if __name__ == "__main__":
    main()

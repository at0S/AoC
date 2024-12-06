def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data

def get_list_midsection(data: list[str]) -> int:
    m = len(data) // 2 
    return int(data[int(m)])

def correctly_ordered(key: str, value: str, order: dict) -> bool:
    if key in order.keys():
        if value not in order[key]:
            return False
    else:
        return not correctly_ordered(value, key, order)
    return True

def filter_print_order(sequence: list[str], order: dict):
    for i in range(len(sequence) - 1):
        left = sequence[i]
        right = sequence[i+1]
        if not correctly_ordered(left, right, order):
            return None
    return sequence

def fix_print_order(sequence: list[str], order: dict):
    for i in range(len(sequence) - 1):
        left = sequence[i]
        right = sequence[i+1]
        if not correctly_ordered(left, right, order):
            sequence[i] = right
            sequence[i+1] = left
            sequence = fix_print_order(sequence, order)
    return sequence

def main():
    page_order = {}
    print_sequence = []
    data = read_input()
    for line in data:
        if "|" in line:
            key, value = line.strip().split("|")
            if key not in page_order.keys():
                page_order[(key)] = []
                page_order[key].append(value)
            else:
                page_order[key].append(value)
        else:
            if len(line.strip()) > 0:
                print_sequence.append(line.strip())

    original_middle = 0
    fixed_middle = 0
    for ps in print_sequence:
        ps = ps.split(",")
        original = filter_print_order(ps, page_order)
        fixed = fix_print_order(ps, page_order)
        if original is not None:
            original_middle += get_list_midsection(original)
        fixed_middle += get_list_midsection(fixed)
    print(f"Page Order: {page_order} \nPrint Sequence: {print_sequence}")                    
    print(f"Original Middle Numbers Sum: {original_middle}")
    print(f"Fixed Middle Numbers Sum: {fixed_middle - original_middle}")

if __name__ == "__main__":
    main()

def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data

def get_list_midsection(data: list[str]) -> int:
    m = len(data) // 2 
    return int(data[int(m)])

def check_order(left: str, right: str, order: dict) -> bool:
    if left in order.keys():
        if right not in order[left]:
            return False
    else:
        return not check_order(right, left, order)
    return True

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

    middle_numbers = 0
    for ps in print_sequence:
        ps = ps.split(",")
        for i in range(len(ps) - 1):
            if not check_order(ps[i], ps[i+1], page_order):
                break
        else:
            middle_numbers += get_list_midsection(ps)
                    
    print(f"Middle Numbers Sum: {middle_numbers}")

if __name__ == "__main__":
    main()

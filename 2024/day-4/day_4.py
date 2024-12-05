def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data


def neighbours(i: int, j: int, matrix):
    neighbours = []
    if i == 0 and j == 0:
        neighbours = [
            (matrix[i][j + 1], i, j + 1, "south"),
            (matrix[i + 1][j], i + 1, j, "east"),
            (matrix[i + 1][j + 1], i + 1, j + 1, "southeast"),
        ]
        return neighbours
    if i == 0 and j == len(matrix[i]) - 1:
        neighbours = [
            (matrix[i][j - 1], i, j - 1, "north"),
            (matrix[i + 1][j - 1], i + 1, j - 1, "northeast"),
            (matrix[i + 1][j], i + 1, j, "east"),
        ]
        return neighbours
    if i == len(matrix) - 1 and j == 0:
        neighbours = [
            (matrix[i - 1][j], i - 1, j, "west"),
            (matrix[i - 1][j + 1], i - 1, j + 1, "southwest"),
            (matrix[i][j + 1], i, j + 1, "south"),
        ]
        return neighbours
    if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        neighbours = [
            (matrix[i - 1][j], i - 1, j, "west"),
            (matrix[i - 1][j - 1], i - 1, j - 1, "northwest"),
            (matrix[i][j - 1], i, j - 1),
            "north",
        ]
        return neighbours
    if i == 0:
        neighbours = [
            (matrix[i][j - 1], i, j - 1, "north"),
            (matrix[i][j + 1], i, j + 1, "south"),
            (matrix[i + 1][j - 1], i + 1, j - 1, "northeast"),
            (matrix[i + 1][j], i + 1, j, "east"),
            (matrix[i + 1][j + 1], i + 1, j + 1, "southeast"),
        ]
        return neighbours
    if i == len(matrix) - 1:
        neighbours = [
            (matrix[i][j - 1], i, j - 1, "north"),
            (matrix[i][j + 1], i, j + 1, "south"),
            (matrix[i - 1][j - 1], i - 1, j - 1, "northwest"),
            (matrix[i - 1][j], i - 1, j, "west"),
            (matrix[i - 1][j + 1], i - 1, j + 1, "southwest"),
        ]
        return neighbours
    if j == 0:
        neighbours = [
            (matrix[i - 1][j], i - 1, j, "west"),
            (matrix[i - 1][j + 1], i - 1, j + 1, "southwest"),
            (matrix[i][j + 1], i, j + 1, "south"),
            (matrix[i + 1][j], i + 1, j, "east"),
            (matrix[i + 1][j + 1], i + 1, j + 1, "southeast"),
        ]
        return neighbours
    if j == len(matrix[i]) - 1:
        neighbours = [
            (matrix[i - 1][j], i - 1, j, "west"),
            (matrix[i - 1][j - 1], i - 1, j - 1, "northwest"),
            (matrix[i][j - 1], i, j - 1, "north"),
            (matrix[i + 1][j - 1], i + 1, j - 1, "northeast"),
            (matrix[i + 1][j], i + 1, j, "east"),
        ]
        return neighbours
    if i != 0 and i != len(matrix) - 1 and j != 0 and j != len(matrix[i]) - 1:
        neighbours = [
            (matrix[i - 1][j - 1], i - 1, j - 1, "northwest"),
            (matrix[i - 1][j], i - 1, j, "west"),
            (matrix[i - 1][j + 1], i - 1, j + 1, "southwest"),
            (matrix[i][j - 1], i, j - 1, "north"),
            (matrix[i][j + 1], i, j + 1, "south"),
            (matrix[i + 1][j - 1], i + 1, j - 1, "northeast"),
            (matrix[i + 1][j], i + 1, j, "east"),
            (matrix[i + 1][j + 1], i + 1, j + 1, "southeast"),
        ]
        return neighbours
    return neighbours

def get_southeast(i,j, matrix):
    if i < len(matrix) - 1 and j < len(matrix[i]) - 1:
        return matrix[i + 1][j + 1]
    return None

def get_northeast(i,j, matrix):
    if i > 0 and j < len(matrix[i]) - 1:
        return matrix[i - 1][j + 1]
    return None

def get_northwest(i,j, matrix):
    if i > 0 and j > 0:
        return matrix[i - 1][j - 1]
    return None

def get_southwest(i,j, matrix):
    if i < len(matrix) - 1 and j > 0:
        return matrix[i + 1][j - 1]
    return None


def find_x_mases(matrix):
    x_mases = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            if current == "A":
                if get_southeast(i, j, matrix) == "M" and get_northwest(i, j, matrix) == "S":
                    if get_southwest(i, j, matrix) == "S" and get_northeast(i, j, matrix) == "M":
                        x_mases += 1
                    if get_southwest(i, j, matrix) == "M" and get_northeast(i, j, matrix) == "S":
                        x_mases += 1
                if get_southeast(i, j, matrix) == "S" and get_northwest(i, j, matrix) == "M":
                    if get_southwest(i, j, matrix) == "M" and get_northeast(i, j, matrix) == "S":
                        x_mases += 1
                    if get_southwest(i, j, matrix) == "S" and get_northeast(i, j, matrix) == "M":
                        x_mases += 1
    return x_mases

def find_xmases(matrix):
    xmases = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            current_neighbours = neighbours(i, j, matrix)
            if current == "X":
                for neighbour in current_neighbours:
                    if neighbour[0] == "M":
                        current = "M"
                        current_m_neighbours = neighbours(neighbour[1], neighbour[2], matrix)
                        for m_neighbour in current_m_neighbours:
                            if m_neighbour[0] == "A" and m_neighbour[3] == neighbour[3]:
                                current = "A"
                                current_a_neighbours = neighbours(m_neighbour[1], m_neighbour[2], matrix)
                                for a_neighbour in current_a_neighbours:
                                    if a_neighbour[0] == "S" and a_neighbour[3] == neighbour[3]:
                                        xmases += 1
    return xmases


def main():
    data = read_input()
    matrix = [list(line.strip()) for line in data]
    xmases = find_xmases(matrix)
    print(f"xmases: {xmases}")
    x_mases = find_x_mases(matrix)
    print(f"x_mases: {x_mases}")

if __name__ == "__main__":
    main()

import copy

def read_input() -> list[str]:
    data = ""
    with open("input") as f:
        data = f.readlines()
    return data

def project(guard) -> tuple[int,int]:
    if guard["direction"] == "north":
        return (guard["position"][0] - 1, guard["position"][1])
    if guard["direction"] == "south":
        return (guard["position"][0] + 1, guard["position"][1])
    if guard["direction"] == "east":
        return (guard["position"][0], guard["position"][1] + 1)
    if guard["direction"] == "west":
        return (guard["position"][0], guard["position"][1] - 1)
    return (0,0)

def main():
    visited_obstacles = []
    loops = 0
    all_loops = []
    guard = {}
    projected = tuple()
    matrix = read_input()
    for i, line in enumerate(matrix):
        for j,char in enumerate(line):
            if char == "^":
                guard = {"position": (i,j), "direction": "north", "steps": 0, "squares": [(i,j)], "swd": [(i,j,"north")]}
            if char == "v":
                guard = {"position": (i,j), "direction": "south", "steps": 0, "squares": [(i,j)], "swd": [(i,j,"south")]}
            if char == ">":
                guard = {"position": (i,j), "direction": "east", "steps": 0, "squares": [(i,j)], "swd": [(i,j,"east")]}
            if char == "<": 
                guard = {"position": (i,j), "direction": "west", "steps": 0, "squares": [(i,j)], "swd": [(i,j,"west")]}

    while True:
        projected = project(guard)
        if projected[0] < 0 or projected[1] < 0 or projected[0] >= len(matrix) or projected[1] >= len(matrix[0]):
            break
        else:
            if matrix[projected[0]][projected[1]] == "#":
                visited_obstacles.append(projected)
                if guard["direction"] == "north":
                    guard["direction"] = "east"
                    continue 
                if guard["direction"] == "south":
                    guard["direction"] = "west"
                    continue
                if guard["direction"] == "east":
                    guard["direction"] = "south"
                    continue
                if guard["direction"] == "west":
                    guard["direction"] = "north"
                    continue

            x,y = projected
            square_with_direction = (x, y, guard["direction"])
            guard["squares"].append((x,y))
            guard["swd"].append(square_with_direction)
            guard["position"] = projected
            guard["steps"] += 1

            # imagine obstacle in front
            imaginary_guard = copy.deepcopy(guard)
            if guard["direction"] == "north":
                imaginary_guard["direction"] = "east"
            if guard["direction"] == "south":
                imaginary_guard["direction"] = "west"
            if guard["direction"] == "east":
                imaginary_guard["direction"] = "south"
            if guard["direction"] == "west":
                imaginary_guard["direction"] = "north"
            
            while True:
                # so the problem now, I need to project imaginary guard trajectory up until he breaks out of maze
                # each position should be compared to visited squares of real gurd. I also need to check
                # if the imaginary guard is going to hit the obstacle on the very first step.
                if imaginary_guard["position"][0] < 1 or imaginary_guard["position"][1] < 1 or imaginary_guard["position"][0] >= len(matrix) - 1  or imaginary_guard["position"][1] >= len(matrix[0]) - 1:
                    break
                projected_i = project(imaginary_guard)
                i_i, j_i = projected_i
                if matrix[i_i][j_i] == "#":
                    if imaginary_guard["direction"] == "north":
                        imaginary_guard["direction"] = "east"
                        continue 
                    if imaginary_guard["direction"] == "south":
                        imaginary_guard["direction"] = "west"
                        continue
                    if imaginary_guard["direction"] == "east":
                        imaginary_guard["direction"] = "south"
                        continue
                    if imaginary_guard["direction"] == "west":
                        imaginary_guard["direction"] = "north"
                        continue
                
                x_i, y_i = projected_i
                square_with_direction_i = (x_i, y_i, imaginary_guard["direction"])
                imaginary_guard["position"] = projected_i
                imaginary_guard["swd"].append(square_with_direction_i)
                if square_with_direction_i in guard["swd"]:
                    alpha, beta = guard["position"]
                    if imaginary_guard["direction"] == "north":
                        # he is actually moving west
                        beta -=1
                    if imaginary_guard["direction"] == "south":
                        # he is actually moving east
                        beta += 1
                    if imaginary_guard["direction"] == "east":
                        # he is actually moving north
                        alpha -= 1
                    if imaginary_guard["direction"] == "west":
                        # he is actually moving south
                        alpha += 1
                    print(f"loop at: {guard['position']} when imaginary guard is moving: {imaginary_guard['direction']}")

                    all_loops.append((alpha, beta))
                    loops += 1
                    break
                c = imaginary_guard["swd"].count(square_with_direction_i)
                if c > 1:
                    break


    print(f"guard total steps: {guard['steps']}")
    print(f"squares travelled: {guard['swd']}")
    print(f"uniquely travelled: {len(set(guard['squares']))}")

    print(f"loops: {len(set(all_loops))}")       
    print(f"all loops: {all_loops}")

if __name__ == "__main__":
    main()

# area of a simple polygon where vertices are (x, y) coordinates
def shoelace(coordlist):
    area = 0
    for idx in range(len(coordlist)):
        area += (coordlist[idx][0] * (coordlist[idx-1][1] - coordlist[(idx+1) % len(coordlist)][1]))
    return abs(area) // 2

# area of the interior of a simple polygon 
def picks(area, edges):
    return (area - (edges // 2) + 1)

def part1(lines):
    coords = [(0, 0)]
    edges = 0
    for line in lines:
        dig_dir, dig_len, dig_rgb = line.split()
        edges += int(dig_len)
        next_coord = coords[-1]
        match dig_dir:
            case "R":
                next_coord = (next_coord[0] + 0, next_coord[1] + int(dig_len))
            case "D":
                next_coord = (next_coord[0] + int(dig_len), next_coord[1])
            case "L":
                next_coord = (next_coord[0] + 0, next_coord[1] - int(dig_len))
            case "U":
                next_coord = (next_coord[0] - int(dig_len), next_coord[1])
        coords.append(next_coord)

    area = shoelace(coords)
    inside = picks(area, edges)

    # answer is the inside area + number of edges
    # since shoelace is exact, and problem set needs whole 1^3 area of a given point,
    # inside area + number of edges gives the answer
    ans1 = inside + edges
    print(f"1: {ans1}")

def part2(lines):
    edges = 0
    coords = [(0, 0)]
    dig_dir_map = {0: "R", 1: "D", 2: "L", 3: "U"}
    for line in lines:
        _, _, dig_rgb = line.split()
        dig_rgb = dig_rgb.replace("(", "").replace(")", "")
        dig_dir = dig_dir_map[int(dig_rgb[-1])]
        dig_len = int(dig_rgb[1:-1], 16)
        
        # same as part 1 from here on
        edges += int(dig_len)
        next_coord = coords[-1]
        match dig_dir:
            case "R":
                next_coord = (next_coord[0] + 0, next_coord[1] + int(dig_len))
            case "D":
                next_coord = (next_coord[0] + int(dig_len), next_coord[1])
            case "L":
                next_coord = (next_coord[0] + 0, next_coord[1] - int(dig_len))
            case "U":
                next_coord = (next_coord[0] - int(dig_len), next_coord[1])
        coords.append(next_coord)
    
    ans2 = picks(shoelace(coords), edges) + edges
    
    print(f"2: {ans2}")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    part1(lines)
    part2(lines)

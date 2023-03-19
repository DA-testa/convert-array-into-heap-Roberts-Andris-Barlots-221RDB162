# python3
def sift_down(data, i, swaps):
    smallest_value = i
    right_side = 2 * i + 2
    left_side = 2 * i + 1

    if left_side < len(data) and data[left_side] < data[smallest_value]:
        smallest_value = left_side

    if right_side < len(data) and data[right_side] < data[smallest_value]:
        smallest_value = right_side

    if i != smallest_value:
        data[i], data[smallest_value] = data[smallest_value], data[i]
        swaps.append((i, smallest_value))
        sift_down(data, smallest_value, swaps)

def build_heap(data):
    swaps = []
    for i in range(len(data)//2, -1, -1):
        sift_down(data, i, swaps)    
    return swaps

def main():
    text = input()

    if text == "F":
        file = str(input())
        if "a" not in file:
            file = "tests/" + file
            with open(file, "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
    elif text == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()

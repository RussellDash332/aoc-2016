n = int(input())

arr = list(range(n))
while len(arr) != 1:
  arr = arr[2 * (len(arr) % 2)::2]
print("Part 1:", arr[0] + 1)

arr = list(range(n))
while len(arr) > 2:
    k = len(arr)
    tri = k // 6 - 1
    if k % 6 == 1:
        arr = arr[:3 * tri + 1:3] + arr[3 * tri + 2:3 * tri + 6:2] + arr[3 * tri + 7::3]
    elif k % 6 == 5:
        arr = arr[1:3 * tri + 5:3] + arr[3 * tri + 6:3 * tri + 8:2] + arr[3 * tri + 9::3]
    elif k % 6 == 4:
        arr = arr[:3 * tri + 4:3] + arr[3 * tri + 4::3]
    elif k % 6 == 2:
        arr = arr[1:3 * tri + 2:3] + arr[3 * tri + 4:3 * tri + 6:2] + arr[3 * tri + 6::3]
    else:
        arr = arr[2::3]
print("Part 2:", arr[0] + 1)
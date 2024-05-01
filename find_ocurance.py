array = sorted([1, 7, 1, 0, 5, 7, 7, 8,10,11,12,12,13,142])

start = -1
end = -1
target = 7
for i in range(int(len(array)/2) + 1):
    if array[i] == target:
        if start == -1:
            start = i
    if array[len(array) - 1 - i] == target:
        if end == -1:
            end = len(array) - 1 - i

if start != -1 and end != -1:
    print(start, end)
else:
    print(-1)

low = 0
high = len(array) - 1
while low <= high:
    mid = int((low + high) / 2)
    if array[mid] == target:
        start = mid
        high = mid - 1
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(start)
low = 0
high = len(array) - 1
while low <= high:
    print(low, high)
    mid = int((low + high) / 2)
    if array[mid] == target:
        end = mid
        low = mid + 1
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(end)


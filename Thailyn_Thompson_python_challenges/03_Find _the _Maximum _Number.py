def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(find_maximum([4,9,1,17,2]))  # Output: 17
print(find_maximum([-5,-2,-9,-1]))  # Output: -1
print(find_maximum([12]))  # Output: 12
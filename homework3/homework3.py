#1 Oski Stole Your Power
def power(x,y):
    x = 2
    y = 3
    exp = x * x
    return((y-1)*exp)
print(power(2,3))

#2 What Should I Wear
def tempRange(min,max):
    readings = [15,14,17,20,23,28,20]
    return (min(readings),max(readings))
print (tempRange(min,max))

#3 Check If Its The Weekend
day = 6
def weekend (day):
    if day>5:
        return True
    else:
        return False
print(weekend(day))

#4 Fuel Efficiency Calculator
def fuel_efficiency(distance,fuel):
    distance = 70
    fuel = 21.5
    return (distance/fuel)
print (fuel_efficiency(70,21.5))

#5 Secret Code
def decodeNumbers(n):
    last_digit = n % 10  
    remaining_part = n // 10 
    multiplier = 1
    temp = remaining_part
    while temp > 0:
        temp //= 10
        multiplier *= 10
    return last_digit * multiplier + remaining_part 
print(decodeNumbers(12345))

#6 Min and Max But With Loops
#6.1
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loop(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value
print(find_min_with_for_loop(nums))
    
def find_max_with_for_loops(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
        return max_value
print (find_max_with_for_loops(nums))

#6.2
def find_min_with_while_loop(nums):
    min_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    return min_val
print(find_min_with_while_loop(nums))

def find_max_with_while_loop(nums):
    max_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val
print(find_max_with_while_loop(nums))

#7 Counting Vowels
text = 'UC Berkeley, founding in 1868!'
def vowel_and_consonant_count(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1

            else:
                consonant_count += 1
    return (vowel_count, consonant_count)
print(vowel_and_consonant_count(text))


#8 Calculate Digital Root
num = 2468
def digital_root(num):
    digital_sum = 0
    while num > 0:
        digital_sum += num % 10
        num //= 10
    return digital_sum
print(digital_root(num))    
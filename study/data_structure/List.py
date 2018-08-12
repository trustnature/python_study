"""
列表：有序，异构，动态
"""
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

nums = [1, 2, 3, 4]
nums.remove(3)
print(nums)
nums.pop()
print(nums)
nums.pop(0)
print(nums)
nums.extend([3, 4])
print(nums)
nums.insert(0, 1)
print(nums)

first = [1, 2, 3, 4, 5]
second = first
second.append(6)
print(second)
print(first)
third = first.copy()
third.append(7)
print(third)
print(first)

saying = "Don't panic!"
letters = list(saying)
print(letters)
print(letters[1])
print(letters[-1])
print(letters[3:])
print(letters[0:10:3])
print(letters[::2])
print(''.join(letters[::2]))

# 空集合返回 []
l = list();
print(l)
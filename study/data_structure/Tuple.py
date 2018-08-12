"""
元组 不可变
与列表区别：列表用中括号 元组用小括号
"""
vowels1 = ['a', 'e', 'i', 'o', 'u']
print(type(vowels1))
print(vowels1)
vowels2 = ('a', 'e', 'i', 'o', 'u')
print(type(vowels2))
print(vowels2)

t = ('Python')
print(type(t))
print(t)
t2 = ('Python',)
print(type(t2))
print(t2)

c = tuple()
# 空元组返回 ()
print(c)


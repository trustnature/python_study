"""
集合测试
不允许重复
与字典区别时 只有键 没有 :
"""

vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
print(vowels)

vowels = set('aeiou')
word = 'hello'
# 集合
u = vowels.union(word)
print(u)
#转换成列表
u_list = sorted(list(u))
print(u_list)
#那些不是共有元素
d = vowels.difference(set(word))
print(d)
#共有元素
i = vowels.intersection(set(word))
print(i)

c = set();
# 空集合返回 set()
print(c)
"""
函数定义
函数之间 间隔两个空行
"""


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


print(search4vowels('cesassde'))
print(search4letters('shlloe'))
print(search4letters(letters='xyz', phrase='galaxy'))

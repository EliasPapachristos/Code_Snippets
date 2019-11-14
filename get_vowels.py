def get_vowels(string):
    return [each for each in string if each in 'aeiou']


print(get_vowels('kendo'))
print(get_vowels('martial art'))
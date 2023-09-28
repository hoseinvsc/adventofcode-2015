  

def has_3_vowel(s):
    vowels = "aeiou"
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return True
    return False



def is_twice_repeated(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def have_disalow_char(s):
    disallowed_strings = ["ab", "cd", "pq", "xy"]
    for substring in disallowed_strings:
        if substring in s:
            return True
    return False



with open("problem5/day5.txt", "r") as file:
    lines = file.readlines()
    nice_count = 0
    
    for line in lines:
        line = line.strip()
        if has_3_vowel(line) and is_twice_repeated(line) and not have_disalow_char(line):
            nice_count += 1
    print(nice_count)
def are_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count = {}

    # ✅ First loop: build frequency map from str1
    for char in str1:
        count[char] = count.get(char, 0) + 1

    # ✅ Second loop: validate using str2
    for char in str2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_anagram(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")

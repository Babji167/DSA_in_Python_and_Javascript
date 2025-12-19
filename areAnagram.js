function areAnagram(str1, str2) {
    // Step 1: If lengths are different, they can't be anagrams
    if (str1.length !== str2.length) {
        return false;
    }

    // Step 2: Create a character count map for str1
    const charCount = {};

    for (let char of str1) {
        // If character already exists, increment count
        // Otherwise, initialize it to 1
        charCount[char] = (charCount[char] || 0) + 1;
    }

    // Step 3: Subtract character counts using str2
    for (let char of str2) {
        // If character doesn't exist or count is zero, not an anagram
        if (!charCount[char]) {
            return false;
        }

        // Decrease the count for matched character
        charCount[char]--;
    }

    // Step 4: All characters matched correctly
    return true;
}

str1="test";
str2="stay";

result = areAnagram(str1,str2);
if (result){
    console.log("given strings are Anagram");
}
else{
    console.log("Not Anagram");
}
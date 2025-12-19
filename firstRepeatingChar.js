function firstRepeatingChar(str) {
    const seen = new Set();

    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (seen.has(char)) {
            return i; // First repeating character found
        }
        seen.add(char);
    }

    return -1; // No repeating character
}

str="steelhound"
result = firstRepeatingChar(str)
if (result){
    console.log(`${str} is having a single left Repeating character in it!!`)
}else{
    console.log("It has more repeating left character")
}
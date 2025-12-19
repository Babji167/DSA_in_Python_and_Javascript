const readline = require("readline");
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
const isPalindrome = (input) => {
  for (let i = 0; i < input.length/2; i++) {
    if (input[i] !== input[input.length - i - 1]) return false;
  }
  return true;
};

const main = () => {
    rl.question('Enter a string: ', (input) => {
        if (isPalindrome(input)) {
            console.log(`${input} is a palindrome`);
        } else {
            console.log(`${input} is not a palindrome`);
        }
        rl.close();
    });
};
main();



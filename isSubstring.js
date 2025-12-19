const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const isSubSeq = (s1, s2, n, m) => {
  if (m === 0) return true;
  if (n === 0) return false;
  if (s1[n - 1] === s2[m - 1]) return isSubSeq(s1, s2, n - 1, m - 1);
  else return isSubSeq(s1, s2, n - 1, m);
};

const main = () => {
  rl.question("Enter first string (s1): ", (s1) => {
    rl.question("Enter second string (s2): ", (s2) => {
      const n = s1.length;
      const m = s2.length;
      const result = isSubSeq(s1, s2, n, m);
      console.log(result ? "s2 is a subsequence of s1" : "s2 is NOT a subsequence of s1");
      rl.close();
    });
  });
};

main();
function reverseWordsAndCharacters(input) {
  // Step 1: Split the sentence into words
  const words = input.trim().split(' '); // ['smart', 'work']

  // Step 2: Reverse the order of words
  const reversedOrder = [];
  for (let i = words.length - 1; i >= 0; i--) {
    reversedOrder.push(words[i]); // ['work', 'smart']
  }

  // Step 3: Reverse each word individually
  const finalWords = [];
  for (let i = 0; i < reversedOrder.length; i++) {
    const word = reversedOrder[i];
    let reversedWord = '';
    for (let j = word.length - 1; j >= 0; j--) {
      reversedWord += word[j]; // reverse characters
    }
    finalWords.push(reversedWord); // ['krow', 'trams']
  }

  // Step 4: Join the final words into a sentence
  const result = finalWords.join(' ');
  console.log(result);
}

let input = "I'm Optimus Prime and this message is to my Creators"
reverseWordsAndCharacters(input)
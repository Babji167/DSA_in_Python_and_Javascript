function moveZeros(arr) {
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== 0) {
            [arr[i], arr[count]] = [arr[count], arr[i]];
            count++;
        }
    }
    return arr;
}


let arr2 = [10, 8, 0, 0, 12, 0];

console.log("Optimal Approach Output:");
console.log(moveZeros([...arr2]));
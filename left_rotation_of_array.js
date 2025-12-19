function leftRotateEfficient(arr) {
    let n = arr.length;
    let x = arr[0];

    for (let i = 1; i < n; i++) {
        arr[i - 1] = arr[i];
    }
    arr[n - 1] = x;
}
let arr = [1, 2, 3, 4, 5];
leftRotateEfficient(arr);
console.log("Rotated Array:", arr); 
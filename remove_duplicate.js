function remDups(arr) {
    let res = 1;
    for (let i = 1; i < arr.length; i++) {
        if (arr[res - 1] !== arr[i]) {
            arr[res] = arr[i];
            res++;
        }
    }
    return res;
}

let arr = [10, 20, 20, 30, 30, 30];
console.log("Before Removal: " + arr);
let n = remDups(arr);
console.log("After Removal: " + arr.slice(0,n));
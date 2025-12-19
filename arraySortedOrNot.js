function arraySortedOrNot(arr) {
    if (arr.length === 0 || arr.length === 1) {
        return true;
    }
    for (let i = 1; i < arr.length; i++) {
        if (arr[i - 1] > arr[i]) {
            return false;
        }
    }
    return true;
}

let arr = [20, 23, 23, 45, 78, 88];
if (arraySortedOrNot(arr)) {
    console.log("Yes");
} else {
    console.log("No");
}
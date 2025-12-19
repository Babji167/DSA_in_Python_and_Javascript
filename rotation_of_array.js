function rotation_of_array(arr) {
    let low_num = 0;
    let high_num = arr.length - 1;
    while (low_num < high_num) {
        let temp = arr[low_num];
        arr[low_num] = arr[high_num];
        arr[high_num] = temp;
        low_num++;
        high_num--;
    }
    return arr;
}

let arr = [11, 12, 13, 14, 15, 16];
let result = rotation_of_array(arr);
console.log(result);



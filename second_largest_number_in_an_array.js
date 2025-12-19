function second_largest_number(arr){
    let first_max = -1
    let second_max= -1
    for (let i=0; i<arr.length; i++){
        if (arr[i]>first_max){
            second_max = first_max
            first_max = arr[i]
        }
        else if (arr[i]<first_max && arr[i]>second_max){
            second_max = arr[i]
        }
    }
    return second_max
}

let arr = [11,12,34,25,67,24,89]
result = second_largest_number(arr)
console.log(result)
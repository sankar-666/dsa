// function myFunction(a){
//     a.slice(3)
//     return a
// }

// function
// myFunction
// (
// a, b
// )
// {

// return a.filter((el) => el != b )
// }

// function
// myFunction
// (
// a
// )
// {
// return a.reduce((acc, cur) => {
//     return acc + 1; 
// },0)
// }

function
    myFunction
    (
    arr
    )
    {
    start = 0;
    end = arr.length - 1;
    
    while(start <= end){
        console.log(start, end);
       if(arr[start] !== arr[end]){
           return false
       }
       start++;
       end--;
    }
    return true
    }

console.log(myFunction(['help', 'me']))
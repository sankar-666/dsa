// To find the factorial of a given Number
// here I am using a Reccursive function
// So just assume find factorial of n
// just return n * call same functon with argument as n-1

const findFactorial = (n) => {
    if(n == 1){
        return n
    }
    return n * findFactorial(n - 1)
}


console.log(findFactorial(10));


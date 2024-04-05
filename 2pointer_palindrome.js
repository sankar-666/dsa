// I want to check given string is a palindrom or not
// here I am using a two pointer approch
// assume i have a string
// I am storing  left value and right value in 2 variables
// then I will compare both values if they are equal then it's a palindrome otherwise not


const isPalindrome = (text) => {
    let start = 0;
    let end = text.length - 1;
    
    while (start < end) {
        if (text[start] !== text[end]) {
            return false;
        }
        start++;
        end--;
    }
    
    return true;
}

const text = 'msfdcdfsms'
console.log(isPalindrome(text));

// const isPalindrome = (text) => {
//     let start = 0;
//     let end = text.length - 1;
//     let flag = true 

//     while (start < end) {
//         if(text[start] == text[end]){
//             start++
//             end--
//         }else{
//             flag = false
//             break
//         }
//     }
    
//     return flag
// }

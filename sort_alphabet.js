
function myFunction(arr){
    return arr.sort( (a, b) => {
        if(a.charCodeAt(0) < b.charCodeAt(0)){
            return -1;
        }else if(a.charCodeAt(0) > b.charCodeAt(0)){
            return 1;
        }else{
            return 0;
        }
    })
}



console.log(myFunction(['b', 'c', 'd', 'a']));
console.log(myFunction(['z', 'c', 'd', 'a', 'y', 'a', 'w']));
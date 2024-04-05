

 const haveSameElements = (array1, array2) => {
    if (array1.length !== array2.length) {
      return false;
    }
  
    const frequencyCounter1 = new Map;
    for (const item of array1) {
      frequencyCounter1.set(item, (frequencyCounter1.get(item) || 0) + 1)
    }
  
    const frequencyCounter2 = new Map;
    for (const item of array2) {
        frequencyCounter2.set(item, (frequencyCounter2.get(item) || 0) + 1);
    }
    
    for (const [key, value] in frequencyCounter1) {
      if (!frequencyCounter2.has(key)) {
        return false;
      }
      if (frequencyCounter2.get(key) !== value) {
        return false;
      }
    }
    return true;
  };

console.log(haveSameElements([1,2,2,2,3],[3,1,2,2,2]))


// This is not a good Approch using sorting
// const haveSameElements = (array1, array2) => {
	
// 	if(array1.length !== array2.length){
// 		return false
// 	}

// 	a = array1.sort((a,b)=> a-b)
// 	b = array2.sort((a,b)=> a-b)

// 	for(let i = 0; i < a.length; i++ ){
// 		if(a[i] !== b[i]){
// 			return false
// 		}
// 	}
// 	return true
// }
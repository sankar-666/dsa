var twoSum = function(nums, target) {

    var indexArray = [];
    var length = nums.length
    nums.forEach((num,index)=>{
        console.log(index)
        if(nums[index-1] + nums[index] === target){
            indexArray = [...indexArray,index-1]
            indexArray = [...indexArray,index]
        }
    })
    return indexArray
};


console.log(twoSum([3,2,3],6))
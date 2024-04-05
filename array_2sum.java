import java.util.HashMap;
import java.util.Map;

public class array_2sum {

    // O(n^2) t   O(1) s
    public static int[] twoSum(int[] arr, int target){
        for(int i=0; i< arr.length -1; i++){
            for(int j = i+1; j< arr.length; j++){
                if(arr[i] + arr[j] == target){
                    return new int[] {arr[i], arr[j]};
                }
            }
        }
        return new int[0];
    } 

    // O(n) t  O(n) s
    public static int[] towSumwithHashSet(int[] arr, int target){
        Map<Integer, Integer> elementsMap = new HashMap<>();
        
        for(int i=0; i< arr.length; i++){
            int match = target - arr[i];
            if(elementsMap.containsKey(match)){
                return new int[]{arr[i], elementsMap.get(match)};
            }else{
                elementsMap.put(arr[i], arr[i]);
            }
        }
        

        return new int[0];
    }

    public static void main(String[] args) {
        int[] arr = {1,2,4,5,3,2,8,9};
        int[] out = towSumwithHashSet(arr, 12);
        for(int i=0; i< out.length; i++){
            System.out.println(out[i]);
        }
    }

}
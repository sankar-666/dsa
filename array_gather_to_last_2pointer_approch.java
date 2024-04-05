import java.util.HashMap;
import java.util.Map;

public class array_gather_to_last_2pointer_approch {

        // we can use a two pointer approch with O(n) ts

        public static int[] getherToLast(int[] arr){
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // Find the number with the maximum occurrence
        int maxOccurrenceNumber = arr[0]; // Default to the first element
        int maxCount = countMap.get(arr[0]); // Default count for the first element

        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxOccurrenceNumber = entry.getKey();
                maxCount = entry.getValue();
            }
        }
     
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            if( arr[start] == maxOccurrenceNumber){
                if(arr[end] == maxOccurrenceNumber){
                        end --;
                        continue;
                }else{
                    int temp = arr[end];
                    arr[end] = arr[start];
                    arr[start] = temp;
                    start ++;
                }
            }else{
                start++;
            }
    
        }
        
        return arr;
    }

    public static void main(String[] args) {
        int[] arr = {6, 1, 6, 8, 10, 4, 15, 6, 3, 9, 6};
        int[] result = getherToLast(arr);
        
        for(int i=0; i<result.length; i++){
            System.out.println(result[i]);
        }
    }
    
}

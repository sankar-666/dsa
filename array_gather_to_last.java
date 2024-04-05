// import java.util.ArrayList;
// import java.util.Collections;
// import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class array_gather_to_last {

    public static int[] getherToLast(int[] arr){
        Map<Integer, Integer> counterMap = new HashMap<>();
        int[] result = new int[arr.length];

        for(int i=0; i<arr.length; i++){
            counterMap.put(arr[i], counterMap.getOrDefault(arr[i], 0) + 1);
        }
        
        int max = 0;
        int idx = 0;
        for(int i : counterMap.keySet()){
            if(counterMap.get(i) > max ){
                max = counterMap.get(i);
                idx = i;
            }
        }

        int j = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] != idx){
                result[j] = arr[i];
                j+=1;
            }
        }

        for(int i=1; i<=max; i++){
            result[result.length - i] = idx;
        }

        return result;


        
        // OPTIMISED SOLUTION ,
        //  Map<Integer, Integer> counterMap = new HashMap<>();
        // List<Integer> result = new ArrayList<>();

        // for (int i : arr) {
        //     counterMap.put(i, counterMap.getOrDefault(i, 0) + 1);
        // }

        // int maxFrequency = Collections.max(counterMap.values());

        // for (int i : arr) {
        //     if (counterMap.get(i) != maxFrequency) {
        //         result.add(i);
        //     }
        // }

        // for (int i = 0; i < maxFrequency; i++) {
        //     result.add(maxFrequency);
        // }

        // return result.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        int[] arr = {6, 1, 6, 8, 10, 4, 15, 6, 3, 9, 6};
        int[] result = getherToLast(arr);
        
        for(int i=0; i<result.length; i++){
            System.out.println(result[i]);
        }

    }
    
}

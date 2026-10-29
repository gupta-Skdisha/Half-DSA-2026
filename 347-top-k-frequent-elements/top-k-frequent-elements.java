class Solution {
    public int[] topKFrequent(int[] nums, int k) {
         HashMap<Integer,Integer>map= new HashMap<>();
         int n =nums.length;
         for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        Integer[] arr=map.keySet().toArray(new Integer[0]);
        int[] result=new int[k]; 
        Arrays.sort(arr,(a,b)->map.get(b) - map.get(a));

        for(int num:nums){
            for(int i =0;i<k;i++){
                result[i]=arr[i];
            }

        }
        return result;
    }
}

class Solution {
    public long sumAndMultiply(int n) {
       if(n==0){
        return 0;
       }
       int sum=0;
       long rev=0;
       while(n>0){
        int dig=n%10;
        if(dig!=0){
            sum +=dig;
            rev=rev*10+dig;
        }
        n/=10;
       }
       long num=0;
       while(rev>0){
        num=num*10+rev%10;
        rev /=10;
       }
       return num * sum;
    }
}
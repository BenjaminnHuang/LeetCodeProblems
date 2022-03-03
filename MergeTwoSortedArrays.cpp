#include <vector>
using std::vector;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    
    //last index of array[m+n]
    int last = m + n - 1;
    
       while(n > 0 && m > 0){
           //compare last numbers of nums1 and nums2
           //Put the smaller value to the last index of nums1
            if(nums1[m - 1] < nums2[n - 1]){
                nums1[last] = nums2[n - 1];
                n-=1;
            }
            else{
                nums1[last] = nums1[m - 1];
                m-=1;
            }
            last-=1;
       }

       //Put the remaining value in nums1 
       while(n > 0){
           nums1[last] = nums2[n - 1];
           n-=1;
           last-=1;
       }
    }      
};


//1, 2 ,3
//2, 3, 4

//1,2,3,0,0,0
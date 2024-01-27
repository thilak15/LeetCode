class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force Approach
        # lets use a dict to find the next large element for every element in the nums2
        # Then create a res list by checking of this nums1 keys value sin the dict
        next_l={nums2[i]:-1 for i in range(len(nums2))} 
        #  intializing the dict with value s-1 so that if u dont find a greater value it will be -1
        res=[]

        for i in range(len(nums2)-1):
            for k in range(i+1,len(nums2)):
                print(nums2[k],nums2[i])
                if nums2[k]>nums2[i]:
                    next_l[nums2[i]]=nums2[k]
                    break
        print(next_l)
        for x in nums1:
            res.append(next_l[x])
        return res

        # Time complexity for this approach is O(n^2) n:length of nums2
        #space complexity is O(n+m) n:length if nums2 {dict length} ,m length of nums1 for result

        # We can reduce the time complexity by reducing the time comlexity for finding the next big element for that we can use stacks
        


                


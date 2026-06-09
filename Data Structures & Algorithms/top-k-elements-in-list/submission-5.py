class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num_freq = {}
        
        for i in range(len(nums)):
            if nums[i] not in dict_num_freq.keys():
                dict_num_freq[nums[i]] = 1
            else:
                dict_num_freq[nums[i]] +=1

        
        list_1 = list(dict_num_freq.items())
        print(list_1)  
        sorted_list = sorted(list_1,key = lambda x:x[1])
        print(sorted_list)
        return [x[0] for x in sorted_list[len(sorted_list)-k:]]
                

            
        
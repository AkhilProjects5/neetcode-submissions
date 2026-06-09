class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists_ana = []
        already_in = []
        for i in range(len(strs)):
            if strs[i] in already_in:
                continue
            else:
                sublist = [strs[i]]
                for j in range(i+1,len(strs)):
                    if (len(strs[i]) == len(strs[j])) and sorted(list(strs[i])) == sorted(list(strs[j])):
                        sublist.append(strs[j])
                        already_in.append(strs[j])
                        print(already_in)
            sublists_ana.append(sublist)
        return sublists_ana

        

# coding: utf-8

# In[35]:


nums = [-1, 0, 1, 2, -1, -4]
lists=[]
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for u in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[u]==0:
                lists.append([nums[i],nums[j],nums[u]])
#new_list = [list(t) for t in set(tuple(_) for _ in l)]
new_list = list(set(tuple(sorted(t)) for t in lists))
#a=list(set(lists))
print(new_list)      


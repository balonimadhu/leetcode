pos={}
nums=[-1,0,1,2,-1,-4]
nums.sort()
print(nums)
m=0
for i in range(len(nums)):
    for j in range( i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                pos[m]=nums[i],nums[j],nums[k]
                m=m+1
temp=[]
res={}
for key, val in pos.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print(res)        
                    

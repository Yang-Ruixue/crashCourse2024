def mergesort(nums):
    if len(nums)>1: #如果列表长度大于一，分割成左右两个部分
        mid=len(nums)//2 #计算分割点
        leftpart=nums[:mid] #分割左侧子列表
        rightpart=nums[mid:] #分割右侧子列表

        mergesort(leftpart) #递归地对左侧子列表进行分割
        mergesort(rightpart) #递归地对右侧子列表进行分割

        i,j,k=0,0,0
        while i<len(leftpart) and j<len(rightpart): #当左右子列表中都还有元素
            if leftpart[i]<rightpart[j]:
                nums[k]=leftpart[i]
                i=i+1
            else:
                nums[k]=rightpart[j]
                j=j+1
            k=k+1
        while i<len(leftpart): #如果左侧子列表还有剩余的元素
            nums[k]=leftpart[i]
            i=i+1
            k=k+1
        while j<len(rightpart): #如果右侧子列表还有剩余的元素
            nums[k]=rightpart[j]
            j=j+1
            k=k+1
    return nums
print(mergesort([5,1,1,2,0,0]))
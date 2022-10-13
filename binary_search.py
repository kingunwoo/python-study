
n_list = []
m_list = []


n_number = int(input())
n_list = [n_number]
n_list = list(map(int,n_list))



m_number = int(input())
m_list = [m_number]
m_list = list(map(int,m_list))


def binary_search(arr,target):
    arr.sort()
    start = 0
    last=len(arr)-1
    
    
    while(start<=last):
        mid=(start+last)//2
        
        if(arr[mid]==target):
            return mid
        
        elif(arr[mid]>target):
            last=n_list[mid]-1
            
        elif(arr[mid]<target):
            start=n_list[mid]+1
            
    return 0    

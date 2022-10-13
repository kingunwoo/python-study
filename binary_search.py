
n_number = int(input())
n_arr = list(map(int,input().split(' ')))
n_arr.sort()


m_number = int(input())
m_arr = list(map(int,input().split(' ')))


def binary_search(target):
    start = 0
    last=n_number-1
    
    
    while start<=last:
        mid=(start+last)//2
        
        if n_arr[mid]==target:
            return 1
        
        if n_arr[mid]>target:
            last=n_arr[mid]-1
            
        else:
            start=n_arr[mid]+1
            
    return 0    

for n in m_arr:
    print(binary_search(n))
    

                        
    



   
    
    
    

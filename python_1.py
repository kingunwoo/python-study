import random

n_list = []
m_list = []
c=None

n_number = random.randint(1,100000)
m_number = random.randint(1,100000)
print(n_number)
print(m_number)

for v in range(1,n_number+1):
    n_list.append(random.randint(1,100000))

print(n_list)
    
for v in range(1,m_number+1):
    m_list.append(random.randint(1,100000))     
    
print(m_list) 

for a in m_list:
    for b in n_list:
        if (a==b):
            print(1)
            c=True
            break
        
        elif(a != b):
            c=False
            
    if(c==False):
        print(0)    
              
    



   
    
    
    

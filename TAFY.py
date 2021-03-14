#!/usr/bin/env python
# coding: utf-8

# In[3]:


rules = dict()

#rules['A'] = 'b','c'
#rules['B'] = 'cA','bb'
#string = "...B"
#strings = 999999

rules['S'] = 'aQb','accb'
rules['Q'] = 'cSc'
string = "S"
strings = 5

stack = []
ready = []
stack.append(string)
no_not_term = 0 



# Левосторонний обход

while len(stack) > 0 and len(ready) <= strings:
    
    #отладка
    print("------------------------------")
    print("Stack: ",stack)                  
    print("Ready: ",ready)
    
    for key in rules:
        
        # проверка, что в текущей строке остались только терминалы
        if no_not_term == len(rules):
            ready.append(stack.pop(len(stack)-1))
            no_not_term = 0
            continue
            
        
        # проверка, что в текущей строке есть нетерминал key
        if len(stack) > 0:
            if stack[len(stack)-1].find(key, 0 , len(stack[len(stack)-1])) >= 0:
                no_not_term = 0
                tmp = stack.pop(len(stack)-1)
                #отладка
                print("нашелся нетерминал ",key)

                # замена нетерминала key всеми вариантами
                for j in range(len(rules[key])):
                        stack.append(tmp.replace(key, rules[key][j], 1))
                        #отладка
                        print("Замена нетерминала",key," на ",rules[key][j])

            else:
                no_not_term += 1
                continue
            
print("\n Цепочки: \n")
for i in range(len(ready)):
    print(i,") ",ready[i])


# In[ ]:





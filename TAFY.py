#!/usr/bin/env python
# coding: utf-8

# In[11]:


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

# первое попавшееся правило обход
# если беск то strings цепочек

while len(stack) > 0 and len(ready) <= strings:
    
    #отладка
    print("------------------------------")
    print("Stack: ",stack)                  
    print("Ready: ",ready,"\n")
    
    for key in rules:
        
        # проверка, что в текущей строке остались только терминалы
        if no_not_term == len(rules):
            
            #отладка
            print(stack[len(stack)-1]," -> ready")
                
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


# In[81]:


def iterate_left(stack,ready,rules,debug):
    
    no_not_term = 0 
    
    #ОТЛАДКА
    if debug:
        print("------------------------------")
        print("Stack: ",stack)                  
        print("Ready: ",ready,"\n")
    #--------------------------------------
    
    # проходим все элементы строки СЛЕВА на право (1)
    for char in stack[len(stack)-1]:
        
        #ОТЛАДКА
        if debug:
            print("Нетерминальные сиволы в сстроке ",no_not_term / len(rules))
        #-----------------------------------------------------------------
        
        # каждый элемент сравниваем с ключом из правил
        for key in rules:
            
            #ОТЛАДКА
            if debug:
                print("Check ",char," for ",key," in ",stack[len(stack)-1])
            #-----------------------------------------------------------------
                   
            # если элемент это ключ из правил, то заменяем (2)
            if char == key:
                no_not_term = 0
                tmp = stack.pop(len(stack)-1)

                for j in range(len(rules[key])):
                        stack.append(tmp.replace(key, rules[key][j], 1))
                        
                        #ОТЛАДКА
                        if debug:
                            print("Замена нетерминала",key," на ",rules[key][j])
                        #---------------------------------------------------
                
                        
                        
                return
            # если элемент не является хоть одним из ключей (3)
            else:
                no_not_term += 1
                
            # проверка, что в текущей строке остались только терминалы (3)
            # если каждый элемент это не ключ     
            if no_not_term == len(rules)*len(stack[len(stack)-1]):

                #ОТЛАДКА
                if debug:
                    print(stack[len(stack)-1]," -> ready")
                #-------------------------------------

                ready.append(stack.pop(len(stack)-1))
                no_not_term = 0
                
                return
        
rules = dict()

rules['A'] = 'b','c'
rules['B'] = 'cA','bb'
string = ".B."

stack = []
ready = []
stack.append(string)

        
while len(stack) > 0:
    iterate_left(stack,ready,rules,False)
            
print("\n Цепочки: \n")
for i in range(len(ready)):
    print(i,") ",ready[i])


# In[ ]:





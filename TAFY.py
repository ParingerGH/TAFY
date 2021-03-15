#!/usr/bin/env python
# coding: utf-8

# In[1]:


def iterate_left(stack,ready,rules,min_len,max_len,debug):
    
    no_not_term = 0 
    
    #ОТЛАДКА
    if debug:
        print("------------------------------")
        print("Stack: ",stack)                  
        print("Ready: ",ready,"\n")
    #--------------------------------------
    
    # отсекам слишком длинные
    if len(stack[len(stack)-1]) > max_len:
        stack.pop(len(stack)-1)
        return
    
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
                if len(stack[len(stack)-1]) <= max_len and len(stack[len(stack)-1]) >= min_len:
                    ready.append(stack.pop(len(stack)-1))
                else:
                    stack.pop(len(stack)-1)
                no_not_term = 0
                
                return
        
rules = dict()

rules['S'] = 'T','+T','-T'
rules['T'] = 'F','TF'
rules['F'] = '0','1','2','3','4','5','6','7','8','9'
string = "S"

stack = []
ready = []
stack.append(string)

        
while len(stack) > 0:
    iterate_left(stack,ready,rules,2,4,False)
            
print("\n Цепочки: \n")
for i in range(len(ready)):
    print(i,") ",ready[i])


# In[7]:


def iterate_right(stack,ready,rules,min_len,max_len,debug):
    
    no_not_term = 0 
    
    #ОТЛАДКА
    if debug:
        print("------------------------------")
        print("Stack: ",stack)                  
        print("Ready: ",ready,"\n")
    #--------------------------------------
    
    # отсекам слишком длинные
    if len(stack[len(stack)-1]) > max_len:
        stack.pop(len(stack)-1)
        return
    
    # проходим все элементы строки СЛЕВА на право (1)
    cur_str = stack[len(stack)-1][::-1]
    for char in cur_str:
        
        
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
                if len(stack[len(stack)-1]) <= max_len and len(stack[len(stack)-1]) >= min_len:
                    ready.append(stack.pop(len(stack)-1))
                else:
                    stack.pop(len(stack)-1)
                no_not_term = 0
                
                return
        
rules = dict()

rules['S'] = 'T','+T','-T'
rules['T'] = 'F','TF'
rules['F'] = '0','1','2','3','4','5','6','7','8','9'
string = "S"

stack = []
ready = []
stack.append(string)

        
while len(stack) > 0:
    iterate_right(stack,ready,rules,2,2,False)
            
print("\n Цепочки: \n")
for i in range(len(ready)):
    print(i,") ",ready[i])


# In[ ]:





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
    iterate_left(stack,ready,rules,2,2,False)
            
print("\n Цепочки: \n")
for i in range(len(ready)):
    print(i,") ",ready[i])


# In[9]:


def replaseE(string, null_simbol):
    ans_str = ""
    for i in range (0,len(string)):
        if string[i] != null_simbol:
            ans_str += string[i]
    return ans_str

def iterate_right(stack,ready,rules,min_len,max_len,debug):
    
    no_not_term = 0 
    
    #ОТЛАДКА
    if debug:
        print("------------------------------")
        print("Stack: ",stack)  
        print("Ready: ",ready,"\n")
    #--------------------------------------
    
    e = next(iter(stack))
    
    # отсекам слишком длинные
    if len(e) > max_len:
        
        if debug:
            print("Удалено ",e," тк ",len(e)," > ",max_len)
        
        stack.remove(e)
        return

    
    #пустая цепочка
    if len(e) == 0 and min_len != 0:
        stack.remove(e)
        return
    elif len(e) == 0:
        ready.add(e)
        stack.remove(e)
        return
        
    cur_str = e[::-1]
    
    
    for char in cur_str:
        
        
        #ОТЛАДКА
        if debug:
            print("Нетерминальные сиволы в сстроке ",no_not_term / len(rules))
        #-----------------------------------------------------------------
        
        # каждый элемент сравниваем с ключом из правил
        for key in rules:
            
            #ОТЛАДКА
            if debug:
                print("Check ",char," for ",key," in ",e)
            #-----------------------------------------------------------------
                   
            # если элемент это ключ из правил, то заменяем (2)
            if char == key:
                no_not_term = 0
                
                tmp = cur_str
                stack.remove(e)
                

                for j in range(len(rules[key])):
                        stack.add(tmp.replace(key, rules[key][j], 1))
                        
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
            if no_not_term == len(rules)*len(e):
         
                #-------------------------------------
                if len(e) <= max_len and len(e) >= min_len:
                    
                    
                    
                    ready.add(replaseE(e,null_simbol))
                    stack.remove(e)
                    
                    if debug:
                        print(e,"-> ready")

                else:
                    stack.remove(e)

                nono_not_term = 0
                
                return 10
        
rules = dict()

rules['S'] = 'AAA',
rules['A'] = 'AAA','0','e'
string = "S"

null_simbol = 'e'

stack = set()
ready = set()
stack.add(string)

        
while len(stack) > 0:
    iterate_right(stack,ready,rules,0,4,True)
        
count = 1
print("\n Цепочки: \n")
for i in ready:
    print(count,") ","длинна ",len(i)," ",i)
    count += 1


# In[10]:


def replaseE(string, null_simbol):
    ans_str = ""
    for i in range (0,len(string)):
        if string[i] != null_simbol:
            ans_str += string[i]
    return ans_str

def iterate_left(stack,ready,rules,min_len,max_len,debug):
    
    no_not_term = 0 
    
    #ОТЛАДКА
    if debug:
        print("------------------------------")
        print("Stack: ",stack)  
        print("Ready: ",ready,"\n")
    #--------------------------------------
    
    e = next(iter(stack))
    
    # отсекам слишком длинные
    if len(e) > max_len:
        
        if debug:
            print("Удалено ",e," тк ",len(e)," > ",max_len)
        
        stack.remove(e)
        return

    
    #пустая цепочка
    if len(e) == 0 and min_len != 0:
        stack.remove(e)
        return
    elif len(e) == 0:
        ready.add(e)
        stack.remove(e)
        return
        
    cur_str = e
    
    
    for char in cur_str:
        
        
        #ОТЛАДКА
        if debug:
            print("Нетерминальные сиволы в сстроке ",no_not_term / len(rules))
        #-----------------------------------------------------------------
        
        # каждый элемент сравниваем с ключом из правил
        for key in rules:
            
            #ОТЛАДКА
            if debug:
                print("Check ",char," for ",key," in ",e)
            #-----------------------------------------------------------------
                   
            # если элемент это ключ из правил, то заменяем (2)
            if char == key:
                no_not_term = 0
                
                tmp = cur_str
                stack.remove(e)
                

                for j in range(len(rules[key])):
                        stack.add(tmp.replace(key, rules[key][j], 1))
                        
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
            if no_not_term == len(rules)*len(e):
         
                #-------------------------------------
                if len(e) <= max_len and len(e) >= min_len:
                    
                    
                    
                    ready.add(replaseE(e,null_simbol))
                    stack.remove(e)
                    
                    if debug:
                        print(e,"-> ready")

                else:
                    stack.remove(e)

                nono_not_term = 0
                
                return 10
        
rules = dict()

rules['S'] = 'AAA',
rules['A'] = 'AAA','0','e'
string = "S"

null_simbol = 'e'

stack = set()
ready = set()
stack.add(string)

        
while len(stack) > 0:
    iterate_left(stack,ready,rules,0,4,True)
        
count = 1
print("\n Цепочки: \n")
for i in ready:
    print(count,") ","длинна ",len(i)," ",i)
    count += 1


# In[ ]:





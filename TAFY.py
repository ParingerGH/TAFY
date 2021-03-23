#!/usr/bin/env python
# coding: utf-8

# In[22]:


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
                        stack.add(tmp.replace(key, rules[key][j], 1)[::-1])
                        
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
                if len(replaseE(e,null_simbol)) <= max_len and len(replaseE(e,null_simbol)) >= min_len:
                    
                    
                    
                    ready.add(replaseE(e,null_simbol))
                    stack.remove(e)
                    
                    if debug:
                        print(e,"-> ready")

                else:
                    stack.remove(e)

                nono_not_term = 0
                
                return 10
        
rules = dict()

#
#rules['S'] = 'AAA',
#rules['A'] = 'AAA','0','e'
#string = "S"

#1
#rules['S'] = 'aQb','accb',
#rules['Q'] = 'cSc',
#string = "S"

#6
#rules['S'] = 'aSb','bSa','SS','e'

#7 чот не то она там написала
#rules['S'] = 'AB','aAb','bBa','e'

#8
rules['S'] = 'A#','B#',
rules['A'] = 'a','Ba'
rules['B'] = 'b','Bb','Ab'

string = "S"

null_simbol = 'e'

stack = set()
ready = set()
stack.add(string)

        
while len(stack) > 0:
    iterate_right(stack,ready,rules,0,7,True)
        
count = 1
print("\n Цепочки: \n")
for i in ready:
    print(count,") ","длинна ",len(i)," ",i)
    count += 1


# In[23]:


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
                if len(replaseE(e,null_simbol)) <= max_len and len(replaseE(e,null_simbol)) >= min_len:
                    
                    
                    
                    ready.add(replaseE(e,null_simbol))
                    stack.remove(e)
                    
                    if debug:
                        print(e,"-> ready")

                else:
                    stack.remove(e)

                nono_not_term = 0
                
                return 10
        
rules = dict()

#rules['S'] = 'AAA',
#rules['A'] = 'AAA','0','e'
#string = "S"

#8
rules['S'] = 'A#','B#',
rules['A'] = 'a','Ba'
rules['B'] = 'b','Bb','Ab'

null_simbol = 'e'

stack = set()
ready = set()
stack.add(string)

        
while len(stack) > 0:
    iterate_left(stack,ready,rules,4,6,True)
        
count = 1
print("\n Цепочки: \n")
for i in ready:
    print(count,") ","длинна ",len(i)," ",i)
    count += 1


# In[ ]:





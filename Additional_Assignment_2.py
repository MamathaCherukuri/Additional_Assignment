#!/usr/bin/env python
# coding: utf-8

# 1) The function "echo_name" takes 2 parameters: a string value, "name1"and
# an integer value, "echo_int". It returns a string that is a concatenation of
# "echo_int" copies of "name1".

# In[1]:


# Define a lambda function: echo_name
echo_name = (lambda x, y: x * y)
# Call echo_name with parameters ("acadgild",5)
result = echo_name ("acadgild",5)
# Print result
print(result)


# 2) Convert temperature in Celsius to Fahrenheit using map() and lambda
# functions 

# In[4]:


Celsius = [49.2, 26.5, 47.3, 47.8]
Fahrenheit=list(map(lambda c:9/5*c+32,Celsius))
print("Farenhiet Data : ",Fahrenheit)


# 3) The function filter(function, list) filters out all the elements of a list, for
# which the function function returns True.

# In[20]:


sample_string = "Welcome to AcadGild"
vowels_output=list(filter(lambda x: x in "aeiouAEIOU", sample_string))
print(vowels_output)


# 4)Use generator expression to print out only alphabets from the following
# string

# In[21]:


string = "123@Welc34ometo12@ac#adGild"
string_prnt = ''.join(char for char in string if char not in '123@4#')
string_prnt


# 5) Implement a function longestWord() that takes a list of words and returns
# the longest one.

# In[28]:


word= ["January","Feburary","March","April","May","June","July"]
def longestWord(arg_word):
    word_len = []  
    for n in word:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return [word_len[-1][1]]
print(longestWord(word))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





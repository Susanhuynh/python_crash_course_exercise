#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[3]:


s = "Hi there Sam!"
list(s.split())


# In[4]:


d = "Hi there dad!"
list(d.split())


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[5]:


planet = "Earth"
diameter = 12742


# In[6]:


print("The diameter of {} is {} kilometers.".format(planet, diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[8]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[11]:


lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[16]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[19]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[20]:


def domainGet(string):
    split = list(string.split("@"))
    return split[1]


# In[21]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[23]:


def findDog(string):
    split = list(string.split())
    for word in split:
        if word == "dog":
            return True


# In[24]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of timesthe word "dog" occurs in a string. Again ignore edge cases. **

# In[44]:


def countDog(string):
    i = 0
    split = string.split()
    for word in split:
        if word == "dog":
            i += 1
    return i


# In[45]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[46]:


seq = ['soup','dog','salad','cat','great']


# In[48]:


abc = list(filter(lambda word: word[0]=='s',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[52]:


def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 60+5:
            return "No Ticket"
        elif speed > (60+5) and speed <= (80+5):
            return "Small Ticket"
        else:
            return "Big Ticket"
    else:
        if speed <= 60:
            return "No Ticket"
        elif speed > 60 and speed <= 80:
            return "Small Ticket"
        else:
            return "Big Ticket"


# In[53]:


caught_speeding(81,True)


# In[54]:


caught_speeding(81,False)


# # Great job!

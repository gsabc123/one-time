#!/usr/bin/env python
# coding: utf-8

# 

# # python中的内置类型
# - str
# - list
# - tuple
# - set
# - dict

# ## list列表
# - 一组由有序数据做成的序列
#     - 数据就有先后顺序
#     - 数据可以不是一类数据
# - list的创建
#     - 直接创建，用中括号创建，内容直接用英文逗号隔开
#     - 使用list创建
#     - 列表包含单个字符串的时候是一个特例
#     - 

# In[1]:


# 直接赋值创建列表
L1 = [1,5,8,4,6,9]
# list内的数据可以不是一个类型
L2 = [8,7,5,1,6,4,3,"xiaojing","大拿"]

print(L1)
print(L2)


# In[3]:


# 创建列表的第二种方式
L3 = list()
print(L3)
print(type(L3))


# In[6]:


# list创建的特例演示
s = "Liu Dana"
# 想创建一个只包含s一个字符串的列表
L1 = list("Liu")
print(type(L1))
print(L1)


#!/usr/env python
#coding:utf8
'''
列表常用的增，删，查，改
'''
# list_var_name= ['元素1','元素2']  --> 元素可以试数字，字符串，列表嵌套列表

list_test = ['I','Love','Python']
print "Index0 is", list_test[0]  # 注意这里的 ,

list_a = [1,2,3,4,5,6,7,8,9]
print list_a[2:5]
print list_a[1::2] # 取偶数

########################################  增
# .append()
a = [1,2,3,]
b = [4,5,6]
a.append(b)
print a

# .extend()
a = [1,2,3,]
b = [4,5,6]
a.extend(b)
print a

# .insert()
a = [1,2,4,5]
b = 3
a.insert(2,b)
print a

########################################  删
# .pop()  括号是可选，不填写默认删除最后一个元素,pop 是根据索引来删除元素
a = [1,2,3,4]
a.pop(2)
print a

# .remove() 根据值来删除
a = [1,2,3,2,1]
a.remove(1)
print a

# .del()
a = [1,2]
del(a[0])
print a
del(a)
#print a

########################################  查
# 根据索引查询对应元素的值
a = [1,2,3]
print a[0]
# 根据值查询对应元素的索引
a = [1,2,3]
print a.index(3)

########################################  改
L = [1,2,3]
L[2]=4
print L

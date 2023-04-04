###  Check yourself  20.03    
# class Person:
#   __name = None
#   __last_name = None
#   __age = None
#   __email = None
#   def get_name(self):
#     return self.__name
#   def get_last_name(self):
#     return self.__last_name
#   def get_age(self):
#     return self.__age
#   def get_email(self):
#     return self.__email

#   def set_name(self, new_name):
#     self.__name = new_name
#     return self.__name
#   def set_last_name(self, new_last_name):
#     self.__last_name = new_last_name
#     return self.__last_name
#   def set_age(self, new_age):
#     self.__age = new_age
#     return self.__age
#   def set_email(self, new_email):
#     self.__email = new_email
#     return self.__email
  

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com







# class Person:
#   def __init__(self,name=None,last_name=None,age=None,email=None):
#     self.__name = name
#     self.__last_name = last_name
#     self.__age = age
#     self.__email = email

#   def get_name(self):
#     return self.__name

#   def set_name(self,name):
#     self.__name = name
#     return self.__name

#   def get_last_name(self):
#     return self.__last_name

#   def set_last_name(self,last_name):
#     self.__last_name = last_name
#     return self.__last_name

#   def get_age(self):
#     return self.__age

#   def set_age(self,age):
#     self.__age = age
#     return self.__age

#   def get_email(self):
#     return self.__email

#   def set_email(self,email):
#     self.__email = email
#     return self.__email

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com


# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_last_name(self):
#         return self.__last_name

#     def set_last_name(self, last_name):
#         self.__last_name = last_name

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         self.__age = age

#     def get_email(self):
#         return self.__email

#     def set_email(self, email):
#         self.__email = email

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com





# arr = []
# with open("27-B_demo.txt") as file:
#     for f in file.readlines():
#         arr.append(f.strip().split())
# arr = list(map(lambda i: [int(i[0]), int(i[1])], arr[1:]))

# sums = [0, 0, 0]
# for a, b in arr:
#     sums_new = [0, 0, 0]
#     for i in range(3):
#         sums_new[i] = max(sums[(i-a)%3] + a, sums[(i-b)%3] + b)
#     sums = sums_new

# print(sums[1])



# arr = []
# with open("27-B_demo.txt") as file:
#     for f in file.readlines():
#         arr.append(f.strip().split())
# arr = list(map(lambda i: [int(i[0]), int(i[1])], arr[1:]))

# sum = 0
# for a, b in arr:
#     if a % 3 == 0:
#         if b % 3 == 0:
#             continue
#         else:
#             sum += b
#     elif b % 3 == 0:
#         sum += a
#     else:
#         sum += max(a, b)

# print(sum)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     dummy = ListNode(0)
#     current = dummy
#     carry = 0
    
#     while l1 or l2 or carry:
#         sum = carry
#         if l1:
#             sum += l1.val
#             l1 = l1.next
#         if l2:
#             sum += l2.val
#             l2 = l2.next
            
#         carry = sum // 10
#         current.next = ListNode(sum % 10)
#         current = current.next
    
#     return dummy.next


"==========циклы=========="
# цикл - блок кода который обрабатывается несколко раз 
# for - цикл который работает с интерируемыми обьектами 
# цикл заканчивает свою работу когда



list1 = ['hello', 10, True, [1,2,3]]
for element in list1:
    print(element)

string1 = 'hello world'
for letter in string1:
    print(letter)
    

i = 1   
while i != 10:
    print('hello', i)    
    i = i + 1

i = 0 
while i:      #вообще ни разу не отработает потомучто 0 это False
    print('hello world')
    i = i + 1

'===========Ключевыу слова в циклах============='
# break - полностью останавливает цикл
# continue - переход к следущей итераций 

# for i in range(10):
#     if i == 3:
#         break
#     print(i)
    # 0 
    # 1
    # 2

for i in range(10):
    if i == 3:
        continue
    print(i)


num = input("Enter a num of integers seprated by whitespace: ")
num = num.split(" ") 
num = [int(x) for x in num]  
print(num)

temp_LICS = [num[0]] 
LICS = []  

for k in num[1:]:
    if k > temp_LICS[-1]:
        temp_LICS.append(k)  
    else:
        if len(temp_LICS) > len(LICS):
            LICS = temp_LICS
        temp_LICS = [k]

if len(temp_LICS) > len(LICS):
    LICS = temp_LICS

print("Length: ", len(LICS))
print("LICS: ", LICS)



num = input("Enter a num of integers: ")
num = num.split(" ")
num = [int(x) for x in num]
















# n = int(input("Enter size of the row: "))
# m = int(input("Enter size of the col: "))
# matrix = []



# for i in range(n):
# 	row = []
# 	for j in range(m):
# 		row.append("_")
# 	print(row)
# 	matrix.append(row)

# print(matrix)



















num = input("Enter a sequence of integers seperated by whitespace: ")

#將list轉為整數
lst1 = num.split(" ")
int_lst1 = []
for i in lst1:
	if i:
		int_lst1 = int_lst1 + [int(i)]

#找最小整數
lst2 = [] + [min(int_lst1)]

#輸入規則
#先設定i的範圍，當lst1後面的數大於前面的就將比較大的放入list1
#lst2每次放入後者，如果lst2最後一數不等於最大數，將它於list中刪除
for i in range (0,len(int_lst1)-1):
	if int_lst1[i+1] > int_lst1[i]:
		lst2 = lst2 + [int_lst1[i+1]]

	if lst2[len(lst2)-1]!=max(lst2):
		del lst2[len(lst2)-1]

#將答案輸出
print("Length: ", len(lst2))
print("LICS: ", lst2)

































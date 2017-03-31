#5-10检查用户名
current_name=['apple','banana','peach','meat']
new_name=['apple','banana','meat','sweet']
for i in new_name:
    i.lower()#
    if i in current_name:
        print(str(i)+" wrong! u can not use it")
    else:
        print(str(i)+" u can use it")

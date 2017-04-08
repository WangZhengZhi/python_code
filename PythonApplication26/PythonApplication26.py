option=input("welcome to use this\n1.find people\n2.creat new people\n3.delete people\n4.quit this soft\n ")
people={'wang':'18941142123'}
option=int(option)
if option==1:
    print(".........seaching.................\n")
    name=input("please input u want seach people's name")
    for name in people.values():
        print(name.title())
if option==2:
    print(".......creating.....................\n")
    name=input("please enter u creat name\n")
    tel=input("please enter u creat telphone\n ")
    people[name]=tel
    '''for k,v in people.items():
        print(k.title())
        print(str(v))'''#just for test this value and keys
if option==3:
    print(".......deleting...................\n")
    name=input("enter the name u want to delete\n")
    if name not in people.keys():
        print("u delete people not in this !!")
    
    if name in people.keys():
        del people[name]
        print("delete is successful!!!!\n")

    
    '''for k,v in people.items():
        print(k.title())
        print(str(v))'''#just for test v and k
if option==4:
    print(".......quiting.............\n")
    print("thaks for u use\n")
    

    
    


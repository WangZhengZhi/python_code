'''
def make_album(name,singer):
    id={'id_name':name,'id_singer':singer}
    return id
while True:
    input_name=input("please input u name or quit to quit")
    if input_name=='quit':
        break
    input_singer=input("please input u singer or enter quit to quit")
    if input_singer=='quit':
        break
    id_print=make_album(input_name,input_singer)
    print(id_print)
'''
'''
def users(name):
    for i in name:
        print("hello "+i)
usernames=['wang','li','hua']
users(usernames)
'''
#8.4.1
'''
unprint_modes=['a','b','c']
print_modes=[]
while unprint_modes:
    current_modes=unprint_modes.pop()
    print("the "+current_modes +" is printing\n")
    print_modes.append(current_modes)
print("this follow is already print")
for i in print_modes:
    print(i.title())
    '''
'''
def modes(unprint_modes,print_modes):
    while unprint_modes:
        current_modes=unprint_modes.pop()
        print("printing "+current_modes)
        print_modes.append(current_modes)
def show_print(print_modes):
    print("the following things had been print")
    for i in print_modes:
        print(i)
unprint_mode=['apple','peach','banana']
print_mode=[]
modes(unprint_mode,print_mode)
show_print(print_mode)
'''
'''
def print_modles(unprint_modles,complete_modles):
    while unprint_modles:
        current_modle=unprint_modles.pop()
        print("printing "+current_modle)
        complete_modles.append(current_modle)
def show(unprint_modles,complete_modles):
    print("those following print had been print")
    for i in complete_modles:
        print(i)
unprint_modle=['apple','banana','peach']
complete_modle=[]
print_modles(unprint_modle,complete_modle)
show(unprint_modle,complete_modle)
'''
#8.4.2
def print_modles(unprint_modles,complete_modles):
    while unprint_modles:
        current_modle=unprint_modles.pop()
        complete_modles.append(current_modle)
        print("the follwing is printing "+current_modle)

def show(unprint_modles,complete_modles):
    print("successful ! ")
    for i in complete_modles:
        print(i)
unprint_modle=['apple','peach','banana']
complete_modle=[]
print_modles(unprint_modle,complete_modle)
show(unprint_modle,complete_modle)






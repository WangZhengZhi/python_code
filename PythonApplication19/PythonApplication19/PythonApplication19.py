def print_model(unprint_models,complete_models):
    while unprint_models:
        current_model=unprint_models.pop()
        print(current_model+"is printing")
        complete_models.append(current_model)
def show(complete_models):
    for i in complete_models:
        print(i)
unprint_model=['apple','banana']
complete_model=[]
print_model(unprint_model,complete_model)
show(complete_model)
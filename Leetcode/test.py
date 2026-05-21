name = "Euron"
list_val = []
for i in range(1,len(name)+1):
    list_val.append(name[-i])

new_name = "".join(list_val)
print(new_name)
print(dir(new_name))

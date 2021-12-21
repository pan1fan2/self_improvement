mydict = {"name" : "Max", "age" : 28, "city" : "New York"}
print(mydict)

#mydict.popitem() # pop last inputted pair


# try :
#     print(mydict["lastname"])
# except:
#     print("error")

#### Copy dict #####
#mydict_copy = mydict # will point to the same rom address
#mydict_copy["email"] = "abc@xyz.com"
#print(mydict_copy)

# mydict_copy = dict(mydict)
# mydict_copy["email"] = "abc@xyz.com"
# print(mydict_copy)

#### Update dict #####
mydict_2 = {"name" : "Mary", "email" : "max@xyz.com"}
mydict.update(mydict_2)
print(mydict)
encrypt = input("what do you want to encrypt")
value = int(input("what is the shift value"))
nice = list(encrypt)
bleh = []
ron = ""
gf = ""
romo = []
raya = []
for i in nice:
    last_char = ord("Z") if i.isupper() else ord("z")
    cat = ord(i)
    bleh.append(cat)
run = [x+value for x in bleh]
for g in run:
    cat = chr(g)
    raya.append(cat)
for k in raya:
    gf +=k
print(gf)
file = open("message.txt","w")
file.write(gf)
file.close()
print("file has been created successfuly")
question = input("do you want to convert the message back yes for yes no for no").capitalize()
if question == "Yes":
    vala = [y-value for y in run]
    for item in vala:
        dog = chr(item)
        romo.append(dog)
    for n in romo:
        ron+= n
    print(ron)
if question == "No":
    print("print thank you for using the app")
    
    



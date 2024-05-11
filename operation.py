
# Function to create the laptop dictionary (dic)
def dic():
    file = open("laptop.txt","r")
    lap_dic = {}
    laptop_id = 1

    for line in file:
        line = line.replace("\n","")
        lap_dic.update({laptop_id:line.split(",")})
        laptop_id =laptop_id+ 1
    return lap_dic


def validlp_id():
    lap_dic= dic()

    valid_id = int(input("Kindly enter the ID number of the item you would like to purchase: "))
    while valid_id <= 0 or valid_id >len(lap_dic):
                    print("Kindly provide a valid ID\n")
                    valid_id = int(input("Kindly enter the ID of the item you want"))  
    return valid_id      

def validlp_quantity():
    
    quantity_of_item = int(input("Kindly enter the quantity of the items you require: "))
    
    while quantity_of_item <= 0:
        print("Apologies, The quantity of the items you entered isn't available")
        quantity_of_item = int(input("Kindly enter the quantity of the items you require: "))
    return quantity_of_item

def file_write(valid_id,quantity_of_item):
        lap_dic = dic()
        lap_dic[valid_id][3] = int(lap_dic[valid_id][3]) - int(quantity_of_item)
        file = open('laptop.txt','w')
        for values in lap_dic.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
        file.close()


def print_command(user_dic,name,phone):     
                                  
                    print("S.N \t Name \t\t Brand\t \tquantity   Price    Processor    Graphics")
                    a = 1
                    file = open('laptop.txt','r')
                    for line in file:
                            print(a,"\t"+line.replace(",","\t"))
                            a+=1
                    file.close()
                    print("---------------------------------------------------------------------------------------------")
                    print("\n\n\n---------------------------------------------------------------------------------------")
                    print("\t\t\t\tINVOICE")
                    print("---------------------------------------------------------------------------------------")
                    print("\t\t\tItti Electronics")
                    print("\t\t\tJhamsikhel,Lalitpur, Nepal")
                    print("---------------------------------------------------------------------------------------")

                    print("\nName of the user: "+str(name))
                    print("Phone number of the user: "+str(phone))
                    print("\n")
                    print("---------------------------------------------------------------------------------------")
            
                    print("---------------------------------------------------------------------------------------")
                    print("\n\nProduct\t\tQuantity\tPer Price\tAmount\t\tTotal\n")
                    
                    for i in user_dic.values():
                            print(str(i[0])+str(i[1])+"\t"+"\t"+str(i[2])+"\t"+str(i[3])+"\t"+str(i[4]))
                       

def sell_validlp_id():
    lap_dic= dic()
    valid_id = int(input("Kindly enter the ID of the items you wish to sell "))
    while valid_id <= 0 or valid_id >len(lap_dic):
                    print("Please provide a valid ID\n")
                    valid_id = int(input("Kindly enter the ID of the items you wish to sell "))  
    return valid_id

def sell_validlp_quantity():
    quantity_of_item = int(input("Kindly provide us with the quantity of the items you want to sell: "))
    
    while quantity_of_item <= 0:
        print("The quantity of items you entered cannot be sold. Kindly enter a valid quantity")
        quantity_of_item = int(input("Kindly provide us with the quantity of the items you wish to sell: "))
    return quantity_of_item


def sell_file_write(valid_id,quantity_of_item):
        lap_dic = dic()
        lap_dic[valid_id][3] = int(lap_dic[valid_id][3]) + int(quantity_of_item)
        file = open('laptop.txt','w')
        for values in lap_dic.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
        file.close()
        
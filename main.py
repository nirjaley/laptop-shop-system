from read import *
from operation import *
from write import *

print("                             Itti Electronics")
print("                        Jhamsikhel, Lalitpur, Nepal")
print("--------------------------------------------------------------------------")
here_loop = True

while here_loop == True:
    print("Press 1 to purchase")
    print("Press 2 to sell items")
    print("Press 3 to exit")
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        name, phone = username_phone()
        lap_dic= dic()
        
        user_dic = {}
        more = True
        while more == True:
            print(display_file())
            valid_id = validlp_id()
            quantity_of_item =  validlp_quantity()

            file_write(valid_id,quantity_of_item)

            item_name = lap_dic[valid_id][0]
            
            quantity = int(quantity_of_item)
            price_per = lap_dic[valid_id][2]
            price_chosen = lap_dic[valid_id][2].replace("$","")
            total = int(price_chosen)*int(quantity)
            

            user_dic[valid_id]=(item_name,quantity,price_per,price_chosen,total)
            

            again = input("Do you want to browse more items?(Yes/No)").lower()
            if again == "Yes":
                more = True
            else:
                print("13% vat has been added to your total purchase.\n")
                total = 0
                final_total = 0
                
                vat_amount = total*(13/100)
                final_total = total+vat_amount
                print_command(user_dic,name,phone)
                invoice(user_dic,name,phone)
                more = False

        
    elif user_input == 2:
        
        name, phone = username_phone()
        lap_dic = dic()
        
        user_dic = {}
        more = True
        while more == True:
            print(display_file())
            valid_id = sell_validlp_id()
            quantity_of_item =  sell_validlp_quantity()

            sell_file_write(valid_id,quantity_of_item)

            item_name = lap_dic[valid_id][0]
            
            quantity = int(quantity_of_item)
            price_per = lap_dic[valid_id][2]
            price_chosen = lap_dic[valid_id][2].replace("$","")
            total = int(price_chosen)*int(quantity)
            

            user_dic[valid_id]=(item_name,quantity,price_per,price_chosen,total)
            

            again = input("Do you want to browse more items?(Yes/No)").lower()
            if again == "Yes":
                more = True
            else:
                print("13% vat has been added to your total cost.\n")
                total = 0
                shipping_cost = 800
                final_total = 0
                
                final_total= total+shipping_cost
                print_command(user_dic,name,phone)
                invoice(user_dic,name,phone)
                more = False
        
    elif user_input == 3:
        print("Thank you for your order, Please visit us again!")
        here_loop = False
    
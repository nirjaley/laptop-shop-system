def invoice(user_dic,name,phone):
        file_name =  str(name) + ".txt"
                    
        with open(file_name,'w') as purchased_file:
                        purchased_file.write("\n\n\n-----------------------------------------------------------------------------------------\n")
                        purchased_file.write("\t\t\t\t   Invoice\n")
                        purchased_file.write("-----------------------------------------------------------------------------------------\n")
                        purchased_file.write("\t\t\t\t   Itti Electronics\n")
                        purchased_file.write("\t\t\t  Jhamsikhel, Lalitpur, Nepal\n")
                        purchased_file.write("------------------------------------------------------------------------------------------\n\n")
                        purchased_file.write("\nName of the user: "+str(name)+"\n")
                        purchased_file.write("Phone number of the user: "+str(phone)+"\n")
                        purchased_file.write("\n")
                        purchased_file.write("-----------------------------------------------------------------------------------------\n")
                        
                        purchased_file.write("-----------------------------------------------------------------------------------------\n")
                        purchased_file.write("\n\nProduct\tQuantity\tPer Price\tAmount\t\tTotal\n")
                        for i in user_dic.values():
                                purchased_file.write(str(i[0])+str(i[1])+"\t"+str(i[2])+"\t"+str(i[3])+"\t"+str(i[4])+"\n")
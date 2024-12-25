def generate_and_save_phone_numbers(filename):
    with open(filename, "w") as file:
        for i in range(100000000, 1000000000): # 10 digits
            file.write(f"0{i}\n")
        
        for i in range(1000000000, 10000000000): # 11 digits
            file.write(f"0{i}\n")

generate_and_save_phone_numbers("phonenumber.txt")

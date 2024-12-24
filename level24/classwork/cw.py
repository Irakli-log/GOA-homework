
print("registration; ")


reg_username = input("შეიყვანეთ სახელი: ") 
reg_password = input("შეიყვანეთ პაროლი: ")

print("login: ")

log_name = input(" chawere shenu saxeli: ")
log_pasword = input("chawere shemi paroli: ")


while log_name != reg_username or log_pasword != reg_password:
    print("araswori paroli an saxelia chaweret tavidan: ")
    log_name = input("gtxov chawero swori saxeli  ")
    log_pasword = input("gtxov chawero swori paroli ")


print("welcome")
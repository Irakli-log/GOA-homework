string_var = "343" 
int_var = 238          
float_var = 16.3


string_var = "567"      

string_in_to_int = int(string_var)


int_to_float = float(int_var)


float_to_string = str(float_var)


print("სტრინგის ცვლადი: ", string_var)
print("ინტეჯერში გარდაქმნილი: ", string_in_to_int, "მისი მონაცემთა ტიპი: ", type(string_in_to_int))

print("\nინტეჯერის ცვლადი: ", int_var)
print("ფლოატში გარდაქმნილი: ", int_to_float, "მისი მონაცემთა ტიპი: ", type(int_to_float))

print("\nფლოატის ცვლადი: ", float_var)
print("სტრინგში გარდაქმნილი: ", float_to_string, "მისი მონაცემთა ტიპი: ", type(float_to_string))

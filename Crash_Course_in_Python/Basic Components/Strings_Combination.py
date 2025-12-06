first_name = "Annabelle"
last_name = "Higgins"

#Method 01: Using + operator
full_name = first_name + " " + last_name
print(full_name)

#Method 02: Using f-strings (formatted string literals) - Preferred
full_name_fstring = f"{first_name} {last_name}"
print(full_name_fstring)

#Method 03: Using str.format() method
full_name_format = "{0} {1}".format(first_name, last_name)
print(full_name_format)

#Method 04: Using join() method
full_name_join = " ".join([first_name, last_name])
print(full_name_join)



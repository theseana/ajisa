# poulstar
string1 = "@#$$^%^*Poulstar#@$%#$%#$%"   
new_string1 = string1.strip('@#$%^*').lower()
print(new_string1)


# poulstar
string2 = "SDFsdf SDfsdf sdfasdf sadfsdf Poulstar aPFDSAF DSF " 
new_string2 = string2.split()[4].lower()
print(new_string2)


# "$$$$poulstar$$$$"
string3 = "****POULSTAR****"  
new_string3 = string3.lower().replace("*", "$")
print(new_string3)

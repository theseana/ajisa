def get_info():
    text = input('Enter your information:(name family age)\n')
    return text.split()


info = get_info()

template = f"""Name: {info[0]}
Last: {info[1].upper()}
Age:  {info[2]}
*****************
"""
print(template)
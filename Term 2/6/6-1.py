import turtle as tr


shape = input("Enter which shape Square/Triangle?(s/t) ")

if shape == 't':
    for i in range(3):
        tr.fd(150)
        tr.lt(120)
        
if shape == 's':
    for i in range(4):
        tr.fd(150)
        tr.lt(90)

tr.done()
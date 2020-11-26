a = ['amirreza', 'javad', 'setayesh', 'artin', 'iliya']
print(a[4])
print(a[1:4])
print(a[-1])

a.append('sina')
a.append('iliya')
a.append('iliya')
a.append('iliya')
a.append('iliya')

print(a)

# تعداد تکرار رو مشخص میکند
print(a.count('iliya'))

# شماره پلاک بر میگردونه
print(a.index('iliya'))

a.insert(3, 'Hazhir')
print(a)

print(a.pop())
print(a)

popped = a.pop(3)
print(popped)
print(a)

# به ترتیب 
a = [1, 5, 8, 97, -1,45, 12,1, 51]
a.sort()
print(a)
b = ['c', 'Z', 'z', 'A', 'a']
b.sort()
print(b)

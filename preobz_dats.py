from datetime import datetime
text = '1986-05-22'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y 
print(diff)

print(z)
newdate = datetime.strftime
print(newdate)
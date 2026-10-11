f = open('data.txt', 'r+')

# read the entire file
data = f.readlines()

#Print the data
print(data)

#write to the file
f.write(input("Say your feedback:"))

#close the file
f.close()
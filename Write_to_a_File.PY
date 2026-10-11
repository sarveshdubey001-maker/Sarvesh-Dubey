# Step 1: Open the file in write mode
f = open("Data1.txt", "w")

# Step 2: Write some content
f.write("Practising Python file handling.\n")
f.write("This is my first file handling python program\n")
f.write(input("write more content:"))

f.close()

print("Content written to data1.txt successfully!")
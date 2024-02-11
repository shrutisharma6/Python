import  os
file1 = open('test.txt', 'w')
file1.write("Write testing 2")
for i in range(5):
    file1.write("*")
file1.close()

file2 = open('test.txt','r')
print(file2.read())
file2.close()

file3 = open('test.txt', 'a')
file3.write("12345")
file3.close()

file2 = open('test.txt','r')
print(file2.read())
file2.close()

os.remove("test.txt")

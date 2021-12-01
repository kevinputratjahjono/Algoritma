#write
def write(jadi):
    
    f = open("kepo.txt", "w")
    
    f.write(jadi)
    
    f.close()
    
#read
def main():
    
    f = open("kepo.txt", "r")
    if f.mode == "r":
        contents = f.read()
    print (contents)
    
x = str(input("Nama: "))
y = str(input("Umur: "))
z = str(input("Alamat: "))
q = str(input("Email: "))
o = str(input("Dosen Wali: "))
jadi = ("{}\n{}\n{}\n{}\n{}\n". format(x,y,z,q,o))

print("\n")
print("Loading. . . ")
write(jadi)
print("")
main()

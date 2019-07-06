def write_to_file():
    with open("demo.txt","w") as f:
        f.write("Writing for file")
        l=["neha \n ","garde"]
        f.writelines(l)

def read_from_file():
    with open("demo.txt","r") as f:
        #f.read()
        for line in f:
            print(line)
            #break

        l=f.readlines()

def append_file():
    with open("demo.txt","a+") as f:
        f.write("\n Hello Neha. How r u doing today?")
        f.seek(0)
        print(f.read())


if __name__ == '__main__':
    write_to_file()
    append_file()
    #read_from_file()
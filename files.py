def write_to_file():
    with open("demo.txt","w") as f:
        f.write("Writing for file")
        l=["neha \n ","garde"]
        f.writelines(l)


if __name__ == '__main__':
    write_to_file()
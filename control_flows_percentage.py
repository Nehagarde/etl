if __name__ == '__main__':
    percentage = int(input("Enter percentage: "))

    if 100 >= percentage >= 80:
        print("Distinction")
    elif 79 >= percentage >= 70:
        print("First class")
    elif 69 >= percentage >= 60:
        print("Second class")
    elif 59 >= percentage >= 50:
        print("Pass")
    else:
        print("Fail")
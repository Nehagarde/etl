d = {'0':'0','1':'9','2':'8','3':'7','4':'6','5':'5','6':'4','7':'3','8':'2','9':'1','*':'*'}

if __name__ == '__main__':
    s1 = input("Enter 1st string:")
    s2 = input("Enter 2nd string:")

    s1_list = [d[i] for i in list(s1)]
    s1 = "".join(s1_list)
    s2_list = [d[i] for i in list(s2)]
    s2 = "".join(s2_list)

    print(s1)
    print(s2)
    eval(s1)
    eval(s2)
    res = eval(s1)+eval(s2)
    print(res)
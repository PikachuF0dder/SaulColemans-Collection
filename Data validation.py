name = input("name: ")

def strValid(string,mini=3,maxi=20):
    if string and isinstance(string,str) and mini <= len(string) <= maxi:
        print("Valid ")
    else:
        print("Invalid ")

strValid(name)

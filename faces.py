def main():
    user = input("how are you feeling today? ")
    convert(user)
    
def convert(user):
    user = user.replace(":)","🙂")
    user = user.replace(":(","🙁")
    user = str(user)
    return print(user)
main()
user = input("Please say a greeting? ")
user = str(user).lower()
if "hello" in user:
    print("$0")
elif user.find("h") == 0:
    print("$20")
else:
    print("$100")
import getpass

database = {"Payal":"1304","DikshaW":"1207","Mitali":"1907","DikshaM":"0411","Shrutika":"0511"}
username = input("Enter your username : ")
password = getpass.getpass("Enter your password : ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again :")
        break
print("Verified")

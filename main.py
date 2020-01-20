import pyssword
from getpass import getpass

if __name__ == "__main__":
    pwd = getpass("Insert the \"master password\">>>")
    det = input("Insert the \"detail modifier\">>>")
    print(pyssword.generate(pwd, det))
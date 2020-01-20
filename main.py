import pyssword
from getpass import getpass

if __name__ == "__main__":
    pwd = getpass("Inserisci la \"master password\">>>")
    det = input("Inserisci il \"dettaglio\">>>")
    print(pyssword.generate(pwd, det))
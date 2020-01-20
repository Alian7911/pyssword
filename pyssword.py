def __isconsonant(char: str) -> bool:
    """Returns a bool that indicates whether or not a char is a consonant"""

    if len(char) > 1:
        raise Exception("Only a single character is allowed")
    return char.lower() in "bcdfghjklmnpqrstvwxyz"

def __isvowel(char: str) -> bool:
    """Returns a bool that indicates whether or not a char is a vowel"""

    if len(char) > 1:
        raise Exception("Only a single character is allowed")
    return char.lower() in "aeiou"


def generate(master: str, detail: str = "") -> str:
    """
        Generates a password using a master password and a string to diversify the outcome.

        PARAMETERS
        ----------
        master: str
            Master password.
        detail: str
            Detail string.

        RETURN
        ------
        The generated password.
    """
    
    tmp = ''
    for i in range(len(master)):
        char = master[i]
        if __isconsonant(char) and (i+1) % 3 == 0:
            tmp += char.upper()
        elif __isvowel(char) and (i+1) % 2 == 0:
            tmp += char.upper()
        else:
            tmp += char.lower()
    for i in range(len(detail)):
        char = detail[i]
        if i == 0 or i == 1:
            tmp += char
        elif i == len(detail) - 1 or i == len(detail) - 2:
            tmp += char
    return tmp

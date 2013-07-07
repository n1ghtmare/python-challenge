import string

def decode(text):
    for i, c in enumerate(text):
        if c.isalpha():
            listed_text = list(text)
            listed_text[i] = string.lowercase[(string.lowercase.index(c) + 2) - 26]
            text = "".join(listed_text)
    return text

if __name__ == "__main__":
    scrambled_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print decode(scrambled_text)
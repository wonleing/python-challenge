#!/usr/bin/python
ori="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
cov=""
for char in ori:
    if ord(char) in range(97,121):
        ichar = chr(int(ord(char))+2)
    elif ord(char) in range(121,123):
        ichar = chr(int(ord(char))-24)
    else:
        ichar = char
    cov += ichar
print cov

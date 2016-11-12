def accum(s):
    L = list(s.lower())
    str = ""
    index = 0
    for i in L:
        str +=i.upper()+index*i+"-"
        index+=1
    return str[:-1]

## Function with the use of enumerate() function in Python

def accum_enum(s):
    L = list(s.lower())
    str = ""

    for i,char in enumerate(L):
        str +=char.upper()+char*i+"-"

    return str[:-1]

#print (accum_enum("ZpglnRxqenU"))

def accum_join(s):
    return "-".join([c.upper + (c.lower * i)for i,c in enumerate(s)])

print (accum_enum("ZpglnRxqenU"))
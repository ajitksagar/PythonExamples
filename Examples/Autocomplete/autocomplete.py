def autocomplete(input_,dictionary):
    L = []
    #filterList = []
    count = 0

    input_ = ''.join(e for e in input_ if e.isalpha())

    # def letterStr(x):
    #     str=''.join(e for e in x if e.isalpha())
    #     if str and not str.isspace():
    #         return str

    # filterList = filter(None,map(letterStr, dictionary))

    #print len(filterList)
    # for str1 in dictionary:
    #     str1 = ''.join(e for e in str1 if e.isalpha())
    #     if str1 and not str1.isspace():
    #      filterList.append(str1)


    # if  not filter(None,map(letterStr, dictionary)):
    #   L.append('Nopesville')
    # else:
    for str in dictionary:
            # original_str = str
            # str = ''.join(e for e in str if e.isalpha())
            if str.lower().startswith(input_) and count < 5:
                L.append(str)
                count += 1

    return L


print (autocomplete("aj",["",'']))
# print (autocomplete("aj",["*/#$2","@#$%^&[]"]))
print (autocomplete("#aj",['$%#AJit','abhi','[]!aj2shyam','2aja','Ajat','bhai','aJabhau','hello','ajihi']))


def autocomplete1(input_,dictionary):
    L = []
    filterList = []
    count = 0

    def letterStr(x):
        str=''.join(e for e in x if e.isalpha())
        if str and not str.isspace():
            return str

    filterList=map(letterStr,dictionary)

    return filterList

# print (autocomplete1("aj",[]))
# print (autocomplete1("aj",["*/#$2","@#$%^&[]"]))
print (autocomplete1("aj",['$%#AJit','abhi','[]!aj2shyam','2aja','Ajat','bhai','aJabhau','hello','ajihi']))
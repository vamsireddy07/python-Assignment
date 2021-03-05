def match_symbol(chemicals, symbols):
    import re
    join = []

    for s in symbols:
        for c in chemicals:
            r = re.search(s, c)
            if r:
                join.append(re.sub(s, "[{}]".format(s), c))

    return join		    


print (match_symbol(chemicals, symbols)) 
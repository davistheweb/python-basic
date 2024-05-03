def checkname(name):
    if (name.lower() == 'davis'):
        return True

    else:
        return False
    
check = checkname('DavIS')

print(check)
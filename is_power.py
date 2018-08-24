def is_power(a,b):
    if a > b:
        print a,b,"branch 1"
        return is_power(a/b, b)
    elif a < b:
        print a,b,"branch 2"
        return False
    else:
        print a,b,"branch 3"
        return True


print is_power(59049,3)

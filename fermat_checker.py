def check_fermat(a,b,c,n):
    a_to_n = int(a) ** int(n)
    b_to_n = int(b) ** int(n)
    c_to_n = int(c) ** int(n)
    if (int(c_to_n) == (int(a_to_n) + int(b_to_n))):
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'Yeah, sorry, Fermat\'s still right.'

def prompty():
    print 'Do you think you can fuck with Fermat\'s Last Theorem?\n'
    prompt = 'a?\n'
    a_fermat = raw_input(prompt)
    prompt = 'b?\n'
    b_fermat = raw_input(prompt)
    prompt = 'c?\n'
    c_fermat = raw_input(prompt)
    prompt = 'n?\n'
    n_fermat = raw_input(prompt)
    print n_fermat

    if (int(n_fermat) <= 2):
        print 'You need an n value greater than 2, genius.'
    else:
        check_fermat(a_fermat,b_fermat,c_fermat,n_fermat)

prompty()

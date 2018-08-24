def eval_loop(input):
    while True:
        line = raw_input('> ')
        if line == 'done':
            break
        print eval(line)
    print 'Done!'

eval_loop(input)

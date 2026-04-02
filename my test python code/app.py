def print_info(header,info):
    print('*******{0}*******'.format(header))
    for key,value in info.items():
        print(key,value)
    print('*******end of information******')
print_info('Using global function',globals())
print(__name__)
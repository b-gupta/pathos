import sys

def perm_x(s, i):
    if len(s) == i:
        print s
        return
    
    if s[i] == 'x':
        tokens = s.partition('x')
        perm_x(tokens[0] + '0' + tokens[2], i+1)
        perm_x(tokens[0] + '1' + tokens[2], i+1)
    else:
        perm_x(s, i+1)

if __name__ == '__main__':
    args = sys.argv[1:]
    perm_x(args[0].lower(), 0)

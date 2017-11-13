def flip_line(s):
    # return s[::-1]
    s1 = str()
    for i,x in enumerate(s):
        s1 = x+s1
    return s1

print(flip_line("hello, world"))

s = input('String? ')
if s.count('h') == 0:
    print("There are NO any 'h' inside")
elif s.count('h') <= 2:
    print("Not enough 'h'-s to replace")
else:
    h_first = s.find('h')
    h_last = s.rfind('h')
    s_beg = s[:h_first + 1]
    s_end = s[h_last:]
    s_middle = s[h_first +1:h_last]
    s_middle = s_middle.replace('h', 'H')
    print(s_beg + s_middle + s_end)


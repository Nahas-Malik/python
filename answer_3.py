def find_longest_string(strings):
    if not strings:
        return ""
    return max(strings, key=len)
print(find_longest_string(['cat','car','fear','center']))
print(find_longest_string(['cat','dog','shatter','donut','at','todo']))


## Given an input string, reverse the string word by word.

def reverseWords(s):
    st = s.strip().split(' ')
    st.reverse()
    return (' '.join(list(filter(lambda a: len(a) > 0, st))))

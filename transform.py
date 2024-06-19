def is_diff_one(str1, str2):
    if len(str1) != len(str2):
        return False

    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count = count + 1

    if count == 1:
        return True

    return False


potential_ans = []


def transform(english_words, start, end, count):
    global potential_ans
    if count == 0:
        count = count + 1
        potential_ans = [start]

    if start == end:
        print (potential_ans)
        return potential_ans

    for w in english_words:
        if is_diff_one(w, start) and w not in potential_ans:
            potential_ans.append(w)
            transform(english_words, w, end, count)
            potential_ans[:-1]
    
    return None
    

english_words = set(['dog','dot', 'cat', 'hot', 'hog', 'eat', 'dug', 'dig','hat'])
transform(english_words, 'dog', 'hat', 0)


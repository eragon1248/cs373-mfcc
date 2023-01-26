

def railcipher(word, key):
    ret = ''
    for mod in range (key):
        cur = mod
        while cur<len(word):
            ret+=word[cur]
            cur+=key
    return ret

print(railcipher('helloworld'))
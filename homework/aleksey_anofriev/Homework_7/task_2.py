words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

keys = list(words.keys())
i = 0

while i < len(keys):
    key = keys[i]
    count = words[key]
    repeated = key * count
    print(repeated)
    i += 1

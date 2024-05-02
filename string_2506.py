words=["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]
allowed="fstqyienx"
print(len(words))
x=len(words)
for word in words:
    for wor in word:
        if wor not in allowed:
            x=x-1
            break
print(x)

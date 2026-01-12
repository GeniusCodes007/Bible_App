word = "iwwu iiiu oowi "

new_word = word.replace(" ", "_")
print(new_word)
if " " in word:
    print("Found it")
count = 1
for x in new_word:
    if x == "_":
        print("Found it ", count)
        print("the position is ", new_word.index("_"))
        count += 1
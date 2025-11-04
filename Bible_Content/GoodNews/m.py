import pandas as pan
try:
    bn = pan.read_csv('chapterOne.csv', header=None)
    #bn.columns = ['verse', 'verse content']

    with open('chapterOne.csv', 'r') as chap_1:
        for index, line in enumerate(chap_1.readlines()):
            print(f"{index+1}: {line}")
except Exception as e:
    print(f"The issue is {e}")
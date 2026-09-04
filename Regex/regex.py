import re
text = "python is powerfull, python is easy, python is popular"
findWord = "python"

find = re.findall(findWord, text)

print(f"find the words is {findWord}")
print(f"word find = {len(find)}")


string = "the price is item 100 tk, is so high, out income is just 14000 tk, in 1 month, just 1 kg mango price is 80 tk"


find = re.findall('\d+', string)
print(f"find the number is= {find}")

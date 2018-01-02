file = open('Thor.txt', 'r')
content = file.read()

import re
words = re.split(' ', content)
num_words = len(words)

num_sentences = len(re.findall(r'\.', content))

print("Paragraph Analysis")
print("-------------------------")
print("Approximate word count: " +str(num_words))
print("Approximate sentence count: " +str(num_sentences))
print("Average Letter Count:" +str(round(len(content)/num_words,2)))
print("Average sentence length:" + str(round(num_words/num_sentences,2)))

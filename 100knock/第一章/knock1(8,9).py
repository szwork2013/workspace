# -*- coding: utf-8 -*-
import random
#com
#0:暗号化
#1:復号化
def cipher(message,encode):
	moji_list=list(message)
	moji_list2=[]
	#string=[]
	#moji_list=list(message)
	if encode==0:
		for moji in moji_list:
			if moji.islower():
				moji_list2.append(unichr(219-ord(moji)))
			else:
				moji_list2.append(moji)
	else:
		for moji in moji_list:
			if moji.islower():
				moji_list2.append(unichr((ord(moji)-219)*(-1)))
			else:
				moji_list2.append(moji)
	return moji_list2

def q_1_8(message):
	moji_list=cipher(message,0)
	text="".join(moji_list)
	print text
	moji_list2=cipher(text,1)
	text="".join(moji_list2)
	print text

	return 1

def q_1_9(message):
	listWord=message.split(" ")
	wordChanged=""
	#print listWord
	for word in listWord:
		if len(word) > 4:

			wordHead=word[:1]
			wordTail=word[len(word)-1:len(word)]
			wordBody=word[1:len(word)-1]
			listWordBody=list(wordBody)
			random.shuffle(listWordBody)
			wordBody="".join(listWordBody)
			print wordHead+wordBody+wordTail,
		else:
			print word,

	return 1

print "Q8."
q_1_8("Let us never negotiate out of fear. But let us never fear to negotiate.")
print "Q9."
q_1_9("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")

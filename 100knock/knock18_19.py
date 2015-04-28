# -*- coding: utf-8 -*-

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
	print moji_list
	#moji_list3=cipher(moji_list2,1)
	#print moji_list3
	#for moji in moji_list:
	#	cipher(moji)
	return 1

def q_1_9(message):
	return 1

q_1_8("Let us never negotiate out of fear. But let us never fear to negotiate.")
q_1_9("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")

import os
import math
import string
string1=string.ascii_lowercase
string1=string1+'0123456789_'
list1=[]
textfile=[]
dictlist=[]
string_list=[]
def readdict(readme):
	dict1={}
	stringmat=[]
	for word in readme.split():
		word=word.lower()
		for j in word:
			if j not in string1:
				pos=word.find(j)
				word=word[:pos]+word[pos+1:]
		stringmat.append(word)
		if word not in dict1:
			dict1.update({word:1})
		else:
			dict1[word]+=1
	return (dict1,stringmat)
def dictlis():
	loc=os.getcwd()
	for filename in os.listdir(loc):
		if filename.endswith('.txt'):
			textfile.append(filename)
	for filename in textfile:
		readme=open(filename,'r').read()
		r=readdict(readme)
		r1=r[1]
		r=r[0]
		dictlist.append(r)
		string_list.append(r)
	return (dictlist,string_list)
def bagofwords(dictlist):
	inp=float(input('enter percentage'))
	for i in range(len(dictlist)):
		euclid1=0
		for j in range(i+1,len(dictlist)):
			euclid2=0
			dotprod=0
			if(i!=j):
				i1=dictlist[i]
				j1=dictlist[j]
				for k in i1:
					if k in j1:
						dotprod=dotprod+(i1[k]*j1[k])
					euclid1=euclid1+(i1[k]**2)
				for k1 in j1:
					euclid2=euclid2+(j1[k1]**2)
				euclid1=math.sqrt(euclid1)
				euclid2=math.sqrt(euclid2)
				cos_θ = ((dotprod)/(euclid1*euclid2))*100
				if cos_θ>=inp:
					print(round(cos_θ,3),'"plagiarised"',textfile[i],textfile[j])
				else:
					print(round(cos_θ,3),'"no plagiarism"',textfile[i],textfile[j])

	


dictlist=dictlis()
string_list=dictlist[1]
dictlist=dictlist[0]
bagofwords(dictlist)
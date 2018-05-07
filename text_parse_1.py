import string
import nltk

form nltl.corpus import stopwords

def sort_it_1(fart):
    lst=list(fart.keys())
    lst.sort()
    print('the keys:\n',lst,'\n')
    for key in lst:
        print(key,fart[key])

def sort_by_value(fart):
    lst=list()
    for key,val in list(fart.items()):

        lst.append((val,key))
        lst.sort(reverse=True)
    for key,val in lst:
        print(key,val)


##location=r'C:\Users\Crystal\Desktop\test.txt'
location=r'C:\Users\Crystal\Desktop\Resume_parse.txt'



with open (location) as my_file:
    lines =my_file.read()
##    print('raw read:\n',lines,'\n')
    lines=lines.split()

    lines.sort()
print('sorted word list:\n',lines,'\n')


fart=dict()
for word in lines:
    if word not in fart:
        fart[word]=1
    else:
        fart[word]+=1

##print ('word count dict:\n',fart,'\n')

#sort_it_1(fart)
sort_by_value(fart)



R=['the','on','for','is','to','that','in','a','with','of','and','this','as','at']
R2=['*','&','-','/','!','@','_']
setA=set(R+R2)

setB=set(lines)

print('set R:\n',setA,'\n')
print('sorted word list:\n',lines,'\n')
print('set B:\n',setB,'\n')

no_the=setB.difference(setA)

print('without the:\n', no_the,'\n')

stuff_removed=list(no_the)

print('stuff removed:',stuff_removed)


final=dict()
for c in stuff_removed:
    if c not in final:
        final[c]=1
    else:
        final[c]+=1

print('final dict:',final)
sort_by_value(final)

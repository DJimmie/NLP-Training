import nltk
from nltk.book import *
print(f'---------\n')

def searching_text(text,words):

    print(f'{text}\n')
    result=text.concordance(words,width=79, lines=100)

    print(f'{result}\n\n')

    result=text.similar(words)
    print(f'\nSIMILAR\n{result}')

    t3words=['Adam','Eve','Abraham','God','Pharaoh','Moses','Joseph','poverty']
    t7words=['money;,taxes','poverty','investment','President']
    text.dispersion_plot(t3words)

def counting_vocab(text):

    # Text Length
    print(f'Text Length:{len(text)}')

    # Sorted Set of disting words
    print(f'Sorted Set\n{sorted(set(text))}')

    print(f'\nNumber of distinct words:{len(sorted(set(text)))}')

    # % of distinct words. A measure of the lexical richness of the text. Also know as lexical diversity.
    a=len(set(text)) / len(text)
    print(f'\nThe number of distinct words is just {round(a*100)}% of the total number of words')

    

    


## MAIN-----------------------------MAIN-----------------------------MAIN
searching_text(text3,'Egypt')

counting_vocab(text3)



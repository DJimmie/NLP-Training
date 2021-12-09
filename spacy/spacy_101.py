
# %%
import spacy
from spacy import displacy

def tokenization(s):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(s)
    for token in doc:
        print(token.text, token.pos_, token.dep_)


def parts_of_speech(s):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(s)

    for token in doc:
        print(f'text: {token.text}\nlemma: {token.lemma_}\nPOS: {token.pos_}\nTag: {token.tag_}\nDEP: {token.dep_}\nShape{token.shape_}\nIs Alpha: {token.is_alpha}\nIs stop word: {token.is_stop}')
        print('\n\n')


def named_entities(s):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(s)

    displacy.serve(doc, style="ent")

    return [(ent.text,ent.label_) for ent in doc.ents]

def entity_relationship(s):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(s)

    displacy.render(doc, style='ent')

# %%
parts_of_speech('The heating element failed while going cold.')

# %%
tokenization('The heating element failed while going cold.')

# %%
ner=named_entities('The heating element failed while going cold.')

print(ner)


# %%

entity_relationship('The heating element failed while going cold.')

# %%

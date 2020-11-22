
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
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)


def named_entities(s):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(s)

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
named_entities('Jim is from Philadelphia.')


# %%

entity_relationship('The heating element failed while going cold.')

# %%

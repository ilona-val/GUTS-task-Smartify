import lemminflect
import random
import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator

# def download_english_small_model():

try:
    nlp = spacy.load('en_core_web_sm')
except OSError as e:
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')
nlp.tokenizer.rules = {key: value for key, value in nlp.tokenizer.rules.items() if "'" not in key and "’" not in key and "‘" not in key}

def smartify(sentence):
    """ Performs WordNet lookups on some words from the input sentence.
        Some notes about the function:
            1. Stopwords are kept in place.
            2. Named Entities (i.e. people's names, place names, etc) are kept in place
            2. Words are never replaced with words that have the same first few characters. 
               Example: "going" -> ("go", "goes") would be excluded.
            3. WordNet returned lemmatized forms - these are inflected by to the correct POS tag using the lemminflect spaCy extension
        
        Returns: a string that has been 'smartified'.
    """
    smart = []
    sentence = nlp(sentence)

    for token in sentence:
        if token.is_stop or token.ent_iob in [1,3]:
            # this token is a stopword or part of a Named Entity: so append and continue
            smart.append(token.text)
            continue
            
        # uses the spacy_wordnet extension to parse the synonyms of this token
        # some lemmas are filtered out according to rules in the function comment above
        lemmas = [x.name() for x in token._.wordnet.lemmas() \
                  if not x.name().startswith(token.text[:2]) \
                  and len(x.name()) > 3][:8]

        if len(lemmas) == 0:
            # nothing was found: so just append the original token and continue
            smart.append(token.text)
            continue
            
        # now we can select a random lemma from our synonyms.
        # if it's a compound lemma, with "_" separating words, we join that up
        word = random.choice(lemmas)
        if "_" in word:
            word = ' '.join(word.split("_"))

        # now pass the text to the nlp() object to create a sequence of Token objects
        wtokens = nlp(word)
        
        # for each token in the selected lemma, we inflect back to original tense/part-of-speech where possible, and append
        for wtoken in wtokens:
            inflected_wtoken = wtoken._.inflect(token.tag_, inflect_oov=False)
            smart.append(inflected_wtoken)

    # return a string representing the converted sentence
    return ' '.join(smart).replace(" .", ".").replace(" ,", ",").replace(" !", "!")
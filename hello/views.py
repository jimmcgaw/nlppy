from django.shortcuts import render
from django.http import HttpResponse
import json

import nltk
from nltk.tokenize import word_tokenize


# Create your views here.
def index(request):
    translated = u"",
    if request.method == 'POST':
        sentence = request.POST.get('sentence', '');
        words = word_tokenize(sentence)
        translated = nltk.pos_tag(words)
    return render(request, 'index.html', locals())

def tokenize_tag(request):
    pass

PARTS_OF_SPEECH = {
    "CC" : "conjunction, coordinating",
    "CD" : "numeral, cardinal",
    "DT" : "determiner",
    "EX" : "existential there",
    "FW" : "foreign word",
    "IN" : "preposition or conjunction, subordinating",
    "JJ" : "adjective or numeral, ordinal",
    "JJR" : "adjective, comparative",
    "JJS" : "adjective, superlative",
    "LS" : "list item marker",
    "MD" : "modal auxiliary",
    "NN" : "noun, common, singular or",
    "NNP" : "noun, proper, singular",
    "NNPS" : "noun, proper, plural",
    "NNS" : "noun, common, plural",
    "PDT" : "pre-determiner",
    "POS" : "genitive marker",
    "PRP" : "pronoun, personal",
    "PRP$" : "pronoun, possessive",
    "RB" : "adverb",
    "RBR" : "adverb, comparative",
    "RBS" : "adverb, superlative",
    "RP" : "particle",
    "SYM" : "symbol",
    "TO" : "'to' as preposition or",
    "UH" : "interjection",
    "VB" : "verb, base form",
    "VBD" : "verb, past tense",
    "VBG" : "verb, present participle or",
    "VBN" : "verb, past participle",
    "VBP" : "verb, present tense, not",
    "VBZ" : "verb, present tense, 3rd",
    "WDT" : "WH-determiner",
    "WP" : "WH-pronoun",
    "WP$" : "WH-pronoun, possessive",
    "WRB" : "Wh-adverb",
}

def pos_lookup(request):
    pos = request.GET.get('pos')
    data = json.dumps({ 'text': PARTS_OF_SPEECH.get(pos) })
    return HttpResponse(data, content_type='application/json')

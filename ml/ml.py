from gensim.models.doc2vec import Doc2Vec
import torch
import json
from rake_nltk import Rake
import ml
import gensim.utils as utils

import valence_model, arousal_model


sentence_model = Doc2Vec.load('models/sentence_model1.dat')

valence_model = valence_model.Vec2ValenceNet(valence_model.D_in, valence_model.H, valence_model.D_out)
valence_model.load_state_dict(torch.load('models/valence_model1.dat'))

arousal_model = arousal_model.Vec2ArousalNet(arousal_model.D_in, arousal_model.H, arousal_model.D_out)
arousal_model.load_state_dict(torch.load('models/arousal_model1.dat'))

sentences = lambda review: map(' '.join, review)

def similarity_to_food(model, phrase):
    try:
        if 'food' in phrase:
            return -1.0
        return model.wv.n_similarity(phrase, ['food'])
    except KeyError:
        return -1.0

def menu_response(reviews):
    if not reviews:
        return [], 400

    reviews = filter(len, [filter(len, map(utils.simple_preprocess, i.split('.'))) for i in reviews])
    r = Rake()
    key_phrases = set()
    for review in reviews:
        r.extract_keywords_from_sentences(sentences(review))
        for i in sorted(r.get_ranked_phrases(), key=lambda s: similarity_to_food(ml.sentence_model, s), reverse=True)[:5]:
            key_phrases.add(i)

    similar_phrases = []
    for p1, p2 in map(lambda t: (t[0].split(), t[1].split()), itertools.combinations(key_phrases, 2)):
    	try:
            similar_phrases.append((p1, p2, sentence_model.wv.n_similarity(p1, p2)))
        except KeyError:
            pass
    similar_phrases = sorted(similar_phrases, key=lambda t: t[2], reverse=True)

    food_phrases = set()
    while similar_phrases and similar_phrases[0][2] > 0.9:
        shrt, lng = sorted([' '.join(similar_phrases[0][0]), ' '.join(similar_phrases[0][1])], key=len)
        if shrt not in food_phrases and lng not in food_phrases:
            food_phrases.add(shrt)
        try:
            key_phrases.remove(shrt)
        except KeyError, e:
            try:
                key_phrases.remove(lng)
            except KeyError:
                pass
        similar_phrases.pop(0)
    
    return sorted([(item, 50) for item in food_phrases], key=lambda t: t[1]), 200

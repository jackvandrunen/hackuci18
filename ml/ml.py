from gensim.models.doc2vec import Doc2Vec
import torch
from torch.autograd import Variable
import json
from rake_nltk import Rake
import ml
import gensim.utils as utils
import itertools
import numpy as np

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

def infer_emotion(vector):
    x = Variable(torch.FloatTensor(np.array([vector])), requires_grad=False)
    valence = float(valence_model(x))
    arousal = float(arousal_model(x))
    return arousal


def score_phrases(phrases, reviews):
    for phrase in phrases:
        sentences = []
        for review in reviews:
            for sentence in review:
                sentence = ' '.join(sentence)
                if phrase in sentence:
                    sentences.append(sentence)
        score = 0.0
        for sentence in sentences:
            vector = sentence_model.infer_vector(sentence.split())
            score += infer_emotion(vector)
        score /= len(sentences)
        yield phrase, int(score * 100)

def menu_response(reviews):
    if not reviews:
        return [], 400

    reviews = filter(len, [filter(len, map(utils.simple_preprocess, i.split('.'))) for i in reviews])
    r = Rake()
    key_phrases = []
    for review in reviews:
        r.extract_keywords_from_sentences(sentences(review))
        for i in sorted(r.get_ranked_phrases(), key=lambda s: similarity_to_food(ml.sentence_model, s), reverse=True)[:5]:
            key_phrases.append(i)

    similar_phrases = []
    for p1, p2 in map(lambda t: (t[0].split(), t[1].split()), itertools.combinations(key_phrases, 2)):
    	try:
            similar_phrases.append((p1, p2, sentence_model.wv.n_similarity(p1, p2)))
        except KeyError:
            pass
    similar_phrases = sorted(similar_phrases, key=lambda t: t[2], reverse=True)

    '''food_phrases = set()
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
        similar_phrases.pop(0)'''

    food_phrases, rejected, queue = set(), set(), set()
    for p1, p2, similarity in similar_phrases:
        if similarity < 0.75:
            break
        p1 = ' '.join(p1)
        p2 = ' '.join(p2)
        if p1 in food_phrases | rejected or p2 in food_phrases | rejected:
            continue
        if p1 in queue or p2 in queue:
            if len(p1) < len(p2):
                food_phrases.add(p1)
                rejected.add(p2)
            else:
                food_phrases.add(p2)
                rejected.add(p1)
        else:
            queue.add(p1)
            queue.add(p2)

    
    return sorted(score_phrases(food_phrases, reviews), key=lambda t: t[1], reverse=True), 200

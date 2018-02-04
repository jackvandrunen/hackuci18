from gensim.models.doc2vec import Doc2Vec
import torch

import valence_model, arousal_model


sentence_model = Doc2Vec.load('models/sentence_model1.dat')

valence_model = valence_model.Vec2ValenceNet(valence_model.D_in, valence_model.H, valence_model.D_out)
valence_model.load_state_dict(torch.load('models/valence_model1.dat'))

arousal_model = arousal_model.Vec2ArousalNet(arousal_model.D_in, arousal_model.H, arousal_model.D_out)
arousal_model.load_state_dict(torch.load('models/arousal_model1.dat'))


def menu_response(reviews):
    if not reviews:
        return [], 400
    return [], 200

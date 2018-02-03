from gensim.models.doc2vec import Doc2Vec
import torch


class Vec2ValenceNet(torch.nn.Module):
    
    def __init__(self, D_in, H, D_out):
        super(Vec2ValenceNet, self).__init__()
        self.layer_1 = torch.nn.Linear(D_in, H)
        self.layer_2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        h = self.layer_1(x).clamp(min=0)
        y = self.layer_2(h)
        return y


class Vec2ArousalNet(torch.nn.Module):
    
    def __init__(self, D_in, H, D_out):
        super(Vec2ArousalNet, self).__init__()
        self.layer_1 = torch.nn.Linear(D_in, H)
        self.layer_2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        h = self.layer_1(x).clamp(min=0)
        y = self.layer_2(h)
        return y


sentence_model = Doc2Vec.load('models/sentence_model1.dat')
valence_model = torch.load('models/valence_model1.dat')
arousal_model = torch.load('models/arousal_model1.dat')

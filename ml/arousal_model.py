import torch
from torch.autograd import Variable
import torch.utils.data
import json


class Vec2ArousalNet(torch.nn.Module):
    
    def __init__(self, D_in, H, D_out):
        super(Vec2ArousalNet, self).__init__()
        self.layer_1 = torch.nn.Linear(D_in, H)
        self.layer_2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        h = self.layer_1(x).clamp(min=0)
        y = self.layer_2(h)
        return y


class Vec2ArousalSet(torch.utils.data.Dataset):

    def __init__(self, path):
        with open(path) as f:
            self.data = [(torch.FloatTensor(i[0]), torch.FloatTensor([i[1][1]])) for i in json.load(f)]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]


def collate(batch):
    result = [[], []]
    for x, y in batch:
        result[0].append(x)
        result[1].append(y)
    return (torch.stack(result[0], 0), torch.stack(result[1], 0))


N, D_in, H, D_out = 64, 100, 200, 1

if __name__ == '__main__':
    dataset = Vec2ArousalSet('./emovec.json')
    loader = torch.utils.data.DataLoader(dataset, batch_size=N, shuffle=True, drop_last=True, collate_fn=collate)

    x = Variable(torch.zeros(N, D_in), requires_grad=False)
    y = Variable(torch.zeros(N, D_out), requires_grad=False)

#   model = Vec2ArousalNet(D_in, H, D_out)
    model = torch.load('arousal_model1.dat')

    error = torch.nn.MSELoss(size_average=False)
    optim = torch.optim.Adam(model.parameters(), lr=1e-03)

    era_losses = []
    losses = []
    min_loss = float('Inf')
    for epoch in range(1, 100001):
        for batch in loader:
            x.data, y.data = batch
            y_pred = model(x)

            loss = error(y_pred, y)
            loss.backward()
            optim.step()
            optim.zero_grad()
            losses.append(float(loss))
        avg = sum(losses) / len(losses)
        era_losses.append(avg)
        if avg < min_loss:
            min_loss = avg
            torch.save(model, 'arousal_model1.dat')
        if not epoch % 25:
            print 'epoch {}, loss: {}'.format(epoch, min(era_losses))
        era_losses = []
        losses = []

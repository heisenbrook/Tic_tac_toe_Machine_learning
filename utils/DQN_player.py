import torch
import random
import numpy as np
import torch.nn as nn
import torch.optim as optim

class DQN(nn.Module):
    def __init__(self, inp, out):
        super().__init__()
        self.activation = nn.ReLU()
        self.layer1 = nn.Linear(inp, 200)
        self.layer2 = nn.Linear(200, 200)
        self.layer3 = nn.Linear(200, out) 
    
    def forward(self, x):
        x = self.activation(self.layer1(x))
        x = self.activation(self.layer2(x))
        x = self.layer3(x)
        return x
    

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = DQN(9, 9).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.0001)
loss_fn = nn.MSELoss()

def select_action(state, epsilon):
    if np.random.rand() < epsilon:
        return int(random.choice(state))
    else:
        q_val = model(torch.tensor(state, dtype=torch.float32).to(device))
        return torch.argmax(q_val).item()

def update_model(memory, batch_size, gamma = 0.7):
    exp = random.sample(memory, batch_size)
    for state, action, reward, next_state, done in exp:
        target = reward
        if not done:
            target = reward + gamma * torch.max(model(torch.tensor(next_state, dtype=torch.float32).to(device))).item()
        target_l = model(torch.tensor(state, dtype=torch.float32).to(device))
        target_l[action] = target
        optimizer.zero_grad()
        loss = loss_fn(target_l.clone().detach(), model(torch.tensor(state, dtype=torch.float32).to(device)))
        loss.backward()
        optimizer.step()
        
        
import pytest
import torch
from torch import nn

@pytest.mark.parametrize("block_size,emb_size", [(5,8)])
def test_parameter(block_size,emb_size):
    pos_emb = nn.Parameter(torch.zeros(1, block_size,emb_size))
    # data = torch.tensor([[1,2,3]])
    # result = pos_emb(data)
    print(pos_emb)
    print(pos_emb.shape)


    
    assert pos_emb.shape == (1, block_size, emb_size)
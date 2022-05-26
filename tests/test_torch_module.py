import pytest
import torch
from torch import nn


@pytest.mark.parametrize("block_size,emb_size", [(5, 32)])
def test_parameter(block_size, emb_size):
    pos_emb = nn.Parameter(torch.zeros(1, block_size, emb_size))
    print(pos_emb.shape)
    assert pos_emb.shape == (1, block_size, emb_size)


@pytest.mark.parametrize("vocab_size, emb_size", [(16, 32)])
def test_embedding(vocab_size, emb_size):
    tok_emb = nn.Embedding(vocab_size, emb_size)
    data = torch.tensor([[1, 2, 5, 10, 5]])
    result = tok_emb(data)
    print(result.shape)
    assert result.shape == (1, data.shape[1], emb_size)


@pytest.mark.parametrize("block_size,emb_size", [(3, 32)])
def test_tril(block_size, emb_size):

    mask = torch.tril(torch.ones(block_size, block_size))
    expected = torch.tensor(
        [
            [1.0, 0.0, 0.0],
            [1.0, 1.0, 0.0],
            [1.0, 1.0, 1.0],
        ]
    )
    expected_inv = torch.tensor(
        [
            [0.0, 1.0, 1.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, 0.0],
        ]
    )
    assert torch.all(mask == expected)
    assert torch.all((1 - mask) == expected_inv)

    new_mask = 1 - mask
    print(new_mask)


@pytest.mark.parametrize("num_heads", [(2)])
def test_multihead_attention(num_heads):
    x = torch.ones((5, 3, 6))

    batch_size, block_size, emb_size = x.shape
    multi_head = nn.MultiheadAttention(
        embed_dim=emb_size, num_heads=num_heads, bias=True, batch_first=True
    )
    mask = 1 - torch.tril(torch.ones(block_size, block_size))
    mask = mask.to(dtype=torch.bool)
    print()
    print(mask)
    print(f"{x.shape=}")
    print(f"{mask.shape=}")
    # For a binary mask, a True value indicates that the corresponding position is not
    # allowed to attend.

    attn_output, attn_output_weights = multi_head(x, x, x, attn_mask=mask, need_weights=True)
    print(f"{attn_output.shape=}")
    print(f"{attn_output_weights.shape=}")

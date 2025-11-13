HfMoondream(
  (model): MoondreamModel(
    (vision): ModuleDict(
      (patch_emb): Linear(in_features=588, out_features=1152, bias=True)
      (blocks): ModuleList(
        (0-26): 27 x ModuleDict(
          (ln1): LayerNorm((1152,), eps=1e-05, elementwise_affine=True)
          (attn): ModuleDict(
            (qkv): Linear(in_features=1152, out_features=3456, bias=True)
            (proj): Linear(in_features=1152, out_features=1152, bias=True)
          )
          (ln2): LayerNorm((1152,), eps=1e-05, elementwise_affine=True)
          (mlp): ModuleDict(
            (fc1): Linear(in_features=1152, out_features=4304, bias=True)
            (fc2): Linear(in_features=4304, out_features=1152, bias=True)
          )
        )
      )
      (post_ln): LayerNorm((1152,), eps=1e-05, elementwise_affine=True)
      (proj_mlp): ModuleDict(
        (fc1): Linear(in_features=2304, out_features=8192, bias=True)
        (fc2): Linear(in_features=8192, out_features=2048, bias=True)
      )
    )
    (text): ModuleDict(
      (blocks): ModuleList(
        (0-23): 24 x ModuleDict(
          (ln): LayerNorm((2048,), eps=1e-05, elementwise_affine=True)
          (attn): ModuleDict(
            (qkv): Linear(in_features=2048, out_features=6144, bias=True)
            (proj): Linear(in_features=2048, out_features=2048, bias=True)
          )
          (mlp): ModuleDict(
            (fc1): Linear(in_features=2048, out_features=8192, bias=True)
            (fc2): Linear(in_features=8192, out_features=2048, bias=True)
          )
        )
      )
      (post_ln): LayerNorm((2048,), eps=1e-05, elementwise_affine=True)
      (lm_head): Linear(in_features=2048, out_features=51200, bias=True)
    )
    (region): ModuleDict(
      (coord_encoder): Linear(in_features=256, out_features=2048, bias=True)
      (coord_decoder): ModuleDict(
        (fc1): Linear(in_features=2048, out_features=8192, bias=True)
        (fc2): Linear(in_features=8192, out_features=1024, bias=True)
      )
      (size_encoder): Linear(in_features=512, out_features=2048, bias=True)
      (size_decoder): ModuleDict(
        (fc1): Linear(in_features=2048, out_features=8192, bias=True)
        (fc2): Linear(in_features=8192, out_features=2048, bias=True)
      )
    )
  )
)
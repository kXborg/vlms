LlavaQwen2ForCausalLM(
  (model): LlavaQwen2Model(
    (embed_tokens): Embedding(151936, 1536)
    (layers): ModuleList(
      (0-27): 28 x Qwen2DecoderLayer(
        (self_attn): Qwen2Attention(
          (q_proj): Linear(in_features=1536, out_features=1536, bias=True)
          (k_proj): Linear(in_features=1536, out_features=256, bias=True)
          (v_proj): Linear(in_features=1536, out_features=256, bias=True)
          (o_proj): Linear(in_features=1536, out_features=1536, bias=False)
        )
        (mlp): Qwen2MLP(
          (gate_proj): Linear(in_features=1536, out_features=8960, bias=False)
          (up_proj): Linear(in_features=1536, out_features=8960, bias=False)
          (down_proj): Linear(in_features=8960, out_features=1536, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): Qwen2RMSNorm((1536,), eps=1e-06)
        (post_attention_layernorm): Qwen2RMSNorm((1536,), eps=1e-06)
      )
    )
    (norm): Qwen2RMSNorm((1536,), eps=1e-06)
    (rotary_emb): Qwen2RotaryEmbedding()
    (vision_tower): MobileCLIPVisionTower(
      (vision_tower): MCi(
        (model): FastViT(
          (patch_embed): Sequential(
            (0): MobileOneBlock(
              (se): Identity()
              (activation): GELU(approximate='none')
              (reparam_conv): Conv2d(3, 96, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
            )
            (1): MobileOneBlock(
              (se): Identity()
              (activation): GELU(approximate='none')
              (reparam_conv): Conv2d(96, 96, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=96)
            )
            (2): MobileOneBlock(
              (se): Identity()
              (activation): GELU(approximate='none')
              (reparam_conv): Conv2d(96, 96, kernel_size=(1, 1), stride=(1, 1))
            )
          )
          (network): ModuleList(
            (0): Sequential(
              (0): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(96, 96, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=96)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(96, 96, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=96, bias=False)
                    (bn): BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(96, 384, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(384, 96, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (1): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(96, 96, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=96)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(96, 96, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=96, bias=False)
                    (bn): BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(96, 384, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(384, 96, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
            )
            (1): PatchEmbed(
              (proj): Sequential(
                (0): ReparamLargeKernelConv(
                  (activation): GELU(approximate='none')
                  (se): Identity()
                  (lkb_reparam): Conv2d(96, 192, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), groups=96)
                )
                (1): MobileOneBlock(
                  (se): Identity()
                  (activation): GELU(approximate='none')
                  (reparam_conv): Conv2d(192, 192, kernel_size=(1, 1), stride=(1, 1))
                )
              )
            )
            (2): Sequential(
              (0): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (1): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (2): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (3): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (4): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (5): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (6): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (7): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (8): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (9): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (10): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (11): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(192, 192, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=192, bias=False)
                    (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(192, 768, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(768, 192, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
            )
            (3): PatchEmbed(
              (proj): Sequential(
                (0): ReparamLargeKernelConv(
                  (activation): GELU(approximate='none')
                  (se): Identity()
                  (lkb_reparam): Conv2d(192, 384, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), groups=192)
                )
                (1): MobileOneBlock(
                  (se): Identity()
                  (activation): GELU(approximate='none')
                  (reparam_conv): Conv2d(384, 384, kernel_size=(1, 1), stride=(1, 1))
                )
              )
            )
            (4): Sequential(
              (0): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (1): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (2): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (3): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (4): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (5): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (6): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (7): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (8): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (9): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (10): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (11): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (12): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (13): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (14): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (15): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (16): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (17): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (18): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (19): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (20): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (21): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (22): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (23): RepMixerBlock(
                (token_mixer): RepMixer(
                  (reparam_conv): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(384, 384, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=384, bias=False)
                    (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(384, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(1536, 384, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
            )
            (5): PatchEmbed(
              (proj): Sequential(
                (0): ReparamLargeKernelConv(
                  (activation): GELU(approximate='none')
                  (se): Identity()
                  (lkb_reparam): Conv2d(384, 768, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), groups=384)
                )
                (1): MobileOneBlock(
                  (se): Identity()
                  (activation): GELU(approximate='none')
                  (reparam_conv): Conv2d(768, 768, kernel_size=(1, 1), stride=(1, 1))
                )
              )
            )
            (6): RepCPE(
              (reparam_conv): Conv2d(768, 768, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=768)
            )
            (7): Sequential(
              (0): AttentionBlock(
                (norm): LayerNormChannel()
                (token_mixer): MHSA(
                  (qkv): Linear(in_features=768, out_features=2304, bias=False)
                  (attn_drop): Dropout(p=0.0, inplace=False)
                  (proj): Linear(in_features=768, out_features=768, bias=True)
                  (proj_drop): Dropout(p=0.0, inplace=False)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(768, 768, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=768, bias=False)
                    (bn): BatchNorm2d(768, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(768, 3072, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(3072, 768, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (1): AttentionBlock(
                (norm): LayerNormChannel()
                (token_mixer): MHSA(
                  (qkv): Linear(in_features=768, out_features=2304, bias=False)
                  (attn_drop): Dropout(p=0.0, inplace=False)
                  (proj): Linear(in_features=768, out_features=768, bias=True)
                  (proj_drop): Dropout(p=0.0, inplace=False)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(768, 768, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=768, bias=False)
                    (bn): BatchNorm2d(768, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(768, 3072, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(3072, 768, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (2): AttentionBlock(
                (norm): LayerNormChannel()
                (token_mixer): MHSA(
                  (qkv): Linear(in_features=768, out_features=2304, bias=False)
                  (attn_drop): Dropout(p=0.0, inplace=False)
                  (proj): Linear(in_features=768, out_features=768, bias=True)
                  (proj_drop): Dropout(p=0.0, inplace=False)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(768, 768, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=768, bias=False)
                    (bn): BatchNorm2d(768, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(768, 3072, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(3072, 768, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (3): AttentionBlock(
                (norm): LayerNormChannel()
                (token_mixer): MHSA(
                  (qkv): Linear(in_features=768, out_features=2304, bias=False)
                  (attn_drop): Dropout(p=0.0, inplace=False)
                  (proj): Linear(in_features=768, out_features=768, bias=True)
                  (proj_drop): Dropout(p=0.0, inplace=False)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(768, 768, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=768, bias=False)
                    (bn): BatchNorm2d(768, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(768, 3072, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(3072, 768, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
            )
            (8): PatchEmbed(
              (proj): Sequential(
                (0): ReparamLargeKernelConv(
                  (activation): GELU(approximate='none')
                  (se): Identity()
                  (lkb_reparam): Conv2d(768, 1536, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), groups=768)
                )
                (1): MobileOneBlock(
                  (se): Identity()
                  (activation): GELU(approximate='none')
                  (reparam_conv): Conv2d(1536, 1536, kernel_size=(1, 1), stride=(1, 1))
                )
              )
            )
            (9): RepCPE(
              (reparam_conv): Conv2d(1536, 1536, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=1536)
            )
            (10): Sequential(
              (0): AttentionBlock(
                (norm): LayerNormChannel()
                (token_mixer): MHSA(
                  (qkv): Linear(in_features=1536, out_features=4608, bias=False)
                  (attn_drop): Dropout(p=0.0, inplace=False)
                  (proj): Linear(in_features=1536, out_features=1536, bias=True)
                  (proj_drop): Dropout(p=0.0, inplace=False)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(1536, 1536, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=1536, bias=False)
                    (bn): BatchNorm2d(1536, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(1536, 6144, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(6144, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
              (1): AttentionBlock(
                (norm): LayerNormChannel()
                (token_mixer): MHSA(
                  (qkv): Linear(in_features=1536, out_features=4608, bias=False)
                  (attn_drop): Dropout(p=0.0, inplace=False)
                  (proj): Linear(in_features=1536, out_features=1536, bias=True)
                  (proj_drop): Dropout(p=0.0, inplace=False)
                )
                (convffn): ConvFFN(
                  (conv): Sequential(
                    (conv): Conv2d(1536, 1536, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), groups=1536, bias=False)
                    (bn): BatchNorm2d(1536, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                  )
                  (fc1): Conv2d(1536, 6144, kernel_size=(1, 1), stride=(1, 1))
                  (act): GELU(approximate='none')
                  (fc2): Conv2d(6144, 1536, kernel_size=(1, 1), stride=(1, 1))
                  (drop): Dropout(p=0.0, inplace=False)
                )
                (drop_path): Identity()
              )
            )
          )
          (conv_exp): MobileOneBlock(
            (se): SEBlock(
              (reduce): Conv2d(3072, 192, kernel_size=(1, 1), stride=(1, 1))
              (expand): Conv2d(192, 3072, kernel_size=(1, 1), stride=(1, 1))
            )
            (activation): GELU(approximate='none')
            (reparam_conv): Conv2d(1536, 3072, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=1536)
          )
          (head): GlobalPool2D()
        )
      )
    )
    (mm_projector): Sequential(
      (0): Linear(in_features=3072, out_features=1536, bias=True)
      (1): GELU(approximate='none')
      (2): Linear(in_features=1536, out_features=1536, bias=True)
    )
  )
  (lm_head): Linear(in_features=1536, out_features=151936, bias=False)
)
Idefics3ForConditionalGeneration(
  (model): Idefics3Model(
    (vision_model): Idefics3VisionTransformer(
      (embeddings): Idefics3VisionEmbeddings(
        (patch_embedding): Conv2d(3, 768, kernel_size=(16, 16), stride=(16, 16), padding=valid)
        (position_embedding): Embedding(1024, 768)
      )
      (encoder): Idefics3Encoder(
        (layers): ModuleList(
          (0-11): 12 x Idefics3EncoderLayer(
            (self_attn): Idefics3VisionAttention(
              (k_proj): Linear(in_features=768, out_features=768, bias=True)
              (v_proj): Linear(in_features=768, out_features=768, bias=True)
              (q_proj): Linear(in_features=768, out_features=768, bias=True)
              (out_proj): Linear(in_features=768, out_features=768, bias=True)
            )
            (layer_norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
            (mlp): Idefics3VisionMLP(
              (activation_fn): PytorchGELUTanh()
              (fc1): Linear(in_features=768, out_features=3072, bias=True)
              (fc2): Linear(in_features=3072, out_features=768, bias=True)
            )
            (layer_norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          )
        )
      )
      (post_layernorm): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
    )
    (connector): Idefics3Connector(
      (modality_projection): Idefics3SimpleMLP(
        (proj): Linear(in_features=12288, out_features=576, bias=False)
      )
    )
    (text_model): LlamaModel(
      (embed_tokens): Embedding(49280, 576, padding_idx=2)
      (layers): ModuleList(
        (0-29): 30 x LlamaDecoderLayer(
          (self_attn): LlamaAttention(
            (q_proj): Linear(in_features=576, out_features=576, bias=False)
            (k_proj): Linear(in_features=576, out_features=192, bias=False)
            (v_proj): Linear(in_features=576, out_features=192, bias=False)
            (o_proj): Linear(in_features=576, out_features=576, bias=False)
          )
          (mlp): LlamaMLP(
            (gate_proj): Linear(in_features=576, out_features=1536, bias=False)
            (up_proj): Linear(in_features=576, out_features=1536, bias=False)
            (down_proj): Linear(in_features=1536, out_features=576, bias=False)
            (act_fn): SiLU()
          )
          (input_layernorm): LlamaRMSNorm((576,), eps=1e-05)
          (post_attention_layernorm): LlamaRMSNorm((576,), eps=1e-05)
        )
      )
      (norm): LlamaRMSNorm((576,), eps=1e-05)
      (rotary_emb): LlamaRotaryEmbedding()
    )
  )
  (lm_head): Linear(in_features=576, out_features=49280, bias=False)
)
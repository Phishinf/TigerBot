from opencompass.models import HuggingFaceCausalLM

models = [
    dict(
        type=HuggingFaceCausalLM,
        abbr='baichuan-13b-chat',
        path="baichuan-inc/Baichuan-13B-Chat",
        tokenizer_path='baichuan-inc/Baichuan-13B-Chat',
        tokenizer_kwargs=dict(padding_side='left',
                              truncation_side='left',
                              trust_remote_code=True,
                              use_fast=False, ),
        max_out_len=100,
        max_seq_len=2048,
        batch_size=8,
        model_kwargs=dict(device_map='auto', trust_remote_code=True),
        batch_padding=True,
        run_cfg=dict(num_gpus=1, num_procs=1),
    ),
    dict(
        type=HuggingFaceCausalLM,
        abbr='baichuan-13b-base',
        path="baichuan-inc/Baichuan-7B",
        tokenizer_path='baichuan-inc/Baichuan-7B',
        tokenizer_kwargs=dict(padding_side='left',
                              truncation_side='left',
                              trust_remote_code=True,
                              use_fast=False, ),
        max_out_len=100,
        max_seq_len=2048,
        batch_size=8,
        model_kwargs=dict(device_map='auto', trust_remote_code=True),
        batch_padding=True,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]


from opencompass.models import ExllamaCausalLM

_meta_template = dict(
    round=[
        dict(role='HUMAN', begin='\n\n### Instruction:\n'),
        dict(role='BOT', begin='\n\n### Response:\n', generate=True),
    ],
)

models = [
    dict(
        type= ExllamaCausalLM,
        abbr='tigerbot',
        path="/mnt/nfs/algo/intern/yuwang/Tigerbot_AutoGPTQ/tigerbot_13b/tigerbot_13b_chat_4bit_c4_128g_no_act",
        tokenizer_path='/mnt/nfs/algo/intern/yuwang/Tigerbot_AutoGPTQ/tigerbot_13b/tigerbot_13b_chat_4bit_c4_128g_no_act',
        tokenizer_kwargs=dict(
            cache_dir=None,
            padding_side='left',
            truncation_side='left',
            trust_remote_code=True,
            padding=True,
            truncation=True,
            add_bos_token=False
        ),
        max_out_len=100,
        max_seq_len=2048,
        batch_size=4,
        batch_padding=True,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]

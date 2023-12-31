from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import PPLInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator
from opencompass.datasets import RaceDataset

race_reader_cfg = dict(
    input_columns=['article', 'question', 'A', 'B', 'C', 'D'],
    output_column='answer')

race_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template={
            'A':
            'Read the article, and answer the question by replying A, B, C or D.\n\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}\n\nAnswer: A',
            'B':
            'Read the article, and answer the question by replying A, B, C or D.\n\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}\n\nAnswer: B',
            'C':
            'Read the article, and answer the question by replying A, B, C or D.\n\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}\n\nAnswer: C',
            'D':
            'Read the article, and answer the question by replying A, B, C or D.\n\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}\n\nAnswer: D',
        }),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=PPLInferencer))

race_eval_cfg = dict(evaluator=dict(type=AccEvaluator))

race_datasets = [
    dict(
        type=RaceDataset,
        abbr='race-middle',
        path='race',
        name='middle',
        reader_cfg=race_reader_cfg,
        infer_cfg=race_infer_cfg,
        eval_cfg=race_eval_cfg),
    dict(
        type=RaceDataset,
        abbr='race-high',
        path='race',
        name='high',
        reader_cfg=race_reader_cfg,
        infer_cfg=race_infer_cfg,
        eval_cfg=race_eval_cfg)
]

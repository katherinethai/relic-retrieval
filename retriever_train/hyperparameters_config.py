lit_analysis_both = [
    [('model_name',), ['roberta-base']],
    [('dataset',), ["relic_preprocessed/left_1_right_1_neg_100"]],
    [('batch_size',), [1]],
    [('accumulation',), [1]],
    [('num_epochs',), [10]],
    [('beam_size',), [1]],
    [('eval_batch_size',), [1]],
    [('learning_rate',), ["1e-5"]],
    [('gpu',), ["rtx8000-short"]],
    [('ngpus',), ["1"]],
    [('save_steps',), [250]],
    [('save_total_limit',), [-1]],
    [('optimizer',), ["adam"]],
    [('negative_examples',), ["suffix"]],
    [('prefix_truncate_dir',), ["both"]],
    [('eval_frequency_min',), ["10"]],
]

lit_analysis_left = [
    [('model_name',), ['roberta-base']],
    [('dataset',), ["relic_preprocessed/left_1_right_0_neg_100"]],
    [('batch_size',), [1]],
    [('accumulation',), [1]],
    [('num_epochs',), [10]],
    [('beam_size',), [1]],
    [('eval_batch_size',), [1]],
    [('learning_rate',), ["1e-5"]],
    [('gpu',), ["rtx8000-long"]],
    [('ngpus',), ["1"]],
    [('save_steps',), [250]],
    [('save_total_limit',), [-1]],
    [('optimizer',), ["adam"]],
    [('negative_examples',), ["suffix"]],
    [('prefix_truncate_dir',), ["left"]],
    [('eval_frequency_min',), ["10"]],
]

lit_analysis_right = [
    [('model_name',), ['roberta-base']],
    [('dataset',), ["relic_preprocessed/left_0_right_1_neg_100"]],
    [('batch_size',), [1]],
    [('accumulation',), [1]],
    [('num_epochs',), [10]],
    [('beam_size',), [1]],
    [('eval_batch_size',), [1]],
    [('learning_rate',), ["1e-5"]],
    [('gpu',), ["rtx8000-long"]],
    [('ngpus',), ["1"]],
    [('save_steps',), [250]],
    [('save_total_limit',), [-1]],
    [('optimizer',), ["adam"]],
    [('negative_examples',), ["suffix"]],
    [('prefix_truncate_dir',), ["right"]],
    [('eval_frequency_min',), ["10"]],
]

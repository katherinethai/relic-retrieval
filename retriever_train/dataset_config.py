from collections import defaultdict


BASE_CONFIG = {
    "keys": [
        {"key": "sent1_tokens", "position": "empty", "tokenize": True, "metadata": False},
        {"key": "sent2_tokens", "position": "sequence", "tokenize": True, "metadata": False}
    ],
    "max_total_length": 128,
    "max_prefix_length": 256,
    "max_suffix_length": 98,
    "max_dense_length": 2
}


DATASET_CONFIG = {
    "relic_preprocessed/left_1_right_1_neg_100": BASE_CONFIG,
    "relic_preprocessed/left_4_right_4_neg_100": BASE_CONFIG,
    "relic_preprocessed/left_4_right_0_neg_100": BASE_CONFIG,
    "relic_preprocessed/left_0_right_4_neg_100": BASE_CONFIG,
    "relic_preprocessed/left_1_right_0_neg_100": BASE_CONFIG,
    "relic_preprocessed/left_0_right_1_neg_100": BASE_CONFIG
}

# Fill in DATASET_CONFIG with keys it was missing previously
for dataset, config in DATASET_CONFIG.items():
    for base_key, base_value in BASE_CONFIG.items():
        if base_key not in config:
            config[base_key] = base_value

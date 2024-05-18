# this is for loading the dataset

from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
from dataclasses import asdict

dataset_config = BaseDatasetConfig(formatter="vctk", meta_file_train="/Users/achimmula/Downloads/LJSpeech-1.1/metadata.txt",
                                   language="en-us", path="/Users/achimmula/Downloads/LJSpeech-1.1/wavs")

dataset_config_dict = asdict(dataset_config)
train_samples, eval_samples = load_tts_samples(
    dataset_config_dict, eval_split=True)

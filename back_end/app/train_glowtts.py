# none of this code is actually mine I took it from the https://docs.coqui.ai/en/dev/training_a_model.html

# this is file is not used yet

# this is useful for training the model but it is computationally expensive I didn't even finished running 1 epoch
# I am not even sure if it is working properly as expected 

import os

from trainer import Trainer, TrainerArgs

from TTS.tts.configs.glow_tts_config import GlowTTSConfig

from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.glow_tts import GlowTTS
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor
from dataclasses import asdict

def main(): 

    output_path = os.path.dirname(os.path.abspath(__file__)) + "/output"

    dataset_config = BaseDatasetConfig(formatter="ljspeech", 
                                    meta_file_train="/Users/achimmula/Downloads/LJSpeech-1.1/metadata.txt", 
                                    language="en-us", 
                                    path="/Users/achimmula/Downloads/LJSpeech-1.1/")


    config = GlowTTSConfig(
        batch_size=32,
        eval_batch_size=16,
        num_loader_workers=4,
        num_eval_loader_workers=4,
        run_eval=True,
        test_delay_epochs=-1,
        epochs=5,
        text_cleaner="phoneme_cleaners",
        use_phonemes=True,
        phoneme_language="en-us",
        phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
        print_step=25,
        print_eval=False,
        mixed_precision=True,
        output_path=output_path,
        datasets=[dataset_config],
    )

    ap = AudioProcessor.init_from_config(config)

    tokenizer, config = TTSTokenizer.init_from_config(config)

    # dataset_config = asdict(dataset_config)

    train_samples, eval_samples = load_tts_samples(
        dataset_config, # type: ignore
        eval_split=True,
        eval_split_max_size=config.eval_split_max_size,
        eval_split_size=config.eval_split_size,
    )

    model = GlowTTS(config, ap, tokenizer, speaker_manager=None) # type: ignore

    trainer = Trainer(
        TrainerArgs(), config, output_path, model=model, train_samples=train_samples, eval_samples=eval_samples
    )

    trainer.fit()


if __name__ == '__main__':
    main()
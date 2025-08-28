# This script is adapted from the Neuro-Logical/speech repository:
# https://github.com/Neuro-Logical/speech/tree/main/Multilingual_Evaluation/data_preprocessing/get_speech_transcripts.py
# Modifications were made to fit macOS and project-specific requirements.

import os
from pathlib import Path
import whisper
import argparse

def extract_transcripts(path_recordings, output_folder, language="en"):
    """
    Extract transcription from speech recordings using Whisper.

    Args:
        path_recordings (str): Path to the folder containing .wav recordings.
        output_folder (str): Path to the folder where transcriptions will be saved.
        language (str): Language of the speech recordings (default: "en").
    """
    print("Loading Whisper model...")
    model = whisper.load_model("large-v3")
    print("Model loaded successfully.")

    recordings_path = Path(path_recordings)
    output_path = Path(output_folder)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_path}")

    # List all .wav files in the input directory
    wav_files = list(recordings_path.glob("*.wav"))
    print(f"Found {len(wav_files)} .wav files to process.")

    if not wav_files:
        print("No .wav files found. Please check the input directory.")
        return

    # Process each .wav file
    for path in wav_files:
        try:
            print(f"Processing file: {path.name}")
            result = model.transcribe(str(path), language=language)
            output_file = output_path / f"{path.stem}.txt"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result['text'])

            print(f"Transcription saved to {output_file}\n")

        except Exception as e:
            print(f"Error processing file {path.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio recordings to text using Whisper.")
    parser.add_argument("--input", type=str, default="./input_audio", help="Path to the folder containing .wav recordings.")
    parser.add_argument("--output", type=str, default="./transcriptions", help="Path to the folder to save transcription files.")
    parser.add_argument("--language", type=str, default="en", help="Language code of the recordings (default: 'en').")
    args = parser.parse_args()

    extract_transcripts(args.input, args.output, args.language)

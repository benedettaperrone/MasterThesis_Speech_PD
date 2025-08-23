import os
from pathlib import Path
import argparse

def check_files_in_directory(path_recordings):
    """
    Check if .wav files are present in the specified directory.

    Args:
        path_recordings (str): Path to the folder to check for .wav files.
    """
    recordings_path = Path(path_recordings)
    wav_files = list(recordings_path.glob("*.wav"))
    
    print(f"Checking directory: {recordings_path}")
    print(f"Found {len(wav_files)} .wav files.")

    if wav_files:
        for path in wav_files:
            print(f"File found: {path.name}")
    else:
        print("No .wav files found in the directory.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for .wav files in a directory.")
    parser.add_argument("--input", type=str, default="./input_audio", help="Path to the folder to check for .wav files.")
    args = parser.parse_args()

    check_files_in_directory(args.input)

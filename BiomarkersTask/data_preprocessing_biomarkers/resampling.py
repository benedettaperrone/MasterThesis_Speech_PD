import os
import json
import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf  # Library to read and write audio files

# ------------------- USER CONFIG -------------------
# Path to the input JSON file containing audio metadata
json_path = "dataset.json"

# Base directory where the audio files are stored
input_base_path = "/path/to/your/audio/files"

# Directory where resampled audio files will be saved
output_directory = "/path/to/save/resampled/audio"

# Target sample rate for resampling
target_sr = 16000
# ---------------------------------------------------

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to plot and compare original and resampled waveforms
def plot_waveforms(original, resampled, sr_orig, sr_resampled, title):
    plt.figure(figsize=(12, 6))

    # Original waveform
    plt.subplot(2, 1, 1)
    librosa.display.waveshow(original, sr=sr_orig)
    plt.title(f'Original: {title} (SR: {sr_orig})')

    # Resampled waveform
    plt.subplot(2, 1, 2)
    librosa.display.waveshow(resampled, sr=sr_resampled)
    plt.title(f'Resampled: {title} (SR: {sr_resampled})')

    plt.tight_layout()
    plt.show()

# Load JSON file
with open(json_path, 'r') as file:
    data = json.load(file)

# Loop through each entry in the JSON
for idx, entry in enumerate(data):
    # Check if audio path exists in the entry
    if 'audio' not in entry:
        print(f"Skipping entry {idx}: no audio path found")
        continue

    # Construct full path to the audio file
    audio_path = os.path.join(input_base_path, entry['audio'])

    try:
        # Load original audio with its native sample rate
        audio, sr = librosa.load(audio_path, sr=None)

        # Resample audio to the target sample rate
        resampled_audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)

        # Save resampled audio to the output directory
        output_file_path = os.path.join(output_directory, os.path.basename(audio_path))
        sf.write(output_file_path, resampled_audio, target_sr)

        # Print progress
        print(f"Processed file {idx + 1}/{len(data)}: {os.path.basename(audio_path)}")

        # Optionally plot waveforms for a few random examples
        if np.random.rand() < min(3 / len(data), 1):  # roughly 3 random examples
            plot_waveforms(audio, resampled_audio, sr, target_sr, os.path.basename(audio_path))

    except Exception as e:
        print(f"Error processing file {audio_path}: {e}")

print("Resampling completed.")

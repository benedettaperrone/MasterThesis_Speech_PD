#!/bin/bash

# ------------------- CONFIGURATION -------------------
# Input directory containing .wav files to normalize
in_dir="${1:-./input_audio}"

# Output directory where normalized audio files will be saved
out_dir="${2:-./normalized_audio}"

# Target sample rate for normalized files
target_sr=16000

# Target loudness in LUFS (RMS normalization)
target_lufs=-18
# -----------------------------------------------------

echo "Input Directory: $in_dir"
echo "Output Directory: $out_dir"

# Check if ffmpeg-normalize is installed
if ! command -v ffmpeg-normalize &> /dev/null; then
    echo "ffmpeg-normalize could not be found. Please install it before running this script."
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$out_dir"

# Loop through each .wav file in the input directory
for file in "$in_dir"/*.wav; do
    # Extract the filename
    audio_file=$(basename "$file")
    output_file="$out_dir/$audio_file"

    # Skip processing if the output file already exists
    if [ -f "$output_file" ]; then
        echo "Skipping $audio_file as it already exists in the output directory."
        continue
    fi

    echo "Processing file: $file"
    echo "Output file will be: $output_file"

    # Normalize audio with target sample rate and loudness
    ffmpeg-normalize "$file" -ar "$target_sr" -nt rms -t "$target_lufs" -o "$output_file" -f
done

echo "Normalization completed."

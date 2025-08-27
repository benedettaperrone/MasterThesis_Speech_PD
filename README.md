# MasterThesis_Speech_PD

# Master Thesis Speech Processing

This repository contains code developed for my Master's thesis on speech processing, divided into two main tasks: **Biomarkers Task** and **Classification Task**. The goal of this project is to analyze speech data using different preprocessing and machine learning techniques.

---

## Repository Structure

## 1. Biomarkers Task

This part of the project deals with evaluating speech biomarkers, specifically **Word Error Rate (WER)** and **Character Error Rate (CER)**, on a set of audio recordings.

### 1.1 Data Preprocessing

The preprocessing pipeline includes:

- Resampling audio recordings
- Normalizing audio loudness
- Transcribing audio to text using OpenAI Whisper

**Note:** Some scripts in `data_preprocessing_biomarkers` were adapted from the work of Favaro et al., 2023:

- Repository: [Neuro-Logical/speech](https://github.com/Neuro-Logical/speech/tree/main/Multilingual_Evaluation/data_preprocessing)
- Scripts adapted:
  - `convert_to_16k.sh`
  - `get_speech_transcripts.py`
  - `loudness_norm.sh`
- `requirements.txt` file for the preprocessing pipeline was also taken from Favaro et al., 2023 and may include packages not required for this project.

We modified the scripts to run on macOS and adapted them for our datasets. Proper attribution is provided in the script headers and in this README.


### 1.2 WER and CER Calculation

After preprocessing, transcripts are compared to reference text to calculate:

- **WER (Word Error Rate)**  
- **CER (Character Error Rate)**  

Scripts in `WER_CER` automate this calculation for all datasets used.

---

## 2. Classification Task

This task focuses on classifying audio containing vowels using transformer models.



### 2.1 Data Preprocessing

Audio is prepared for the transformers models in the folder `data_preprocessing_classification`. This includes steps such as:

- Standardizing audio format
- Feature extraction suitable for transformer input

### 2.2 Transformers Models

The models implemented are:

- **ViT (Vision Transformer)** – normal and parallel versions
- **AST (Audio Spectrogram Transformer)** – normal and parallel versions

Scripts for training, evaluation, and inference are in the `transformers` folder.

---

## Usage

### Biomarkers Task

```bash
# Navigate to preprocessing folder
cd BiomarkersTask/data_preprocessing_biomarkers

# Resample and normalize audio
bash convert_to_16k.sh
bash loudness_norm.sh

# Transcribe audio to text
python get_speech_transcripts.py --input ./audio --output ./transcripts

@article{favaro2023multilingual,
  title={Multilingual evaluation of interpretable biomarkers to represent language and speech patterns in Parkinson's disease},
  author={Favaro, Anna and Moro-Vel{\'a}zquez, Laureano and Butala, Ankur and Motley, Chelsie and Cao, Tianyu and Stevens, Robert David and Villalba, Jes{\'u}s and Dehak, Najim},
  journal={Frontiers in Neurology},
  volume={14},
  pages={1142642},
  year={2023},
  publisher={Frontiers}
} 

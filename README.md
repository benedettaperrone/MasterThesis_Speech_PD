# 🎓 Master Thesis – Speech Processing for Parkinson’s Disease

This repository contains the code developed for my Master's thesis in Biomedical Engineering at Politecnico di Torino.  
The project focuses on the analysis of speech data to investigate **biomarkers** and perform **classification tasks** using transformer-based deep learning models.  

Parkinson's disease (PD) is often associated with alterations in voice and speech, which can serve as non-invasive indicators of disease presence and severity.  
This work explores both **automatic speech recognition errors** (WER/CER) and **speech classification models** as potential tools for remote monitoring of PD.

👉 The full thesis is available at: [Webthesis – Politecnico di Torino](https://webthesis.biblio.polito.it/33679/)

---

## 🗂 Datasets

This study utilized three datasets, **which are not included in this repository**:  

1. **Molinette Dataset** – Recordings from 14 PD patients performing sustained vowels, proverbs, and monologues. Data include ON and OFF phases for six patients. *(Private dataset)*

2. **PC-GITA Dataset** – Recordings from 50 PD patients and 50 healthy controls, including vowels, DDK tasks, sentences, and monologues. Data were collected in a noise-controlled environment at Clínica Noel, Medellín, Colombia. This dataset is available on request from the authors.  
   Citation: [Orozco et al., 2014](https://www.researchgate.net/publication/265592171_New_Spanish_speech_corpus_database_for_the_analysis_of_people_suffering_from_Parkinson's_disease/citations)

3. **Bari Dataset** – Recordings from 28 PD patients and 22 healthy controls performing vowels, syllables, and phonemically balanced text reading. This dataset can be requested from the authors.  
   Citation: [Dimauro & Girardi, 2017](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech)

The datasets were used for deep learning classification (sustained vowels), WER and CER analysis (sentences, proverbs, and text), and statistical analysis (UPDRS scores). Detailed descriptions, including demographics, recording protocols, and tasks, are in the thesis.

---

## 📂 Repository Structure

### 1. Biomarkers Task
Evaluation of **Word Error Rate (WER)** and **Character Error Rate (CER)** as potential biomarkers for Parkinson’s disease.

- **`Preprocessing_Biomarkers/`**  
  Scripts for audio preprocessing:
  - Resampling to 16 kHz  
  - Loudness normalization  
  - Transcription using OpenAI Whisper  

  ⚠️ Some preprocessing scripts were **adapted from Favaro et al., 2023** ([Neuro-Logical/speech](https://github.com/Neuro-Logical/speech/tree/main/Multilingual_Evaluation/data_preprocessing)):  

  - `convert_to_16k.sh` → converts all audio recordings to a uniform **16 kHz sampling rate**.  
  - `loudness_norm.sh` → applies **volume normalization** across recordings to ensure consistency.  
  - `get_speech_transcripts.py` → transcribes audio files into text using **Whisper**.  

  In addition, the `requirements.txt` file for the preprocessing pipeline was taken from Favaro et al., 2023 and may include packages not required for this project.  

  Scripts were modified to run on macOS and adapted to the datasets used in this work. Attribution is explicitly provided in both the script headers and this README.  

- **`WER_CER/`**  
  Jupyter notebooks for WER and CER computation on datasets (e.g., Bari, Molinette, PC-GITA).  
  Workflow includes:
  1. Loading transcriptions and metadata (group, task, UPDRS scores).  
  2. Calculating WER and CER.  
  3. Outlier removal via Tukey’s IQR.  
  4. Statistical tests (Shapiro-Wilk, t-test, Mann-Whitney U, Kruskal-Wallis, Dunn post hoc).  
  5. Visualization (boxplots, bar plots with significance indicators).  
  6. Export of summary statistics to Excel.  

---

### 2. Classification Task
Binary classification of sustained vowel recordings from **healthy controls vs. PD patients**, using transformer architectures.

- **`Preprocessing_Transformers/`**  
  Scripts for preparing data for model input:
  - Resampling & standardization  
  - Spectrogram generation (e.g., Mel-spectrograms)  
  - Feature extraction for transformers  

- **Transformer models** (Jupyter notebooks):  
  - `ViT.ipynb` – Vision Transformer  
  - `ViT_parallel.ipynb` – parallel variant  
  - `AST.ipynb` – Audio Spectrogram Transformer  
  - `AST_parallel.ipynb` – parallel variant  

Each notebook includes:
- Data loading & splitting  
- Model definition & training loop  
- Validation and evaluation (accuracy, precision, recall, F1-score)  
- Training curves and metrics logging  

Parallel variants aim to reduce overfitting through stronger regularization and parallelization strategies.  

---

## ⚙️ Installation

Clone the repository and set up a Python environment:

```bash
git clone https://github.com/username/MasterThesis_Speech_PD.git
cd MasterThesis_Speech_PD

# (Recommended) Create virtual environment
conda create -n speechpd python=3.10
conda activate speechpd

# Install dependencies
pip install -r requirements.txt
```
> **Note:** The transformer notebooks were run on **Google Colab** to take advantage of GPU acceleration. They are designed for Colab but can also be executed locally if a GPU is available.



## 🚀 Usage

### Biomarkers Task

```bash
# Navigate to preprocessing
cd BiomarkersTask/Preprocessing_Biomarkers

# Resample and normalize audio
bash convert_to_16k.sh
bash loudness_norm.sh

# Transcribe audio
python get_speech_transcripts.py --input ./audio --output ./transcripts
WER and CER can then be computed using the Jupyter notebooks in WER_CER/.
```

### Classification Task
```bash

# Open and run the desired transformer notebook
jupyter notebook ClassificationTask/ViT.ipynb
```

Other models (ViT_parallel.ipynb, AST.ipynb, AST_parallel.ipynb) can be run similarly.
Each notebook contains preprocessing, training, and evaluation steps.

> **Tip:** For best performance, open the notebooks directly in **Google Colab** (with GPU enabled). They were developed and tested in Colab for this reason.




## 📊 Results
Significant differences in WER and CER were found between PD patients and controls, correlating with UPDRS scores.

Transformer-based classifiers achieved robust performance in distinguishing PD from healthy controls.

Explainability methods (heatmaps on Mel-spectrograms) were explored for highlighting relevant spectral regions.

For detailed results, refer to the full thesis.

## 📚 References
Favaro, A., Moro-Velázquez, L., Butala, A., Motley, C., Cao, T., Stevens, R. D., Villalba, J., & Dehak, N. (2023).
Multilingual evaluation of interpretable biomarkers to represent language and speech patterns in Parkinson's disease.
Frontiers in Neurology, 14:1142642. Link

## 👩‍🎓 Author
Benedetta Perrone
Master’s Thesis in Biomedical Engineering
Politecnico di Torino – A.Y. 2023/2024


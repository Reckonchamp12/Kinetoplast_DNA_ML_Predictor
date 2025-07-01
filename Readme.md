# Kinetoplast DNA ML Predictor

This repository contains the machine learning models and associated code developed during my research internship at the Massachusetts Institute of Technology (MIT) from November 2024 to March 2025.

## 🔬 Project Overview

The project focuses on predicting kinetoplast DNA deformation patterns and equilibrium states using supervised machine learning models trained on features extracted from molecular dynamics (MD) simulations conducted with GROMACS.

Key highlights:
- Feature extraction from MD simulation trajectories (e.g., shape anisotropy, relaxation time, bending rigidity).
- Model training using Random Forest and Gradient Boosting algorithms.
- Significant reduction in simulation runtime by replacing full MD runs with ML predictions.
- Integration of ML pipeline with GROMACS workflows for real-time analysis.

> ⚠️ **Note:** The dataset used in this project is proprietary and covered under a Non-Disclosure Agreement (NDA), and hence is not available in this repository.

## 📂 Repository Structure

```
kinetoplast-ml-predictor/
│
├── src/ # Python scripts
│ ├── extract_features.py # Parses GROMACS output, computes features
│ ├── train_model.py # Trains RF & GB models
│ ├── predict_dna_shape.py # Makes predictions using trained models
│ └── utils.py # Helper functions
│
├── models/ # Saved trained model files (.pkl)
│ └── README.md # Info about model structure and performance
│
├── notebooks/ # Jupyter notebooks for experimentation and analysis
│ ├── EDA.ipynb
│ └── Model_Evaluation.ipynb
│
├── LICENSE
├── .gitignore
└── README.md
```

## 🧠 ML Models Used

- **Random Forest Regressor**
- **Gradient Boosting Regressor**

These models were trained to predict:
- DNA bending rigidity
- Deformation patterns (via PCA-reduced structural modes)
- Equilibrium state parameters under varied simulation environments

## 🔗 GROMACS Integration

The trained models were integrated with GROMACS simulation workflows to allow:
- Real-time feature extraction
- Live prediction of DNA structure evolution
- Rapid scanning of environmental parameters for experimental planning

## 🛡 Disclaimer

This project is a research prototype and should not be used for clinical or diagnostic purposes. The data is confidential and cannot be shared publicly.

---

MIT © 2025

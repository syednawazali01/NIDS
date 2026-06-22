# Network Intrusion Detection System (NIDS)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0+-red.svg)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A machine learning-based Network Intrusion Detection System built with Python, featuring multiple classification models and an interactive Streamlit web interface for real-time threat detection and analysis.

**Table of Contents**
- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Models](#-models)
- [Dataset](#-dataset)
- [Configuration](#-configuration)
- [Performance](#-performance)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## 🎯 Overview

This project implements a comprehensive intrusion detection system that classifies network traffic as either normal or malicious. It uses the KDD Cup dataset for training and employs multiple machine learning algorithms to achieve high accuracy in detecting network attacks.

## ✨ Features

- **Multiple ML Models**: Support for various algorithms:
  - Support Vector Machine (SVM)
  - Multi-Layer Perceptron (MLP) Neural Network
  - Random Forest Classifier
  - Ensemble approaches with model selection

- **Interactive Web Interface**: 
  - Streamlit-based dashboard for easy interaction
  - Real-time prediction capabilities
  - Network packet sniffing (via Scapy)
  - Detailed threat analysis and visualization

- **Data Processing**:
  - Automatic feature encoding and scaling
  - Binary classification (Normal/Attack)
  - Support for KDD Cup dataset format

- **Model Management**:
  - Pre-trained models available in `models/` directory
  - Model serialization using joblib
  - Feature encoders and scalers included

## 📋 Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`:
  - streamlit >= 1.0
  - pandas >= 1.0
  - numpy >= 1.19
  - joblib >= 1.0
  - scapy >= 2.4
  - scikit-learn >= 1.0

## 🚀 Installation

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/syednawazali01/NIDS.git
   cd NIDS
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Linux/Mac**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Manual Installation (without Git)

1. Download the project as ZIP and extract it
2. Navigate to the project directory
3. Follow steps 2-4 above

## 📁 Project Structure

```
.
├── app.py                      # Streamlit web application
├── train_model.py              # Model training script
├── test_models.py              # Model testing and evaluation
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/
│   ├── KDDTrain+.txt          # Training dataset
│   └── KDDTest+.txt           # Testing dataset
└── models/
    ├── best_model.joblib      # Best performing model
    ├── best_model_name.joblib # Model selection reference
    ├── rf_model.joblib        # Random Forest model
    ├── mlp_model.joblib       # Neural Network model
    ├── svm_model.joblib       # SVM model
    ├── scaler.joblib          # Feature scaler
    ├── encoders.joblib        # Categorical encoders
    └── feature_names.joblib   # Feature name mapping
```

## 🎮 Usage

### 1. Train Models
To train new models on the KDD Cup dataset:

```bash
python train_model.py
```

This script will:
- Load the training and test datasets
- Preprocess features and encode categorical variables
- Train multiple ML models
- Evaluate and save the best performing model

### 2. Test Models
To evaluate model performance:

```bash
python test_models.py
```

### 3. Run the Web Application
Launch the interactive Streamlit dashboard:

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

The web interface provides:
- Model predictions on custom network traffic data
- Real-time network packet analysis (if Scapy is available)
- Performance metrics and visualizations
- Attack vs. Normal traffic statistics

## 🧠 Models

The system includes pre-trained models optimized for network intrusion detection:

| Model | Algorithm | Purpose |
|-------|-----------|---------|
| `best_model.joblib` | Ensemble/Best Performer | Primary classification model |
| `svm_model.joblib` | Support Vector Machine | Binary classification |
| `mlp_model.joblib` | Multi-Layer Perceptron | Neural network approach |
| `rf_model.joblib` | Random Forest | Tree-based ensemble |

Supporting files:
- `scaler.joblib`: StandardScaler for feature normalization
- `encoders.joblib`: LabelEncoders for categorical features
- `feature_names.joblib`: Feature column names and order

## 📊 Dataset

The project uses the **KDD Cup 1999 Dataset**, a benchmark dataset for network intrusion detection research:

- **Training Set**: KDDTrain+.txt (contains labeled network connections)
- **Test Set**: KDDTest+.txt (for model evaluation)
- **Features**: 41 network traffic features
- **Target**: Binary classification (Normal/Attack)

### Feature Categories:
- Basic connection features (duration, protocol, service)
- Content-based features (hot, logged_in, compromised, etc.)
- Traffic-based features (count, srv_count, rates)
- Host-based features (dst_host_count, serror_rate, etc.)

## 🔧 Configuration

No additional configuration files are needed. All settings are embedded in the Python scripts:

- Model hyperparameters can be adjusted in `train_model.py`
- UI styling and layout can be customized in `app.py`
- Dataset paths are defined at the top of `train_model.py`

## 📈 Performance

The system achieves high accuracy in detecting network intrusions:
- Trained on KDD Cup 1999 dataset
- Multiple model comparison and selection
- Cross-validation for robust performance estimation

Run `test_models.py` to see detailed classification reports including:
- Accuracy, Precision, Recall, F1-Score
- Confusion matrices
- Per-class performance metrics

## ⚠️ Important Notes

- **Scapy Dependency**: Real-time packet sniffing in the web app requires Scapy. On Windows, this may require WinPcap or Npcap drivers. The application gracefully handles missing Scapy installation.

- **Binary Classification**: The system uses binary classification (Normal/Attack). Multi-class classification can be implemented by modifying the label preprocessing in `train_model.py`.

- **Dataset Size**: The KDD Cup dataset is large (~5MB). Initial model training may take several minutes depending on your system.

## 🛠️ Development

To customize or extend the project:

1. **Add new models**: Modify `train_model.py` to include additional classifiers
2. **Improve features**: Enhance feature engineering in the preprocessing section
3. **Extend UI**: Add new pages or features to the Streamlit application in `app.py`
4. **Optimize performance**: Experiment with hyperparameter tuning

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository** on GitHub
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and test thoroughly
4. **Commit your changes** with clear messages
   ```bash
   git commit -m "Add description of your changes"
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** with a clear description of your changes

### Development Guidelines
- Maintain consistent code style
- Add comments for complex logic
- Test with the provided test datasets
- Update README.md if adding new features
- Follow PEP 8 Python style guide

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. **Scapy Installation Fails on Windows**
**Problem**: Packet sniffing features don't work
**Solution**: 
- Install WinPcap or Npcap drivers: https://nmap.org/npcap/
- Or use WSL (Windows Subsystem for Linux)
- The app will still work without Scapy for model predictions

#### 2. **ModuleNotFoundError: No module named 'streamlit'**
**Problem**: Streamlit not installed
**Solution**:
```bash
pip install -r requirements.txt
# or specifically
pip install streamlit>=1.0
```

#### 3. **Dataset Files Not Found**
**Problem**: KDD training/test data missing
**Solution**:
- Ensure `data/` folder exists with `KDDTrain+.txt` and `KDDTest+.txt`
- Download from: http://kdd.ics.uci.edu/databases/kddcup99/

#### 4. **Models Folder Empty**
**Problem**: Pre-trained models missing
**Solution**:
```bash
python train_model.py
# This will train and save models to the models/ directory
```

#### 5. **Port Already in Use Error**
**Problem**: Streamlit port 8501 is occupied
**Solution**:
```bash
streamlit run app.py --server.port 8502
```

#### 6. **Low Model Accuracy**
**Problem**: Predictions seem inaccurate
**Solution**:
- Check if dataset is correctly loaded
- Verify feature scaling is applied
- Consider retraining with `python train_model.py`
- Review feature preprocessing in training script

### Getting Help

- 📖 **Check the code comments** in each Python file
- 🔍 **Review the docstrings** in functions and classes
- ❓ **Open an issue** on GitHub with:
  - Description of the problem
  - Steps to reproduce
  - Your system information (OS, Python version)
  - Error messages or logs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
- **Streamlit**: Apache License 2.0
- **scikit-learn**: BSD License
- **Pandas**: BSD License
- **NumPy**: BSD License

## 📚 References

- **Dataset**: [KDD Cup 1999 Database](http://kdd.ics.uci.edu/databases/kddcup99/)
- **Streamlit Docs**: https://docs.streamlit.io/
- **scikit-learn Docs**: https://scikit-learn.org/stable/documentation.html
- **Scapy Documentation**: https://scapy.readthedocs.io/

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io) for interactive UI
- Machine learning powered by [scikit-learn](https://scikit-learn.org)
- Data processing with [Pandas](https://pandas.pydata.org)

---

**Last Updated**: 2026-06-22  
**Status**: Active Development

For questions or suggestions, feel free to open an issue on GitHub!


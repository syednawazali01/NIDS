# 🛡️ NIDS - Network Intrusion Detection System

**College Mini Project** | Machine Learning-based Network Security Detection

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0+-red.svg)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A professional network intrusion detection system built with Python, featuring multiple ML models and an interactive Streamlit interface for real-time threat analysis.

## 📂 Project Structure

```
NIDS/
├── src/                          # 🔧 SOURCE CODE
│   ├── app.py                    # Streamlit web interface
│   ├── train_model.py            # Model training
│   └── test_models.py            # Model evaluation
│
├── docs/                         # 📚 DOCUMENTATION
│   ├── README.md                 # Full project documentation
│   ├── QUICKSTART.md             # 5-minute setup guide
│   ├── DEVELOPMENT.md            # Development setup
│   ├── DEPLOYMENT.md             # Production deployment
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md        # Community standards
│   ├── SECURITY.md               # Security policy
│   ├── CHANGELOG.md              # Version history
│   └── ...
│
├── config/                       # ⚙️ CONFIGURATION
│   ├── pyproject.toml
│   ├── setup.cfg
│   ├── Makefile
│   ├── tox.ini
│   └── ...
│
├── data/                         # 📊 DATASETS
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
│
├── models/                       # 🤖 TRAINED MODELS
│   ├── best_model.joblib
│   ├── rf_model.joblib
│   ├── scaler.joblib
│   └── encoders.joblib
│
├── .github/                      # 🐙 GITHUB
│   ├── workflows/                # CI/CD pipelines
│   └── ISSUE_TEMPLATE/           # Issue templates
│
├── Dockerfile                    # 🐳 DOCKER
├── docker-compose.yml
├── requirements.txt              # Python dependencies
└── LICENSE                       # MIT License
```

## 🚀 Quick Start

### Installation (3 steps)

```bash
# 1. Clone & enter project
git clone https://github.com/syednawazali01/NIDS.git
cd NIDS

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # Windows PowerShell
# or: source .venv/bin/activate  # Linux/Mac

# 3. Install & run
pip install -r requirements.txt
streamlit run src/app.py
```

### With Docker

```bash
docker-compose up
# Open http://localhost:8501
```

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [**docs/README.md**](docs/README.md) | Complete project documentation |
| [**docs/QUICKSTART.md**](docs/QUICKSTART.md) | 5-minute setup guide |
| [**docs/DEVELOPMENT.md**](docs/DEVELOPMENT.md) | Development environment setup |
| [**docs/DEPLOYMENT.md**](docs/DEPLOYMENT.md) | Production deployment guide |
| [**docs/CONTRIBUTING.md**](docs/CONTRIBUTING.md) | How to contribute |
| [**docs/SECURITY.md**](docs/SECURITY.md) | Security policy |

## ✨ Features

- **🧠 Multiple ML Models**: Random Forest, SVM, Neural Networks
- **🖥️ Web Interface**: Interactive Streamlit dashboard
- **📡 Real-time Detection**: Live network traffic analysis
- **📊 Model Comparison**: Compare model accuracy
- **🎨 Modern UI**: Dark theme with real-time visualization
- **🔄 Batch Processing**: Analyze multiple packets at once

## 📋 Usage

### Manual Detection

```bash
streamlit run src/app.py
# Go to "Detection" tab → Input network features → Get prediction
```

### Train Models

```bash
python src/train_model.py
```

### Test Models

```bash
python src/test_models.py
```

## 🛠️ Commands

```bash
# Development
pip install -r requirements.txt
python -m venv .venv

# Run application
streamlit run src/app.py

# Train models
python src/train_model.py

# Using Makefile (if installed)
make run           # Start app
make train        # Train models
make test-models  # Evaluate
make format       # Format code
make lint         # Check style
```

## 📚 Project Details

- **Dataset**: KDD Cup 1999 (41 features)
- **Target**: Binary classification (Normal/Attack)
- **Models**: Random Forest (primary), SVM, MLP
- **Framework**: Streamlit, scikit-learn
- **Deployment**: Docker, GitHub Actions

## 🎯 About This Project

This is a **college mini project** demonstrating:
- Machine learning fundamentals
- Network security concepts
- Full-stack Python development
- Professional project structure
- GitHub best practices

Perfect for portfolio or learning purposes!

## 🤝 Contributing

We welcome contributions! See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

## 📞 Support

- 📖 [Full Documentation](docs/README.md)
- 🚀 [Quick Start Guide](docs/QUICKSTART.md)
- 💬 [Open an Issue](https://github.com/syednawazali01/NIDS/issues)
- 🔧 [Development Guide](docs/DEVELOPMENT.md)

---

**Made with ❤️ for learning and security** 🛡️

Repository: https://github.com/syednawazali01/NIDS

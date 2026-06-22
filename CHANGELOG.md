# Changelog

All notable changes to the Network Intrusion Detection System project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-22

### Added
- Initial release of NIDS (Network Intrusion Detection System)
- Multiple ML models: SVM, MLP Neural Network, Random Forest
- Interactive Streamlit web interface
- Real-time network packet analysis with Scapy
- Model training and evaluation scripts
- Support for KDD Cup 1999 dataset
- Comprehensive documentation (README, Contributing guide, Code of Conduct)
- .gitignore and LICENSE files for GitHub
- Feature scaling and categorical encoding
- Model serialization with joblib
- Binary classification (Normal/Attack)

### Features
- **Models**:
  - Support Vector Machine (SVM) classifier
  - Multi-Layer Perceptron (MLP) neural network
  - Random Forest ensemble classifier
  - Model selection and ensemble approach

- **Web Interface**:
  - Beautiful Streamlit dashboard with dark theme
  - Real-time prediction capabilities
  - Network packet sniffing (optional, with Scapy)
  - Performance metrics visualization
  - Attack vs. Normal traffic statistics

- **Data Processing**:
  - Automatic feature preprocessing
  - Label encoding for categorical variables
  - Standard scaling for numerical features
  - Support for large datasets (KDD Cup format)

### Documentation
- Comprehensive README with installation and usage instructions
- CONTRIBUTING.md with contribution guidelines
- CODE_OF_CONDUCT.md for community standards
- Inline code comments and docstrings
- Dataset documentation

## Future Versions

### Planned for v1.1.0
- [ ] Multi-class classification (6-class attack types)
- [ ] Cross-validation and hyperparameter tuning
- [ ] Model performance comparison charts
- [ ] Export predictions to CSV
- [ ] API endpoint for model serving

### Planned for v1.2.0
- [ ] Deep learning models (LSTM, CNN)
- [ ] Feature importance analysis
- [ ] Anomaly detection algorithms
- [ ] Real-time training pipeline
- [ ] Docker containerization

### Planned for v2.0.0
- [ ] Web API with Flask/FastAPI
- [ ] Database integration for storing predictions
- [ ] Advanced visualization dashboards
- [ ] Distributed training support
- [ ] Mobile application

## [Unreleased]

### Under Development
- Performance optimizations
- Additional test coverage
- GitHub Actions CI/CD pipeline

---

For detailed information about upcoming features, check the [Issues](../../issues) and [Discussions](../../discussions) sections.

### How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for information about how to contribute to this project.

### Versioning

This project uses [Semantic Versioning](https://semver.org/):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

### Release Schedule

- Major releases: As needed
- Minor releases: Quarterly
- Patch releases: As needed

---

Last Updated: 2026-06-22

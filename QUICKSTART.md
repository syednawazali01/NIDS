# Quick Start Guide

Get the Network Intrusion Detection System up and running in minutes!

## Prerequisites

- Python 3.7 or higher
- pip (comes with Python)
- Git (for cloning)

## 🚀 Fastest Way: With Docker

If you have Docker installed, you can run NIDS instantly:

```bash
# Clone the repository
git clone https://github.com/syednawazali01/NIDS.git
cd NIDS

# Run with Docker Compose
docker-compose up
```

Then open your browser to: **http://localhost:8501**

## ⚡ Quick Installation (5 minutes)

### 1. Clone the Repository

```bash
git clone https://github.com/syednawazali01/NIDS.git
cd NIDS
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

Your browser will automatically open to: **http://localhost:8501**

## 📚 Using the Application

### Making Predictions

1. Navigate to the **"Predict"** section in the sidebar
2. Input network traffic features (or use example data)
3. Click **"Predict"** button
4. View results: **Normal** or **Attack**

### Viewing Statistics

1. Go to **"Analytics"** tab
2. See real-time attack/normal traffic statistics
3. View model performance metrics

### Real-time Monitoring (Optional)

If Scapy is installed:

1. Go to **"Network Monitor"** section
2. Click **"Start Sniffing"**
3. Watch live network packets being analyzed
4. View real-time classification results

## 🎓 Train Your Own Models

```bash
# Train new models with the KDD dataset
python train_model.py
```

The script will:
- Load training and test data
- Preprocess features
- Train multiple models
- Save the best model and encoders

## ✅ Test the Models

```bash
# Evaluate model performance
python test_models.py
```

View accuracy, precision, recall, and classification reports.

## 🛠️ Common Commands

### Using Make (if you have it installed)

```bash
make help          # Show all available commands
make run           # Run the web app
make train         # Train models
make test-models   # Test models
make clean         # Remove cache files
make lint          # Check code style
make format        # Format code
```

### Without Make

```bash
# Run web application
streamlit run app.py

# Train models
python train_model.py

# Test models
python test_models.py

# Check for code style issues
flake8 .

# Format code
black .
```

## 📊 Understanding the Data

The system works with network traffic data with 41 features:

### Example Features:
- `duration`: Connection duration in seconds
- `protocol_type`: Protocol (tcp, udp, icmp)
- `src_bytes`: Bytes sent from source
- `dst_bytes`: Bytes sent to destination
- `flag`: Connection state (S0, S1, RSTO, etc.)

### Labels:
- **Normal**: Legitimate network traffic (0)
- **Attack**: Malicious network traffic (1)

The pre-trained models can classify these features as either normal or attack traffic.

## 🔍 Understanding Results

### Prediction Output

```
🎯 Prediction: NORMAL ✓
Confidence: 98.5%
Status: Low Risk
```

Or for attacks:

```
⚠️ Prediction: ATTACK ❌
Confidence: 95.2%
Status: High Risk
```

## 🐛 Troubleshooting

### Port 8501 Already in Use

```bash
streamlit run app.py --server.port 8502
```

### Scapy Installation Issues (Windows)

```bash
# Install these first:
pip install pywin32
# Or use Windows Subsystem for Linux (WSL)
```

### Models Not Found

Train the models first:
```bash
python train_model.py
```

### ModuleNotFoundError

Make sure you're in the virtual environment:
```bash
# Check virtual environment is active
pip list
# Should show streamlit, pandas, scikit-learn, etc.
```

## 📚 Next Steps

1. **Read the full [README.md](README.md)** for detailed documentation
2. **Check [CONTRIBUTING.md](CONTRIBUTING.md)** to contribute improvements
3. **Review [DEVELOPMENT.md](DEVELOPMENT.md)** for development setup
4. **See [SECURITY.md](SECURITY.md)** for security guidelines

## 🆘 Need Help?

- 📖 Check the main [README.md](README.md)
- 🔧 See [DEVELOPMENT.md](DEVELOPMENT.md) for troubleshooting
- 💬 Open a [GitHub Issue](https://github.com/syednawazali01/NIDS/issues)
- 🤝 See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## 📦 What You Get

✅ Interactive Streamlit Web Interface  
✅ Multiple Pre-trained ML Models  
✅ Real-time Network Analysis  
✅ Comprehensive Documentation  
✅ Ready for Production Deployment  
✅ Docker Support  
✅ Active Development & Support  

## 🚀 Deployment

Ready to deploy? See the [README.md](README.md) and [SECURITY.md](SECURITY.md) for:
- Production setup
- Security considerations
- Docker deployment
- HTTPS configuration
- API integration

---

**Congratulations! You're ready to detect network intrusions!** 🛡️

For more information, visit the [GitHub repository](https://github.com/syednawazali01/NIDS)

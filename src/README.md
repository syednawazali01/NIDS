# Run Application

This directory contains the main source code for the NIDS application.

## Files

- **app.py** - Main Streamlit web interface
- **train_model.py** - ML model training script  
- **test_models.py** - Model evaluation script

## Running the Application

```bash
# From project root directory
streamlit run src/app.py
```

## Project Structure

All paths in src/ files are relative to the project root:
- `../data/` - Training/test datasets
- `../models/` - Trained model files
- `../docs/` - Documentation

For more information, see [../README_ROOT.md](../README_ROOT.md)

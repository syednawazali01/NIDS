import joblib
from pathlib import Path

# Get paths for new structure
BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

model = joblib.load(MODELS_DIR / "best_model.joblib")
print("✅ Model loaded successfully")
print("Model type:", type(model).__name__)

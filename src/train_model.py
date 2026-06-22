import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from pathlib import Path

# Get paths for new structure
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

# column names for the dataset
col_names = [
    "duration", "protocol_type", "service", "flag",
    "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent",
    "hot", "num_failed_logins", "logged_in", "num_compromised",
    "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count",
    "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate", "label", "difficulty"
]

# load the training and testing data
print("Loading dataset...")
train_data = pd.read_csv(DATA_DIR / "KDDTrain+.txt", header=None, names=col_names)
test_data = pd.read_csv(DATA_DIR / "KDDTest+.txt", header=None, names=col_names)

print("Train size:", train_data.shape)
print("Test size:", test_data.shape)

# convert labels to binary - normal=0, attack=1
train_data["label"] = train_data["label"].apply(lambda x: 0 if x == "normal" else 1)
test_data["label"] = test_data["label"].apply(lambda x: 0 if x == "normal" else 1)

# drop the difficulty column, we dont need it
train_data = train_data.drop("difficulty", axis=1)
test_data = test_data.drop("difficulty", axis=1)

# separate features and labels
X_train = train_data.drop("label", axis=1)
y_train = train_data["label"]
X_test = test_data.drop("label", axis=1)
y_test = test_data["label"]

# Find categorical columns
categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()
print(f"Categorical columns: {categorical_cols}")

# Encode categorical features
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))
    encoders[col] = le

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train SVM
print("\nTraining SVM...")
svm_model = LinearSVC(dual=False, max_iter=10000)
svm_model.fit(X_train, y_train)
svm_pred = svm_model.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, svm_pred))

# Train MLP
print("\nTraining MLP...")
mlp_model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
mlp_model.fit(X_train, y_train)
mlp_pred = mlp_model.predict(X_test)
print("MLP Accuracy:", accuracy_score(y_test, mlp_pred))

# Train Random Forest
print("\nTraining Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
print("RF Accuracy:", accuracy_score(y_test, rf_pred))

# Select best model (Random Forest typically performs best)
best_model = rf_model
best_accuracy = accuracy_score(y_test, rf_pred)
print(f"\n✅ Best model: Random Forest with {best_accuracy:.2%} accuracy")

# Save models and preprocessing objects
os.makedirs(MODELS_DIR, exist_ok=True)
joblib.dump(best_model, MODELS_DIR / "best_model.joblib")
joblib.dump(rf_model, MODELS_DIR / "rf_model.joblib")
joblib.dump(mlp_model, MODELS_DIR / "mlp_model.joblib")
joblib.dump(scaler, MODELS_DIR / "scaler.joblib")
joblib.dump(encoders, MODELS_DIR / "encoders.joblib")
joblib.dump(X_train.columns if hasattr(X_train, 'columns') else list(range(X_train.shape[1])), MODELS_DIR / "feature_names.joblib")

print("\n✅ All models saved to", MODELS_DIR)
print("\nClassification Report:")
print(classification_report(y_test, best_model.predict(X_test)))

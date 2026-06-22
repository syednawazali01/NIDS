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
train_data = pd.read_csv("data/KDDTrain+.txt", header=None, names=col_names)
test_data = pd.read_csv("data/KDDTest+.txt", header=None, names=col_names)

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

# encode the text columns (protocol_type, service, flag)
print("Encoding categorical columns...")
encoders = {}
for col in ["protocol_type", "service", "flag"]:
    le = LabelEncoder()
    # fit on both train and test so no unknown values
    combined = pd.concat([X_train[col], X_test[col]])
    le.fit(combined)
    X_train[col] = le.transform(X_train[col])
    X_test[col] = le.transform(X_test[col])
    encoders[col] = le

# scale all features using standard scaler
print("Scaling features...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

feature_names = [c for c in train_data.columns if c != "label"]

# train SVM model
print("Training SVM model...")
base_svm = LinearSVC(C=1.0, class_weight="balanced", random_state=42)
svm = CalibratedClassifierCV(base_svm)
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
svm_acc = accuracy_score(y_test, svm_pred)
print("SVM Accuracy:", round(svm_acc * 100, 2), "%")
print(classification_report(y_test, svm_pred, target_names=["Normal", "Attack"]))

# train MLP (neural network) model
print("Training MLP Neural Network...")
mlp = MLPClassifier(hidden_layer_sizes=(100, 50, 25), early_stopping=True, max_iter=100, random_state=42)
mlp.fit(X_train, y_train)
mlp_pred = mlp.predict(X_test)
mlp_acc = accuracy_score(y_test, mlp_pred)
print("MLP Accuracy:", round(mlp_acc * 100, 2), "%")
print(classification_report(y_test, mlp_pred, target_names=["Normal", "Attack"]))

# train random forest model
print("Training Random Forest...")
rf = RandomForestClassifier(n_estimators=100, class_weight="balanced", n_jobs=-1, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", round(rf_acc * 100, 2), "%")
print(classification_report(y_test, rf_pred, target_names=["Normal", "Attack"]))

# pick the best model out of all three
accuracies = {"SVM": svm_acc, "MLP": mlp_acc, "Random Forest": rf_acc}
best_name = max(accuracies, key=accuracies.get)
best_model = {"SVM": svm, "MLP": mlp, "Random Forest": rf}[best_name]
print("Best model:", best_name, "with accuracy", round(accuracies[best_name] * 100, 2), "%")

# save the model and other files needed for the app
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_model.joblib")
joblib.dump(scaler, "models/scaler.joblib")
joblib.dump(encoders, "models/encoders.joblib")
joblib.dump(feature_names, "models/feature_names.joblib")

print("Model saved successfully!")
print("Now run: python -m streamlit run app.py")
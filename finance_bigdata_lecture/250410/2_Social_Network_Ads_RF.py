import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("../data/Social_Network_Ads.csv", index_col=0)
# print(df.head())

# 2. LabelEncoder를 이용한 숫자형 카테고리 변환
label_encoder = LabelEncoder()
df['Gender']= label_encoder.fit_transform(df['Gender'])

# 3. X와 y
X = df.drop(['Purchased'], axis=1)
y = df['Purchased']

# 4. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 랜덤 포레스트
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# 6. Make predictions on the testing set
y_pred = rf.predict(X_test)
y_pred_proba = rf.predict_proba(X_test)[:, 1]

# Evaluate the model
print("정확도:", accuracy_score(y_test, y_pred))
print("분류 보고서(Classification Report):")
print(classification_report(y_test, y_pred))
print("혼동 행렬(Confusion Matrix):")
print(confusion_matrix(y_test, y_pred))

# 7. Plot the ROC curve
auc = roc_auc_score(y_test, y_pred_proba)
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()

# 8. 변수 중요도(feature importance) 계산하기
importances = rf.feature_importances_
feature_names = X.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# 표 시각화
print("\n[📊 Feature Importances from Decision Tree]")
print(importance_df)


# 9. 예측하기
# 예: Gender = 1 (남성), Age = 72, EstimatedSalary = 35000
sample = pd.DataFrame([[0, 28, 35000]], columns=['Gender', 'Age', 'EstimatedSalary'])

# 예측
prediction = rf.predict(sample)[0]
probability = rf.predict_proba(sample)[0][1]

print(f"예측된 구매 여부: {'구매함' if prediction == 1 else '구매 안 함'}")
print(f"구매 확률: {probability:.2%}")

# 트리 계열 중 랜덤 포레스트를 추천한다
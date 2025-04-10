import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import graphviz

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

# 5. Create a decision tree classifier
clf = DecisionTreeClassifier(random_state=42, max_depth=5)

# Train the model
clf.fit(X_train, y_train)

# 5-1. graphviz
dot_data = export_graphviz(clf, out_file="tree.dot", feature_names=X.columns, class_names=clf.classes_, filled=True)
print(dot_data)


# 6. 변수 중요도(feature importance) 계산하기
importances = clf.feature_importances_
feature_names = X.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# 표 시각화
print("\n[📊 Feature Importances from Decision Tree]")
print(importance_df)


# 7. Make predictions on the testing set
y_pred = clf.predict(X_test)
y_pred_proba = clf.predict_proba(X_test)[:, 1]
# print(y_pred_proba)

# Evaluate the model
print("정확도:", accuracy_score(y_test, y_pred))
print("분류 보고서(Classification Report):")
print(classification_report(y_test, y_pred))
print("혼동 행렬(Confusion Matrix):")
print(confusion_matrix(y_test, y_pred))


# 8. Plot the ROC curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()

# 9. 예측하기
# 예: Gender = 1 (남성), Age = 72, EstimatedSalary = 35000
sample = pd.DataFrame([[1, 72, 35000]], columns=['Gender', 'Age', 'EstimatedSalary'])

# 예측
prediction = clf.predict(sample)[0]
probability = clf.predict_proba(sample)[0][1]

print(f"예측된 구매 여부: {'구매함' if prediction == 1 else '구매 안 함'}")
print(f"구매 확률: {probability:.2%}")
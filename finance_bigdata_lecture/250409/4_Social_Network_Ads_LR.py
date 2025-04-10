import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# 1. 데이터 불러오기
data_path = './data/Social_Network_Ads_outlier_removed.csv'
df = pd.read_csv(data_path)

print("데이터 크기:", df.shape)
print("컬럼 목록:", df.columns.tolist())

# 2. Label Encoding
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])

# 3. 피처와 타깃 변수 분리
X = df.drop('Purchased', axis=1)
y = df['Purchased']

# 4. 학습/테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. 불필요한 컬럼 제거
X_train_1 = X_train.drop(['Gender', 'User ID'], axis=1)
X_test_1 = X_test.drop(['Gender', 'User ID'], axis=1)

# 6. MinMax 스케일링
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train_1)
X_test_scaled = scaler.transform(X_test_1)

# 7. 로지스틱 회귀 모델 정의
model = LogisticRegression(
    penalty="l1",
    dual=False,
    tol=0.0001,
    C=10,
    fit_intercept=True,
    intercept_scaling=1,
    class_weight=None,
    random_state=42,
    solver='liblinear',
    max_iter=1000,
    multi_class='auto',  # deprecated -> auto로 수정
    verbose=0,
    warm_start=False,
    n_jobs=None,
    l1_ratio=None
)

# 8. 모델 학습
model.fit(X_train_scaled, y_train)

# 9. 예측
y_pred = model.predict(X_test_scaled)

# 10. 평가 지표 출력
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)
y_proba = model.predict_proba(X_test_scaled)[:, 1]
roc_auc = roc_auc_score(y_test, y_proba)

print("정확도(Accuracy): {:.2f}".format(accuracy))
print("혼동 행렬(Confusion Matrix):")
print(conf_matrix)
print("분류 보고서(Classification Report):")
print(class_report)
print("ROC AUC SCORE (predict_proba 기반): {:.4f}".format(roc_auc))

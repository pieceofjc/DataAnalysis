# 🚗 SUV 구매 예측 분석 (Logistic Regression)

사회적 네트워크 광고 데이터를 기반으로, 성별, 나이, 연봉에 따라 SUV 구매 여부를 예측한 로지스틱 회귀 프로젝트입니다.

---

## 📌 프로젝트 요약

- **데이터 출처**: [Kaggle - SUV Data](https://www.kaggle.com/datasets/iamaniket/suv-data)
- **분석 목적**: 사용자 특성(성별, 나이, 연봉) 기반 SUV 구매 가능성 예측
- **주요 기법**: 로지스틱 회귀, 정규화, ROC 곡선, 혼동 행렬

---

## 🔍 분석 프로세스

1. **데이터 로드 및 전처리**
   - CSV 파일 불러오기
   - `Gender` 변수는 LabelEncoder로 숫자형 변환
   - 독립변수(X)와 종속변수(y) 분리

2. **데이터 분할**
   - 학습셋과 테스트셋 (8:2)으로 분할

3. **스케일링**
   - `StandardScaler`로 정규화

4. **로지스틱 회귀 모델 학습**
   - `LogisticRegression` 사용하여 학습
   - 예측 및 확률 추정 수행

5. **모델 평가**
   - 정확도, 정밀도, 재현율, F1-score, ROC-AUC 등 확인
   - ROC 곡선 시각화

---

## 📌 핵심 결과 요약

| 평가 지표       | 값       |
|----------------|----------|
| 정확도 (Accuracy) | 0.875   |
| 정밀도 (Precision) | 0.90    |
| 재현율 (Recall)   | 0.75    |
| F1-score         | 0.82    |
| ROC AUC          | 0.93    |

- `Age`와 `EstimatedSalary`가 주요 영향 변수
- `Gender` 변수는 영향 미미 → 제거해도 성능에 큰 영향 없음
- 예측 결과를 확률로도 해석 가능 (의사결정에 유용)

---

## 🧰 사용 도구

- Python (pandas, matplotlib, seaborn)
- scikit-learn
- Jupyter Notebook

---

## 🧪 실행 방법

```bash
git clone https://github.com/your-id/suv-logistic-prediction.git
cd suv-logistic-prediction
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
jupyter notebook

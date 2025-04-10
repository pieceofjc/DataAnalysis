# 🚗 SUV 구매 예측 분석 (Decision Tree & Random Forest)

사회적 네트워크 광고 데이터를 바탕으로 SUV 구매 여부를 예측하는 모델을 구성하고 분석한 프로젝트입니다.

---

## 📌 프로젝트 요약

- **데이터 출처**: [Kaggle - SUV Data](https://www.kaggle.com/datasets/iamaniket/suv-data)
- **분석 목적**: 성별, 나이, 예상 급여를 기반으로 사용자가 SUV를 구매할 가능성 예측
- **주요 기법**: Decision Tree, Random Forest, 분류 평가 지표 시각화

---

## 🔍 분석 프로세스

1. **데이터 로드 및 구조 파악 & 전처리**
   - `Gender` 컬럼은 LabelEncoder로 숫자형 변환
   - 불필요한 인덱스 제거

2. **학습 데이터 분할**
   - 학습셋 80%, 테스트셋 20%로 분할

3. **모델링 및 예측**
   - **Decision Tree**
     - 깊이 제한 설정 (`max_depth=5`)
     - 변수 중요도 계산 및 시각화
   - **Random Forest**
     - `n_estimators=100`으로 앙상블 구성
     - 확률 예측값 기반 ROC 곡선 시각화

4. **모델 평가**
   - 정확도 (Accuracy)
   - 정밀도, 재현율, F1-score (classification report)
   - 혼동 행렬
   - ROC-AUC

---

## 📌 핵심 결과 요약

### 🎯 Decision Tree

| 평가 항목         | 결과 |
|------------------|------|
| 정확도 (Accuracy) | 93%  |
| 주요 변수         | Age (50.2%), EstimatedSalary (48.7%), Gender (1.1%) |

- `Gender` 변수는 예측에 거의 기여하지 않음 → 제거 고려 가능

### 🌲 Random Forest

| 평가 항목         | 결과  |
|------------------|-------|
| 정확도 (Accuracy) | 95%   |
| ROC AUC           | 0.97  |

- Decision Tree 대비 더 높은 정확도와 안정성 보임

---

## 🧰 사용 도구

- Python (pandas, matplotlib, seaborn)
- scikit-learn
- Jupyter Notebook

---

## 🧪 실행 방법

```bash
git clone https://github.com/your-id/suv-purchase-prediction.git
cd suv-purchase-prediction
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
jupyter notebook

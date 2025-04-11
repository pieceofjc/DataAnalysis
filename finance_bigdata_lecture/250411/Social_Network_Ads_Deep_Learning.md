# 🚗 SUV 구매 예측 분석 (DNN, LSTM, GRU)

사회적 네트워크 광고 데이터를 바탕으로 SUV 구매 여부를 예측하는 모델을 구성하고 분석한 프로젝트입니다.

---

## 📌 프로젝트 요약

- **데이터 출처**: [Kaggle - SUV Data](https://www.kaggle.com/datasets/iamaniket/suv-data)
- **분석 목적**: 성별, 나이, 예상 급여를 기반으로 사용자(예측할 데이터)가 SUV를 구매할 가능성 예측
- **주요 기법**: DNN, LSTM, GRU

---

## 🔍 분석 프로세스

1. **DNN**
    1. **데이터 로드 및 전처리**
        - 불필요한 인덱스 제거
    2. **학습 데이터 분할**
        - 학습셋 80%, 테스트셋 20%로 분할
    3. **스케일링**
        - StandardScaler를 이용하여 표준화
        - saler.save 파일로 저장
    4. **모델링**
        - 모델 구축
        - 컴파일
        - 훈련
    5. **테스트 데이터로 모델 평가**
        - 손실, 정확도 평가
    6. **모델 파일로 저장**
        - 구매예측_DNN.h5로 저장

2. **LSTM 및 GRU**
    1. **데이터 로드 및 전처리**
        - 불필요한 인덱스 제거
    2. **학습 데이터 분할**
        - 학습셋 80%, 테스트셋 20%로 분할
    3. **스케일링**
        - StandardScaler를 이용하여 표준화
        - saler.save 파일로 저장(공통)
    4. **모델링 함수**
        - 모델 생성
        - 컴파일
    5. **모델 학습 및 파일 저장**
        - 입력 데이터 형태 변환
        - EarlyStopping과 ModelCheckpoint 콜백 정의
        - 위 함수를 통해 학습
    5. **테스트 데이터로 모델 평가**
        - 손실, 정확도 평가
        - LSTM과 GRU 비교

3. **새로운 데이터로 예측하기 - predict.py**
    1. **세가지 모델을 학습한 파일을 로드하기**
    2. **예측할 데이터 가져오기**
        - 예측할 데이터 scaler.save로 스케일링하기
        - LSTM과 GRU를 위한 데이터 변환
    3. **예측 수행**
        - model.predict
    4. **결과 비교**
        - 표로 만들어서 출력
---

## 📌 핵심 결과 요약

### DNN (Deep Neural Network)

| 평가 항목         | 결과  |
|------------------|-------|
| 손실 (loss) | 14% |
| 정확도 (accuracy) | 94% |

- 손실이 가장 낮아 예측 오차가 상대적으로 작음
- 정확도는 약간 낮지만 안정적임
- 구조가 간단하고 학습 속도가 빠르기 때문에 베이스라인 모델로 매우 적합

### LSTM (Long Short-Term Memory)

| 평가 항목         | 결과  |
|------------------|-------|
| 손실 (loss) | 16% |
| 정확도 (accuracy) | 95% |

- 손실은 DNN보다 약간 높지만 정확도는 가장 높음
- 본 데이터셋은 LSTM의 장점인 시계열, 순차적 특성이 없어 크게 발휘되지 않음
- 예측 성능이 높으나, 학습 시간 및 자원 소모가 큼

### GRU (Gated Recurrent Unit)

| 평가 항목         | 결과  |
|------------------|-------|
| 손실 (loss) | 16% |
| 정확도 (accuracy) | 95% |

- LSTM과 거의 동일한 정확도와 손실
- 구조가 더 단순해 학습 속도는 빠르면서도 성능은 유사
- LSTM보다 효율적인 선택이 될 수 있음

### 모델 예측 비교

|모델|구매 확률|예측 결과|
|----|--------|-------|
|DNN|0.552266|구매|
|LSTM|0.447853|비구매|
|GRU|0.469788|비구매|

---

## 🧰 사용 도구

- Python (pandas)
- scikit-learn
- Tensorflow

---

## 🧪 실행 방법

```bash
git clone https://github.com/your-id/suv-purchase-prediction.git
cd suv-purchase-prediction
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
jupyter notebook

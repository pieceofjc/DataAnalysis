import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

# 모델명 리스트
model_name = ['DNN', 'LSTM', 'GRU']
models = [load_model(f"구매예측_{name}.h5") for name in model_name]

# 예측할 데이터 (22살, 30000)
data = np.array([[45, 50000]])

# 스케일러 로드
scaler = joblib.load('scaler.save')
new_data = scaler.transform(data)

# LSTM/GRU 입력을 위한 reshape (3D)
new_data_seq = new_data.reshape((new_data.shape[0], 1, new_data.shape[1]))

# 예측 수행 (모델 종류에 따라 입력 형태 다르게)
predictions = []
for name, model in zip(model_name, models):
    if name == 'DNN':
        pred = model.predict(new_data)[0][0]
    else:  # LSTM, GRU
        pred = model.predict(new_data_seq)[0][0]
    predictions.append(pred)

# 결과 정리
prediction_df = pd.DataFrame({
    "모델": model_name,
    "구매 확률": [round(p, 10) for p in predictions],
    "예측 결과": ["구매" if p >= 0.5 else "비구매" for p in predictions]
})

# 출력
print(f"---- {data[0][0]}세, 연봉 {data[0][1]}의 구매 예측 결과 ----")
print(prediction_df)

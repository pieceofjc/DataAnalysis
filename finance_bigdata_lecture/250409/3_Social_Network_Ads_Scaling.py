import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# matplotlib font 설정
import font

# scikit-learn에서 데이터 스케일링을 위한 라이브러리 임포트
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 1. 데이터 불러오기
# index_col=0: CSV 저장 시 인덱스가 함께 저장된 경우 제거
# encoding 옵션은 파일 인코딩에 맞게 조정 (예: 'utf-8' 또는 'cp949')
input_file = "./data/Social_outlier_removed.csv"
df = pd.read_csv(input_file, index_col=0, encoding="utf-8")

# 2. 전처리: 숫자형 변수 선택 (스케일링은 보통 숫자형 변수에 적용)
numeric_cols = df.select_dtypes(include=[np.number]).columns
print("\n스케일링 대상 숫자형 컬럼:")
print(numeric_cols.tolist())

# 3. 스케일링 전 데이터의 분포 시각화 (Box Plot)
plt.figure(figsize=(14, 6))
sns.boxplot(data=df[numeric_cols])
plt.title("스케일링 전 데이터 분포")
plt.show()

# 4. 데이터 스케일링

# 4-1. StandardScaler: 평균 0, 표준편차 1로 변환하는 방법 (표준화)
scaler_standard = StandardScaler()
# fit_transform을 통해 학습 및 변환 수행
data_standard_scaled = scaler_standard.fit_transform(df[numeric_cols])
# 결과를 DataFrame으로 변환 (원본 인덱스와 컬럼 유지)
df_standard_scaled = pd.DataFrame(data_standard_scaled, columns=numeric_cols, index=df.index)

# os.path 모듈을 이용하여 파일명과 확장자를 분리합니다.
dir_name = os.path.dirname(input_file)
base_name = os.path.splitext(os.path.basename(input_file))[0]
output_file = os.path.join(dir_name, base_name + "_standard_Scaled.csv")

df_standard_scaled.to_csv(output_file)

# 4-2. MinMaxScaler: 모든 값을 0~1 범위로 변환
scaler_minmax = MinMaxScaler()
data_minmax_scaled = scaler_minmax.fit_transform(df[numeric_cols])
df_minmax_scaled = pd.DataFrame(data_minmax_scaled, columns=numeric_cols, index=df.index)
output_file = os.path.join(dir_name, base_name + "_minmax_Scaled.csv")

df_minmax_scaled.to_csv(output_file)

# 5. 스케일링 결과 시각화

# StandardScaler와 MinMaxScaler 적용 후 Box Plot 비교
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=df_standard_scaled)
plt.title("StandardScaler 적용 후 데이터 분포")

plt.subplot(1, 2, 2)
sns.boxplot(data=df_minmax_scaled)
plt.title("MinMaxScaler 적용 후 데이터 분포")

plt.tight_layout()
plt.show()

# 6. 스케일링 결과 일부 출력하여 확인
print("\n[StandardScaler] 적용 후 데이터의 첫 5행:")
print(df_standard_scaled.head())

print("\n[MinMaxScaler] 적용 후 데이터의 첫 5행:")
print(df_minmax_scaled.head())
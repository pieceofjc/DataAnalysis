import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# matplotlib font 설정
import font

# VIF 계산을 위해 statsmodels 라이브러리 사용
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. 데이터 불러오기
# index_col=0 옵션을 사용하여 인덱스 컬럼이 포함되지 않도록 합니다.
df = pd.read_csv("./data/Advertising_standard_Scaled.csv", index_col=0, encoding="utf-8")
print("데이터의 첫 5행:")
print(df.head())

# 2. 상관행렬 확인 및 시각화
corr_matrix = df.corr()
print("\n상관행렬:")
print(corr_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="RdBu", center=0)
plt.title("독립 변수들 간의 상관행렬")
plt.show()

# 3. 분산 팽창 계수(VIF) 계산
# 숫자형 변수 대상으로 VIF 계산
# VIF 계산을 위해 DataFrame의 값을 numpy 배열로 변환합니다.
features = df.columns
X = df.values

vif_data = pd.DataFrame()
vif_data["Feature"] = features
vif_data["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]

print("\n분산 팽창 계수(VIF):")
print(vif_data)
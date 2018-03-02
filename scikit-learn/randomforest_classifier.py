import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


from sklearn.datasets import make_blobs # ダミーデータの生成用
X, y = make_blobs(n_samples=500, centers=4, random_state=8, cluster_std=2.4)
# n_samples:サンプル数 centers:中心点の数 random_state:seed値 cluster_std: ばらつき度合い



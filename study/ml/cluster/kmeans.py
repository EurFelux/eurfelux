import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
def kmeans(X, k):
    """
    kmeans算法
    :param X: 数据集
    :param k: 类别数
    :return: 聚类中心，聚类标签
    """
    # 随机初始化k个聚类中心
    centers = X[np.random.choice(X.shape[0], k, replace=False)]
    # 迭代
    while True:
        # 计算每个样本到聚类中心的距离
        distances = cdist(X, centers)
        # 分配样本到最近的聚类中心
        labels = np.argmin(distances, axis=1)
        # 计算新的聚类中心  
        new_centers = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        # 如果聚类中心不再变化，退出循环
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels
# 生成数据集
X, y = make_blobs(n_samples=100, centers=4, random_state=0)
# 调用kmeans算法
centers, labels = kmeans(X, 4)
# 绘制聚类结果
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='*', s=200, linewidths=3, color='r')
plt.show()
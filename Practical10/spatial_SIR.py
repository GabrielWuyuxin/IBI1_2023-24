import numpy as np
import matplotlib.pyplot as plt

# 初始化一个100x100的网格，所有人口均为易感者（值为0）
population = np.zeros((100, 100))

# 随机选择一个位置作为初始感染点
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # 设置初始感染点

# 设置参数
beta = 0.3  # 感染概率
gamma = 0.05  # 康复概率
time_steps = 100  # 模拟时间步数

for t in range(time_steps):
    # 找到所有感染点的索引
    infectedIndex = np.where(population == 1)
    
    # 创建一个新的网格用于更新人口状态
    new_population = population.copy()
    
    # 遍历所有感染点
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        # 感染周围的邻居点
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        if population[xNeighbour, yNeighbour] == 0:
                            new_population[xNeighbour, yNeighbour] = np.random.choice([0, 1], p=[1-beta, beta])
    
    # 更新感染者状态为康复者
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.random() < gamma:
            new_population[x, y] = 2
    
    # 更新人口状态
    population = new_population.copy()
    
    # 每10个时间步绘制一次当前状态
    if t % 10 == 0:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.show()

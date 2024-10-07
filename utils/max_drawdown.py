import numpy as np

def max_drawdown(prices):
    # 将序列转换为 numpy 数组
    prices = np.array(prices)
    
    # 计算累计最大值
    cumulative_max = np.maximum.accumulate(prices)
    
    # 计算回撤
    drawdown = (prices - cumulative_max) / cumulative_max
    
    # 返回最大回撤率
    max_drawdown = np.min(drawdown)
    
    return max_drawdown
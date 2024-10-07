import numpy as np

def sharpe_ratio(prices, risk_free_rate=0.002):

    returns = (prices[1:]-prices[:-1])/prices[:-1]
    # 将序列转换为 numpy 数组
    returns = np.array(returns)
    
    # 计算平均超额回报（即超出无风险利率的部分）
    excess_returns = returns - risk_free_rate
    
    # 计算超额回报的平均值
    mean_excess_return = np.mean(excess_returns)
    
    # 计算回报的标准差（即波动性）
    volatility = np.std(returns)
    
    # 计算夏普比率
    sharpe = mean_excess_return / volatility
    return sharpe
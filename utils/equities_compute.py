import numpy as np
def equities_com(p, timepoints, gain, A):
    equity = [0,0,0] # 3种资产的净值
    stock = [0,0,0] # 3种资产的股票数
    equities = np.zeros(timepoints)

    # 初始投资
    for i in range(3):
        equity[i]=gain*p[i]
        stock[i]=equity[i]/A[i]['close'].iloc[0]
    current_equity = list(equity) # 当前三种资产净值
    current_mouny = sum(current_equity) # 当前所有的资金
    expected_equity = list(equity) # 按比例，期望的资产净值
    # print("初始净值分配："+str(current_equity))
    # print("初始净值："+str(gain)+"，每月增加投资："+str(gain))
    equities[0] = sum(current_equity)

    for t in range(1,timepoints):
        for i in range(3):
            current_equity[i] = A[i]['close'].iloc[t]*stock[i]
        current_mouny = sum(current_equity)+gain
        for i in range(3):
            expected_equity[i] = current_mouny*p[i]
        for i in range(3):
            stock[i] = expected_equity[i]/A[i]['close'].iloc[t]
        equities[t] = current_mouny
    return equities

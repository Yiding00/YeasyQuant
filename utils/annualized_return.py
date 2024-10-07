import numpy_financial as npf
def annualized_return(gain, timepoints, end_equity):
    cash_flows = [-gain] * timepoints
    cash_flows.append(end_equity)
    irr = npf.irr(cash_flows)
    annualized_return = (1 + irr) ** 12 - 1
    return annualized_return
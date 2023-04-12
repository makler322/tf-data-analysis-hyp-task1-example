import numpy as np
import scipy


chat_id = 419670097  # Ваш chat ID, не меняйте название переменной


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.05
    conversion_x = x_success / x_cnt
    conversion_y = y_success / y_cnt

    P = (x_success + y_success) / (x_cnt + y_cnt)
    z_stat = (conversion_x - conversion_y) / np.sqrt(P * (1 - P) * (1. / x_cnt + 1. / y_cnt))
    return scipy.stats.norm.cdf(np.abs(z_stat)) < alpha

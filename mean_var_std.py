import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")

    list1 = np.array(list)
    #print(list1)

    mean_r = [list1[[0,1,2]].mean(), list1[[3,4,5]].mean(), list1[[6,7,8]].mean()]
    mean_c = [list1[[0,3,6]].mean(), list1[[1,4,7]].mean(), list1[[2,5,8]].mean()]

    var_r = [list1[[0,1,2]].var(), list1[[3,4,5]].var(), list1[[6,7,8]].var()]
    var_c = [list1[[0,3,6]].var(), list1[[1,4,7]].var(), list1[[2,5,8]].var()]

    std_r = [list1[[0,1,2]].std(), list1[[3,4,5]].std(), list1[[6,7,8]].std()]
    std_c = [list1[[0,3,6]].std(), list1[[1,4,7]].std(), list1[[2,5,8]].std()]

    max_r = [list1[[0,1,2]].max(), list1[[3,4,5]].max(), list1[[6,7,8]].max()]
    max_c = [list1[[0,3,6]].max(), list1[[1,4,7]].max(), list1[[2,5,8]].max()]

    min_r = [list1[[0,1,2]].min(), list1[[3,4,5]].min(), list1[[6,7,8]].min()]
    min_c = [list1[[0,3,6]].min(), list1[[1,4,7]].min(), list1[[2,5,8]].min()]

    sum_r = [list1[[0,1,2]].sum(), list1[[3,4,5]].sum(), list1[[6,7,8]].sum()]
    sum_c = [list1[[0,3,6]].sum(), list1[[1,4,7]].sum(), list1[[2,5,8]].sum()]

    return {
       'mean': [mean_c, mean_r, list1.mean()],
       'variance': [var_c, var_r, list1.var()],
       'standard deviation': [std_c, std_r, list1.std()],
       'max': [max_c, max_r, list1.max()],
       'min': [min_c, min_r, list1.min()],
       'sum': [sum_c, sum_r, list1.sum()]
    }
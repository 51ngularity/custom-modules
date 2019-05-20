
import sys



#function to determine weight for each list element
#takes list_ and returns list_of_weights(list_)
# for simple moving average use y0 == y1
# for usual weighted moving average use y0=1, y1=interval
def weights_function_linear(interval, y0, y1):
    list_of_weights = []
    m = (y1-y0) / interval
    for x in range(0, interval):
        list_of_weights.append(y0 + m*x)
    return list_of_weights


# the list_of_weights determines whether sma or wma is being calculated
def wma_function(list_, list_of_weights):
    if len(list_) != len(list_of_weights):
        sys.exit("error!  len(list_) != len(list_of_weights)")
    else:
        sum_weights = 0
        sum_weighted_elements = 0
        for x in range(0,len(list_)):
            sum_weights += list_of_weights[x]
            sum_weighted_elements += (list_[x]*list_of_weights[x])
    return sum_weighted_elements / sum_weights



def ema_function(new_value, previous_ema, time_interval):
    a = (2/(time_interval+1))
    return previous_ema + (new_value - previous_ema)*a

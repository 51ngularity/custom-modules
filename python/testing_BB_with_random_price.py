



# -------------------------------- imports

# import sys
# sys.path.insert(0, 'C:\\Users\\konto\Anaconda3\\my_modules' )

import simulated_price_movement
import list_operations
import moving_averages
import standard_deviation_of_custom_mean

import matplotlib.pyplot as plt



# ------------------------------- starting values


time_interval = 300
# how long the program runs

sma_interval_bb = 20
# averaging over this number of steps

price=[1000, 1, 1, 10]
# = [price_value, price_direction, price_move_range_min_%, price_move_range_max_%]

price_list = list_operations.single_value_list(price[0], sma_interval_bb)
# fill list with "sma_interval_bb" number of places with element "price[0]"
# = list_ for wma_function

list_of_weights = moving_averages.weights_function_linear(sma_interval_bb,1,1)
# = list_of_weights for wma_function

sma_value = price[0]
# = average of price_list at the start

multiplier_bollinger = 2

bollinger_min = price[0]
bollinger_max = price[0]


# ------------------------------- lists for plotting

x_axis = [0]
price_plot = [price[0]]
sma_value_plot = [sma_value]
bollinger_min_plot = [bollinger_min]
bollinger_max_plot = [bollinger_max]



# ------------------------------- algorithm start

print("price {:6.1f} | sma {:6.1f} | bb_min {:6.1f} | bb_max {:6.1f} ".format(price[0], sma_value, bollinger_min, bollinger_max))

for x in range(1, time_interval + 1):

    price = simulated_price_movement.price_change(price)
    # get new price

    price_list = list_operations.update_list(price_list, price[0])
    # update price_list

    sma_value = moving_averages.wma_function(price_list,list_of_weights)
    # get new sma_value

    bollinger_min = sma_value - standard_deviation_of_custom_mean.standard_deviation(price_list, sma_value)*multiplier_bollinger
    bollinger_max = sma_value + standard_deviation_of_custom_mean.standard_deviation(price_list, sma_value)*multiplier_bollinger

    print("price {:6.1f} | sma {:6.1f} | bb_min {:6.1f} | bb_max {:6.1f} ".format(price[0], sma_value, bollinger_min, bollinger_max))

    x_axis.append(x)
    price_plot.append(price[0])
    sma_value_plot.append(sma_value)
    bollinger_min_plot.append(bollinger_min)
    bollinger_max_plot.append(bollinger_max)



# ------------------------------- plotting

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 13
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size
# print ("Current size:", fig_size)



plt.plot(x_axis, price_plot, sma_value_plot)
plt.plot(x_axis, bollinger_min_plot, bollinger_max_plot)
plt.title("testing_Bollinger_Bands_with_randomly_generated_price_data")
plt.xlabel("time[1d]")
plt.ylabel("price[btc/usd]")
plt.legend(["price","sma", "bb_min", "bb_max"])

plt.show()


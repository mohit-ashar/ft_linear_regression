# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mashar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/25 06:06:01 by mashar            #+#    #+#              #
#    Updated: 2020/09/29 23:06:42 by mashar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import csv
import matplotlib.pyplot as plt
import numpy as np

theta_0 = 0.0
theta_1 = 0.0

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
f.close()
learning_rate = 0.005
m = len(data[1:])
min_km = min(float(x[0]) for x in data[1:])
max_km = max(float(x[0]) for x in data[1:])
max_price = max(float(x[1]) for x in data[1:])
min_price = min(float(x[1]) for x in data[1:])
for i in range(100000):
    sum_t0 = 0.0
    sum_t1 = 0.0
    for item in data[1:]:
        #normalize the dataset to scale
        item_0 = (float(item[0]) - min_km) / (max_km - min_km)
        item_1 = (float(item[1]) - min_price) / (max_price - min_price)
        sum_t0 = sum_t0 + (theta_0 + (theta_1 * item_0) - item_1)
        sum_t1 = sum_t1 + (theta_0 + (theta_1 * item_0) - item_1) * item_0
    temp_theta_0 = learning_rate * 1/m * sum_t0
    temp_theta_1 = learning_rate * 1/m * sum_t1
    theta_0 -= temp_theta_0
    theta_1 -= temp_theta_1

#denormalize to get unscaled result
theta_0 = theta_0 * (max_price - min_price) + min_price + (theta_1 * min_km * (max_price - min_price)) / (max_km - min_km)
theta_1 = theta_1 * (max_price - min_price) / (max_km - min_km)
f = open("values.txt", "w")
f.write(str(theta_0) + "\n" + str(theta_1))
f.close()

#scatter plot data
for item in data[1:]:
    plt.scatter(float(item[0]),float(item[1]))

#plotting line
plot_x = np.linspace(0, 250000, 250000)
plot_y = theta_1 * plot_x + theta_0
plt.plot(plot_x, plot_y, '-r')
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()

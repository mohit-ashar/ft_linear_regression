# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mashar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/25 06:06:01 by mashar            #+#    #+#              #
#    Updated: 2020/09/29 00:36:22 by mashar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import csv

theta_0 = 0.0
theta_1 = 0.0

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

learning_rate = 0.00000000001
m = len(data[1:])
for i in range(20):
    sum_t0 = 0.0
    sum_t1 = 0.0
    for item in data[1:]:
        #print(sum_t0)
        sum_t0 = sum_t0 + (theta_0 + (theta_1 * float(item[0])) - float(item[1]))
        sum_t1 = sum_t1 + (theta_0 + (theta_1 * float(item[0])) - float(item[1])) * float(item[0])
    temp_theta_0 = sum_t0 / m
    temp_theta_1 = sum_t1 / m
    theta_0 = theta_0 - (learning_rate * temp_theta_0)
    theta_1 = theta_1 - (learning_rate * temp_theta_1)
    print(temp_theta_0)
    print(temp_theta_1)
    print(theta_0)
    print(theta_1)
    print("\n")


f = open("values.txt", "w")
f.write(str(theta_0) + "\n" + str(theta_1))
f.close()


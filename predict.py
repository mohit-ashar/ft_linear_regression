# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mashar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/25 05:35:49 by mashar            #+#    #+#              #
#    Updated: 2020/09/28 23:04:37 by mashar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
try:
    mileage = float(input("Enter mileage of the car to predict price of the car: "))
except:
    print("Mileage can ony be a number")
    exit(0)

f = open("values.txt", "r")
value_list = f.read().split("\n")
if(float(value_list[0]) == 0 and float(value_list[1]) == 0):
    print("Model not trained, price will be zero")
else:
    print("Theta 0 is " + value_list[0] + " and Theta 1 is " + value_list[1])
    print("Price is: " + str(mileage * float(value_list[1]) + float(value_list[0])))
f.close()

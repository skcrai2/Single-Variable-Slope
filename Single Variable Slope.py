# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

coords = [[1000,200],[2000,300],[3000,400]]
m = len(coords)

alpha = 0.0000001
theta1 = 0.0
new_theta = 0.0
sigma = 0.0

diff = 1.0
tolerance = 0.0001

counts = 0
max_iterations = 50000

while diff > tolerance and counts < max_iterations:
    for point in coords:
        x = point[0]
        y = point[1]
        sigma = sigma + ((theta1*x)-y)*x
    new_theta = theta1 - (alpha*(1/m)*sigma)
    diff = abs(new_theta - theta1)
    theta1 = new_theta
    sigma = 0.0
    counts = counts + 1

print('The slope that best fit the data was: ', theta1)
print('The number of iterations to find the slope was:', counts)

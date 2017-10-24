import numpy as np
import matplotlib.pyplot as plt


# initialize the x and y data arrays for each subplot to empty for now
x = []
x_1 = []
y =[]
y_1 = []
y2 = []

# need plt.ion() in order for matplotlib to show as it turns on interactive mode on which allows for iterative
# redrawing of the canvas (i'm pretty sure)
plt.ion()
# if arg is a string then the matplotlib window title is equal to the string
# or can put in an int which either will label that figure with that int or if a figure already exists with that
# int label it will return that existing figure
fig = plt.figure("This is a figure")
ax1 = plt.subplot(211)
ax1.set_ylim((0,10))
ax1.set_xlim((0,5))
ax2 = plt.subplot(212)
ax2.set_ylim((0,5))
ax2.set_xlim((0,5))
# below just use this to se the line style / color the
# data objects input in these lines will essentially be overridden
# with each iteration of below for loop. But we assign them to empty so that
# we show no points and append data points with each iteration of for loop
# note: we just call plot() again on same axes object to add another line to it
line_ax1, = ax1.plot(x, y, 'bo')
line2_ax1, = ax1.plot(x, y_1, 'c--')
line_ax2, = ax2.plot(x, y2, 'r-')
count =0
for datapt in np.arange(0.0, 5.0, 1):
    # then update the existing data objects and only plot the points that
    # we have gone through in the for loop
    y.append(datapt)
    y_1.append(datapt/3)
    x.append(count)
    y2.append(datapt/2)
    # then below need to reset the x and y data with the mutated objects as it doesn't
    # dynamically update, must refer to a static copy of the list objects
    line_ax1.set_xdata(x)
    line_ax2.set_xdata(x)
    line2_ax1.set_xdata(x)
    line_ax1.set_ydata(y)
    line2_ax1.set_ydata(y_1)
    line_ax2.set_ydata(y2)
    fig.canvas.draw()
    count += 1
    # pause() halts the matplotlib plotting for the amount of time put into the argument
    plt.pause(1)

# need this to keep showing the matplotlib window. without this once
# we exit the for loop we will just close the matplotlib window
while(True):
    plt.pause(.05)

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import CheckButtons

class Graph():
    def __init__(self):
        fig = plt.figure()

        gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1], hspace=0.3)
        gs2 = gridspec.GridSpec(2,1, height_ratios=[1,1])
        gs3 = gridspec.GridSpec(1,1, height_ratios=[1])
        gs4 = gridspec.GridSpec(0,1)

        ax1 = fig.add_subplot(gs[0])
        ax2 = fig.add_subplot(gs[1], sharex=ax1)
        ax3 = fig.add_subplot(gs[2], sharex=ax2)

        ax1.plot([1,2,3], [1,2,3], color="crimson")
        ax2.plot([1,2,3], [2,3,1], color="darkorange")
        ax3.plot([1,2,3], [3,2,1], color="limegreen")

        visible = True
        rax = plt.axes([0.05, .85, 0.1, 0.15])
        # check = CheckButtons(rax, ('Plot 1', 'Plot 2', 'Plot 3'), (True, True, True))
        checks = [True, True, True]
        grids = [gs3, gs2, gs]
        axes = [ax1, ax2, ax3]

        def toggle_ax2(label):
            if label == 'Plot 1':
                checks[0] = not checks[0]
            elif label == 'Plot 2':
                checks[1] = not checks[1]
            elif label == 'Plot 3':
                checks[2] = not checks[2]
            num = sum(checks)
            grid = grids[num-1]
            pos = 0
            for count, check in enumerate(checks):
                if check:
                    axes[count].set_visible(True)
                    axes[count].set_position(grid[pos].get_position(fig))
                    pos += 1
                else:
                    axes[count].set_visible(False)
            # remember need to have plt.draw() at the end of the checkbutton method or else will not
            # update the figure accordingly. With the way I do the loop right now it would be on a
            # delay. (ie wouldn't reflect the change until clicking on a check box again)
            plt.draw()

        rax = plt.axes([0.05, .85, 0.1, 0.15])
        # require to make instance variables with the widgets or else the widgets are not guranteed to be not garbage
        # collected. Thus if don't make these instance variables then the plot will show with checkboxes but without
        # any functionality. See below link for reference:
        # https://stackoverflow.com/questions/42419139/matplotlib-widgets-button-doesnt-work-inside-a-class
        self.check = CheckButtons(rax, ('Plot 1', 'Plot 2', 'Plot 3'), (True, True, True))
        self.check.on_clicked(toggle_ax2)

g = Graph()
plt.show()

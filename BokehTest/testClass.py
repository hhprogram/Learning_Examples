from bokeh.plotting import curdoc, figure
import time
from bokeh.models import ColumnDataSource
from functools import partial
from bokeh.layouts import column, row
from bokeh.models.widgets import CheckboxButtonGroup

class Reporter():
    def __init__(self, figNames):
        self.data = []
        self.source = ColumnDataSource(data=dict(x=[0], y=[0]))
        self.doc = curdoc()
        self.figs = {}
        self.buttonToFig = {}
        self.popFigures(figNames)
        self.buttons = self.createButtons(figNames)
        self.layout = column(row(self.buttons, name="buttons"), sizing_mode='scale_width')
        # below works if I want a static layout with the first row with a checkboxbutton Group and then each of
        # the figures in self.figs occupying a row to themselves.
        # layout = column(row(buttons, name='buttons'), row([self.figs[fig] for fig in self.figs]), sizing_mode='scale_width')
        self.doc.add_root(self.layout)
        self.updateView()

    def updateView(self):
        active = self.buttons.active
        for i in range(len(self.figs)):
            if i not in active:
                print(i, " not in active")
                # note: each figure object has a 'name' attribute which is the string name set when I set the
                # name when I create the figures (see popFigures method)
                figureToRemove = self.doc.get_model_by_name(self.buttonToFig[i].name)
                # need a not None check because if figure already gone and try to remove again then will get
                # an error of trying to remove something not is already not in the list
                if figureToRemove is not None:
                    self.layout.children.remove(figureToRemove)
            elif i in active:
                if self.buttonToFig[i] in self.layout.children:
                    print("already shown")
                else:
                    print("adding back")
                    self.layout.children.append(self.buttonToFig[i])

    def popFigures(self, figNames):
        for name in figNames:
            # in order to get full scaling width need to set the sizing mode to each figure to scale_width
            # along with above setting the layout sizing_mode to be scale_width. Note: we could in theory
            # have only some figures scale by adding sizing_mode to only some of the figures
            fig = figure(x_range=[0, 20], y_range=[0,20], name=name, title=name, sizing_mode='scale_width')
            fig.circle(x='x', y='y', source=self.source)
            self.figs[name] = fig

    def createButtons(self, figNames):
        buttons = CheckboxButtonGroup(labels=[name for name in figNames], active=[0, 1, 2])
        buttons.on_click(self.buttonClick)
        for count, name in enumerate(figNames):
            self.buttonToFig[count] = self.figs[name]
        return buttons

    def buttonClick(self, label):
        self.updateView()

    def report(self, data):
        self.data = data
        self.doc.add_next_tick_callback(partial(self.update))

    # @gen.coroutine ?? need to do more research to learn about gen.coroutine decorators
    def update(self):
        y = [i for i in range(len(self.data))]
        self.source.stream(dict(x=self.data, y=y))

class TestObject():
    def __init__(self):
        self.data = []
        self.count = 0
        self.figNames = ["Plot 1", "Plot 2", "Plot 3"]
        self.reporter = Reporter(self.figNames)

    def addSomeData(self):
        self.data.append(self.count)
        self.count += 1

    def report(self):
        self.reporter.report(self.data)

    def runSimulation(self):
        for i in range(20):
            time.sleep(1)
            self.addSomeData()
            self.report()

class TestRun():
    def __init__(self):
        self.obj = TestObject()

    def run(self):
        self.obj.runSimulation()

Small example that shows how to run a python script and the bokeh server simultaneously. This is a proof of concept of 
having bokeh server update with real-time streaming data, sourced from the python script, and update the graph
real time. Also, adds some functionality of adding and removing plots.
Credit to bokeh documentation (below) as I used their example as initial guidance:
https://bokeh.pydata.org/en/latest/docs/user_guide/server.html#updating-from-threads

to run:
`bokeh serve --show run.py` in this BokehTest directory

Note:
You can switch between the implementation using CheckboxButtonGroup and toggle buttons
by commenting / uncommenting the respective lines in the TestRun() constructor method.
(TestObject = CheckboxButtonGroup, TestObject2 = Toggle buttons)

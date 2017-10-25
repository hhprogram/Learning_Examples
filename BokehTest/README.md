Small example that shows how to run a python script and the bokeh server simultaneously. This is a proof of concept of 
having bokeh server update with real-time streaming data, sourced from the python script, and update the graph
real time. Also, adds some functionality of adding and removing plots.
Credit to bokeh documentation (below) as I used their example as initial guidance:
https://bokeh.pydata.org/en/latest/docs/user_guide/server.html#updating-from-threads

Can be run might taking downloading the 'BokehTest' directory. And then running `bokeh serve --show run.py` in the directoy in which you have run.py

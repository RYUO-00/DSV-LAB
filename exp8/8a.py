from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import Label

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [20, 35, 30, 50, 45, 65]

p = figure(
    title="Monthly Sales",
    x_range=months,
    x_axis_label="Month",
    y_axis_label="Sales",
    width = 700,
    height=400
) 
p.line(months, sales, line_width=3, legend_label="Sales")          
p.scatter(months, sales, size=8, legend_label="Sales")              

label = Label(x=3, y=50, text="Highest Sales", x_offset=10,y_offset=10)

p.add_layout(label)

show(p)

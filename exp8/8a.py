from bokeh.plotting import figure, show
from bokeh.io import output_notebook

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [20, 35, 30, 50, 45, 65]

p = figure(
    title="Monthly Sales",
    x_range=months,
    x_axis_label="Month",
    y_axis_label="Sales"
) 
p.line(months, sales, line_width=3, legend_label="Sales")          # the line
p.scatter(months, sales, size=8, legend_label="Sales")              # dots on each month

# Text label placed above the April point
p.text(x=["Apr"], y=[53], text=["Heighest Sales"],
        text_align="center", text_font_size="12pt")

show(p)

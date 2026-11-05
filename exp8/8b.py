
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()

# ---------------- Data ----------------
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# ---------------- 1. Line plot ----------------
p1 = figure(title="Line Plot", x_axis_label="X", y_axis_label="Y")
p1.line(x, y, line_width=3)          # line_width makes the line thicker
show(p1)

# ---------------- 2. Scatter plot ----------------
p2 = figure(title="ScatterPlot", x_axis_label="X", y_axis_label="Y")
p2.scatter(x, y, size=10)            # size is the dot size
show(p2)

# ---------------- 3. Bar plot ----------------
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

p3 = figure(
    title="Bar Plot",
    x_range=categories,              # x axis shows category names
    x_axis_label="Category",
    y_axis_label="value"
)
p3.vbar(x=categories, top=values, width=0.5)   # vertical bars
show(p3)

# ---------------- 4. Area plot ----------------
p4 = figure(title="Area Plot", x_axis_label="X", y_axis_label="Y")
p4.varea(x=x, y1=0, y2=y)            # fills the area between y1=0 and y2=y
show(p4)


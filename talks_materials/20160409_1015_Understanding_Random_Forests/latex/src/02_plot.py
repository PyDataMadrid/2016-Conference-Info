from bokeh.plotting import figure, show

p = figure(title = 'Event attendance')
p.xaxis.axis_label = 'Distance'
p.yaxis.axis_label = 'Age'
p.circle(df[df.attended]['distance'],
         df[df.attended]['age'],
         color='red',
         legend='Attended',
         fill_alpha=0.2,
         size=10)
p.circle(df[~df.attended]['distance'],
         df[~df.attended]['age'],
         color='blue',
         legend="Didn't attend",
         fill_alpha=0.2,
         size=10)
show(p)
from sklearn.linear_model import LogisticRegression

logit = LogisticRegression()
logit.fit(df[['age', 'distance']], df['attended'])

def get_y(x): return -(logit.intercept_[0] + logit.coef_[0,1] * x) / logit.coef_[0,0]

plot = base_plot()
min_x, max_x = df['distance'].min(), df['distance'].max()
plot.line(x=[min_x, max_x],
          y=[get_y(min_x), get_y(max_x)],
          line_color='black',
          line_width=2)

_ = show(plot)
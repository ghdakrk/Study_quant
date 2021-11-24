import numpy as np
from numpy.lib.function_base import meshgrid
import scipy.stats as stat

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


#Black-scholes option formular
def europian_option(S, K, T, r, sigma, option_type):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2 * T) / (sigma * np.sqrt(T)))
    d2 = d1 - sigma * np.sqrt(T)

    if  option_type == "call":
        V = S * stat.norm.cdf(d1) - K * np.exp(-r * T) * stat.norm.cdf(d2)
    else:
        V = K * np.exp(-r * T) * stat.norm.cdf(-d2) - S * stat.norm.cdf(-d1)

    return  V

#Parameter
K = 100
r = 0.01
sigma = 0.25

#Variables
T = np.linspace(0, 1, 100)
S = np.linspace(0, 200, 100)
T, S = meshgrid(T, S)

#Output
call_value = europian_option(S, K, T, r, sigma, "call")
put_value = europian_option(S, K, T, r, sigma, "put")

trace = go.Surface(x=T, y=S, z=call_value)
data = [trace]
layout = go.Layout(title='call_option', scene={'xaxis':{'title':'Maturity'}, 'yaxis':{'title':'Spot_price'}, 'zaxis':{'title':'option_price'}})
fig = go.Figure(data=data, layout=layout)
iplot(fig)

trace = go.Surface(x=T, y=S, z=put_value)
data = [trace]
layout = go.Layout(title='put_option', scene={'xaxis':{'title':'Maturity'}, 'yaxis':{'title':'Spot_price'}})
fig = go.Figure(data=data, layout=layout)
iplot(fig)




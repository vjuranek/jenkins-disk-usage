#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy, time
from pylab import *
from matplotlib.ticker import Formatter

class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind>=len(self.dates) or ind<0: return ''

        return time.strftime(self.fmt,self.dates[ind])
    
def create_graph(data,x_label='Date [y-m-d]',y_label='Default label'):
    dates = [d[0] for d in data]
    values = [d[1] for d in data]
    fig = figure()
    ax = fig.add_subplot(111)
    formatter = MyFormatter(dates)
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(numpy.arange(len(data)), values, 'o-')
    ax.grid(True)
    #ax.xaxis.set_label("Date")
    #ax.yaxis.set_label("Total # of builds/day")
    xlabel(x_label)
    ylabel(y_label)
    fig.autofmt_xdate()
    return fig

def save(graph, plot_name, ext='eps', img_dir="."):
    graph.savefig(img_dir + '/' + plot_name +'.' + ext)


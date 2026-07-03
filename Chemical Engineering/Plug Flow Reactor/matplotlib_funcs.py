from typing import Iterable
import matplotlib.pyplot as plt


def plot_matplotlib_style(x_data:Iterable,y_data:Iterable,x_label:str,y_label:str,legend:str or Iterable[str])->None:
    """Function to plot a matplotlib plot."""
    fig, ax = plt.subplots()
    ax.plot(x_data,y_data)
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    if type(legend) is str:
        plt.legend([legend],loc='best')
    else:
        plt.legend(legend,loc='best')
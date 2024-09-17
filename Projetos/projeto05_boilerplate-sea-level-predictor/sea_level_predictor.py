import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('../projeto05_boilerplate-sea-level-predictor/epa-sea-level.csv')

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    declive, interceptar, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(df['Year'].min(), 2051)
    y_values = [interceptar + declive * x for x in x_values]
    plt.plot(x_values, y_values, 'r')

    df_2000 = df[df['Year'] >= 2000]
    declive, interceptar, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_values = range(df_2000['Year'].min(), 2051)
    y_values = [interceptar + declive * x for x in x_values]
    plt.plot(x_values, y_values, 'g')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')


    
    plt.savefig('sea_level_plot.png')
    return plt.gca()

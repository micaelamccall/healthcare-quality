import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from healthcare_quality.clean_data import merged_df
import seaborn as sns
from matplotlib.lines import Line2D

def sns_scatter_with_category(df, x, y, category, palette, axislabels):
    """ Creates a customized scatterplot with different colors per category 
    arguments:
    df = pandas datafame
    x = column of values for x axis
    y = column of values for y axis
    category = column of categories
    palette = a list of color codes, same length as the number of categories in category
    axislabels = a list with x axis label first, y axis label 2nd, and a nested list with legend labels 3rd"""

    # sets the background to white and add ticks to the axis
    sns.set_style('white')
    sns.set_style('ticks')

    plot = sns.scatterplot(data = df, x = x, y = y, hue = category,  palette=palette)

    # takes away the top and right axes
    sns.despine()

    # sets the x axis ticks to be spaced by 1 unit
    plot.xaxis.set_major_locator(ticker.MultipleLocator(1))

    # creates custom legend parameters
    legend_params=[]
    for color in palette:
        legend_params.append(Line2D([], [], marker='.', color=color, linestyle='None'))
 
    # set x and y axes
    plt.xlabel(axislabels[0])
    plt.ylabel(axislabels[1])

    # set custom legend
    plt.legend(legend_params, axislabels[2], loc='lower left')



if __name__ == '__main__':

    y_list = [
        "patients_rating_of_the_facility_linear_mean_score", 
        "patients_recommending_the_facility_linear_mean_score", 
        "communication_about_your_procedure_linear_mean_score"]
    palette_list = [
        ["#9b59b6","#3498db"], 
        ["#9b59b6","#2ecc71"], 
        ["#9b59b6","#e74c3c"]]
    y_label_list = [
        "Patients' Mean Rating of the Facility", 
        "Patients' Mean Recommendation of the Facility", 
        "Patients' Mean Rating of Communication"]


    for i, y in enumerate(y_list):
        df = merged_df
        x = "rate_of_readmission"
        y = y
        category = "is-MUA?"
        palette = palette_list[i]
        axislabels = ["Readmission Rate", y_label_list[i], ['MUA', 'Not MUA']]
        sns_scatter_with_category(df, x, y, category, palette, axislabels)
        plt.show()
        plt.close()
    
    palette = ["#75bbfd", "#fc5a50", "#ae7181", "#0504aa", "#703be7", "#98eff9"]
    sns_scatter_with_category(
        merged_df, 
        x = "rate_of_readmission", 
        y = "patients_recommending_the_facility_linear_mean_score", 
        category = "MUA-population-type", 
        palette = palette, 
        axislabels = [
            "Readmission Rate", 
            "Patients' Mean Recommendation of the Facility", 
            ["MUA", "MUP Low Income", "None", "MUP Other Pop", "MUP Medicaid", "MUP Homeless"]])


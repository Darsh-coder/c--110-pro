from multiprocessing.sharedctypes import Value
import plotly.graph_objects as go
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("newdata.csv")

series_data = df["c"]
data = series_data.tolist()
population_mean = statistics.mean(data)
population_std = statistics.stdev(data)
#fig = ff.create_distplot([data],["temp"],show_hist = False)

#fig.add_trace(go.Scatter(x=[population_mean,population_mean],y= [0,0.1],mode ="lines" , name = "MEAN" ))

#fig.show()

print("population mean is ",population_mean)
print("population stdev is ",population_std)



def random_set_of_mean(counter):
    dataset = []
    for i in range (0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)


    sample_mean = statistics.mean(dataset)
    return sample_mean


#print("sample mean is ",sample_mean)
#print("sample stdev is ",sample_std)

def show_fig(mean_list):

    fig = ff.create_distplot([mean_list],["temp"],show_hist = False)
    #fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y= [0,0.07],mode ="lines" , name = "MEAN" ))
    fig.show()

def setup ():
    mean_list = []
    for i in range(0,1000):
        setofmeans = random_set_of_mean(81)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    sample_stdev = statistics.stdev(mean_list)
    sample1_mean = statistics.mean(mean_list)
    print("the sample_stdev is ",sample_stdev)
    print("the sample1_mean is ",sample1_mean)

setup()


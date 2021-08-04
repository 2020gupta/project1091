import csv
import random
import pandas as pd
import statistics as st
import plotly.graph_objects as go
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
result=df["mathscore"].tolist()
# count=[]
# for i in range(0,1000):
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)
#     result.append(dice1+dice2)
#     count.append(i)
mean=st.mean(result)
median=st.median(result)
mode=st.mode(result)
stdev=st.stdev(result)
fstd_start,fstd_stop=mean-stdev,mean+stdev
sstd_start,sstd_stop=mean-(2*stdev),mean+(2*stdev)
tstd_start,tstd_stop=mean-(3*stdev),mean+(3*stdev)
list1=[result for  result in result if result>fstd_start and result<fstd_stop]
list2=[result for  result in result if result>sstd_start and result<sstd_stop]
list3=[result for  result in result if result>tstd_start and result<tstd_stop]
print(stdev,fstd_start,fstd_stop,sstd_start,sstd_stop,tstd_start,tstd_stop)
print(len(list1)*100.0/len(result),len(list2)*100.0/len(result),len(list3)*100.0/len(result))
graph=ff.create_distplot([result],["result"],show_hist=False)
graph.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[fstd_start,fstd_start],y=[0,0.17],mode="lines",name="std1"))
graph.add_trace(go.Scatter(x=[fstd_stop,fstd_stop],y=[0,0.17],mode="lines",name="std1"))

graph.add_trace(go.Scatter(x=[sstd_start,sstd_start],y=[0,0.17],mode="lines",name="std2"))
graph.add_trace(go.Scatter(x=[sstd_stop,sstd_stop],y=[0,0.17],mode="lines",name="std2"))

graph.add_trace(go.Scatter(x=[tstd_start,tstd_start],y=[0,0.17],mode="lines",name="std3"))
graph.add_trace(go.Scatter(x=[tstd_stop,tstd_stop],y=[0,0.17],mode="lines",name="std3"))
graph.show()
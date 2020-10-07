import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("Pak.csv")
df2 = pd.read_csv("Us.csv")
df3 = pd.read_csv("Sweden.csv")
df4 = pd.read_csv("India.csv")
df5 = pd.read_csv("Canada.csv")
df6 = pd.read_csv("Norway.csv")

dfa1=pd.DataFrame(df1,columns=["Date","Pos_Per"])
dfa2=pd.DataFrame(df2,columns=["Date","Pos_Per"])
dfa3=pd.DataFrame(df3,columns=["Date","Pos_Per"])
dfa4=pd.DataFrame(df4,columns=["Date","Pos_Per"])
dfa5=pd.DataFrame(df5,columns=["Date","Pos_Per"])
dfa6=pd.DataFrame(df6,columns=["Date","Pos_Per"])

x1=dfa1['Date']
y1=dfa1['Pos_Per']
x2=dfa2['Date']
y2=dfa2['Pos_Per']
x3=dfa2['Date']
y3=dfa3['Pos_Per']
x5=dfa4['Date']
y4=dfa4['Pos_Per']
x5=dfa5['Date']
y5=dfa5['Pos_Per']
x6=dfa6['Date']
y6=dfa6['Pos_Per']



plt.plot(x1,y1 , color='g', label="Pak")
plt.plot(x2,y2 , color='b', label="US")
plt.plot(x3,y3 , color='k', label="Sweden")
plt.plot(x4,y4 , color='y', label="India" )
plt.plot(x5,y5 , color='r', label="Canada")
plt.plot(x6,y6 , color='m', label="Norway")
plt.legend()
plt.xticks(rotation="vertical")
plt.show()
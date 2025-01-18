# find s
import pandas as pd

data=pd.read_csv('1.csv',header=None)
attributes=['Sky', 'Temp', 'Humidity', 'Wind', 'Water', 'Forecast']
data.columns=attributes
print(attributes)
print(data)

target=['yes','yes','no','yes']
print(target)

h=['0','0','0','0','0','0']
print("Initial Hypothesis: ",h)

for i in range(len(target)):
    if target[i]=='yes':
        for j in range(len(attributes)):
            print(j)
            if h[j]=='0':
                h[j]=data.iloc[i,j]
            elif h[j]!=data.iloc[i,j]:
                h[j]='?' 
        print(f"After {i+1} iteration : ",h)

print(f"Final Hypothesis: ",h)




Sunny,Warm,Normal,Strong,Warm,Same
Sunny,Warm,High,Strong,Warm,Same
Rainy,Cold,High,Strong,Warm,Change
Sunny,Warm,High,Strong,Cool,Change
           


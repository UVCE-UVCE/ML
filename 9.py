# locally Weighted Regresssion (LWR)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("../LR.csv")
x=data['x']
y=data['y']
print(data)

def gaussianKernel(q,point,k):
    return np.exp(-(q-point)**2/(2*k**2))

def lwr(q,x,y,k):
    weights=[ gaussianKernel(q,x[i],k) for i in range(len(x))]
    weights_Mat=np.diag(weights)
    xBias=np.vstack([np.ones(len(x)),x]).T
    theta=np.linalg.pinv(xBias.T @ weights_Mat @ xBias) @ (xBias.T @ weights_Mat @ y)
    return theta[0]+theta[1]*q

k=0.1
query_points=np.linspace(min(x),max(x),100)
predictions=[ lwr(query,x,y,k) for query in query_points]

plt.scatter(x,y,color='green')
plt.plot(query_points,predictions,color="red")
plt.show()
import numpy as np

x=np.array(([2,9],[1,5],[3,6]))
y=np.array(([92],[89],[86]))
x=x/np.amax(x)
y=y/100

def sigmoid(x):
    return (1/(1+np.exp(-x)))

def derivative_sigmoid(x):
    return x*(1-x)

epoch=7000
learning_rate=0.1
inputlayer_neurons=2
hiddenlayer_neurons=3
output_neurons=1

wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wo=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bo=np.random.uniform(size=(1,output_neurons))

for i in range(epoch):
    net_h=np.dot(x,wh)+bh
    sigma_h=sigmoid(net_h)
    net_o=np.dot(sigma_h,wo)+bo
    output=sigmoid(net_o)
    deltaK=(y-output)*derivative_sigmoid(output)
    deltaH=deltaK.dot(wo.T)*derivative_sigmoid(sigma_h)
    wo=wo+sigma_h.T.dot(deltaK)*learning_rate
    wh=wh+x.T.dot(deltaH)*learning_rate

print("Input: ",str(x))
print("Actual Output: ",str(y))
print("Predicted Output: ",output)

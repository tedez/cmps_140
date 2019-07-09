import math
from sklearn.metrics import *

def logistic(x, w):
    length = len(x)
    retval = []
    for i in range(0, length):
        retval.append(sigmoid(np.dot(x[i], np.transpose(w))))
    return retval
    
def sigmoid(z):
    return (float(1.0 / float((1.0 + math.exp(-1.0*z))))) 

def loss_func(y, h):
    y = np.array(y)
    h = np.array(h)
    return np.sum((y - h)**2)

def loss_func_derivative(y, h, x):
#     length = len(y)
    y = np.array(y)
    h = np.array(h)
    x = np.array(x)
    return np.dot((y - h) * (h * (1 - h)), x)
    
def accuracy(y, h):
    return 100 * np.sum(y==h)/len(y)

def logistic_regression(x, y, loss_func_derivative, learning_rate, num_steps=100):
    w = np.ones(3)
    x = np.pad(x, [[0,0], [1,0]], mode='constant')

    print('Intial Accuracy:{}%'.format(accuracy(y, np.round(logistic(x, w)))))
    prev_loss = 0
    for step in range(num_steps):
        h = logistic(x, w)
        loss = loss_func(y, h)
        
        if math.fabs(loss - prev_loss) < 0.0000001:
            return w
         
        w += learning_rate * loss_func_derivative(y, h, x)
        
        print('Step {} Accuracy:{}%, Loss: {}'.format(step+1, accuracy(y, np.round(logistic(x, w))), loss))
        prev_loss = loss
    return w
    
learning_rate = 0.5
ws = logistic_regression(data, labels, loss_func_derivative, learning_rate)
yh = np.round(logistic(np.pad(data, [[0,0], [1,0]], mode='constant'), ws))
colors = ['g' if _yh==_y else 'r' for _yh, _y in zip(yh, labels.astype(np.int))]
plt.title('Classification Results')
plt.scatter(data[:,0], data[:,1], c=colors)

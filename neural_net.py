import math

#one neuron
class Neuron(object):

    def __init__(self, inputs, weights):
        self.inputs = inputs
        self.weights = weights


    #get the summation of inputs*weights
    def calc_z(self):
        z=0

        for i in range(0, len(self.inputs)):
            z=z+self.inputs[i]*self.weights[i]
        print z
        return
    
    def calc_sigmoid(self, z):
        s=1/(1+math.exp(-z))
        print s
        return

def RunNetwork():

    n=Neuron([1, 2, 3], [0.1, 0.1, 0.9])

    z=n.calc_z()

    n.calc_sigmoid(z)
    return

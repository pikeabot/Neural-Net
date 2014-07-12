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
        print "z=", z
        return z
    
    def calc_sigmoid(self, z):
        """
        o = s(z) = 1.0 / (1.0 + e**(-z)) 
        ds(o)/dz = s(z) * (1 - s(z)) = o * (1 - o)
        """
        s=1/(1+math.exp(-z))
        print s
        return s

    def calc_dw(self, index, perf_elem, z):
        w1=(perf_elem.d-z)*self.inputs[index]-self.weights[index]
        #update weights
        self.weights[index]=w1
        return 

class PerformanceElement(object):
    
    def __init__(self, desired):
        self.d=desired

    def calc_perf(self, o):
        """
        P(o) = -0.5 (d - o)**2 
        dP(o)/dx = (d - o) 
        """
        print "d-0=", self.d-o
        return self.d-o
    
def run_node():

    input_list=[1, 2, 3]
    output_list=[0.1, 0.1, 0.9]
    desired_out=0.0
    
    n=Neuron(input_list, output_list)
    p=PerformanceElement(desired_out)

    i=0
    
    for i in range(0, 10):
        #calculate sum of inputs into node
        z=n.calc_z()

        #calculate performance criteria
        #p.calc_perf(o)

        #calculate sigmoid
        #o= n.calc_sigmoid(z)        
        
        #recalulate weights
        for i_list in range(0, len(input_list)):
            n.calc_dw(i_list, p, z)
            

    return

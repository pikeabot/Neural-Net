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
        #print "z=", z
        return z
    

        
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

class Layer(object):

    def __init__(self, layer_num):
        self.layer=layer_num

    def neurons(self, neurons):
        self.neurons=neurons

    def weights(self, weights):
        self.w = weights

class Network(object):

    def __init__(self, neurons, perf_elem):
        self.neurons=neurons
        self.desired=perf_elem

        
    def calc_sigmoid(self, z):
        """
        o = s(z) = 1.0 / (1.0 + e**(-z)) 
        ds(o)/dz = s(z) * (1 - s(z)) = o * (1 - o)
        """
        s=1/(1+math.exp(-z))
        print s
        return s

    def calc_dw(self, index, perf_elem, z):
        
        w1=.9*(perf_elem.d-z)*self.neurons.inputs[index]+self.neurons.weights[index]
        #update weights
        self.neurons.weights[index]=w1
        return



    def create_layers(self, num_layers):

        num_of_neurons=num-layers+1
        for i in range (0, num_layers):
            layers=self.Layers(i)
        return
        
    def run_network(self):

        n=self.neurons
        p=self.desired
        
        for i in range(0, 30):
            
            #calculate sum of inputs into node
            z=n.calc_z()

            #calculate performance criteria
            #p.calc_perf(o)

            #calculate sigmoid
            #o= n.calc_sigmoid(z)        
            
            #recalulate weights
            for i_list in range(0, len(n.inputs)):
                self.calc_dw(i_list, p, z)

        return
        
        
    
def run_node():

    input_list=[-1, 0, 0]
    weights_list=[1, 1, 1]
    desired_out=0.0


    n=Neuron(input_list, weights_list)
    p=PerformanceElement(desired_out)
    network=Network(n,p)
    network.layer=1
    network.run_network()

    return

def calc_dw1(index, neuron, perf_elem, z):
        
    w1=.9*(perf_elem.d-z)*neuron.inputs[index]+neuron.weights[index]
    #update weights
    return w1

def calc_dw0(index, neuron, d, z):

    d0=neuron.weights[index]*d    
    w1=.9*d0*neuron.inputs[index]+neuron.weights[index]
    #update weights
    return w1                                       

""" working but not necessarily the most efficient"""                                           
def neural_net_two_layer():

    in0=[-1, 0]
    #in2=[-.5 -.5 0]
    w0=w1=w2=w0_0=w1_0=w2_0=[1, .9]
    
    desired_out=0.0
    p=PerformanceElement(0)
    
    n=list()
    n.append(Neuron(in0, w0))
    n.append(Neuron(in0, w1))
    n.append(Neuron([0, 0], w2))


    for i in range(0, 500):
            
        #calculate sum of inputs into node
        z0=n[0].calc_z()
        z1=n[1].calc_z()

        n[2].inputs=[z0, z1]

        z2=n[2].calc_z()
        #print "z=", z2
        #calculate error at layer 1
        error=p.d-z2

        #recalulate weights into layer 1
        for j in range(0, len(w2)):
            w2_0[j]=calc_dw1(j, n[2], p, z2)
        n[2].weights=w2_0

        #calculate the error at layer 0, neuron 1
        for k in range(0, len(w0)):
            w0_0[k]=calc_dw0(k, n[0], error,  z0)
        n[0].weights=w0_0
        
        for m in range(0, len(w1)):
            w1_0[m]=calc_dw0(m, n[1], error,  z1)
        n[1].weights=w1_0    
    print "z=", z2    
    return

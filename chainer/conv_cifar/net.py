import chainer
import chainer.functions as F
import chainer.links as L


class CifarMLP(chainer.Chain):

    """An example of multi-layer perceptron for CIFAR dataset.

    This is a very simple implementation of an MLP. You can modify this code to
    build your own neural net.

    """
    def __init__(self, n_out):
        super(CifarMLP, self).__init__(
            l1=L.Convolution2D(3, 100, 5, pad=2),
            l2=L.Convolution2D(100, 50, 3, pad=1),
            l3=L.Linear(12800, 1024),
            l4=L.Linear(1024, 256),
            l5=L.Linear(256, n_out),
        )

    def __call__(self, x):
#        h0 = F.dropout(x);
        h0 = x;
        h1 = F.max_pooling_2d(F.relu(self.l1(h0)), 2)
        h2 = F.relu(self.l2(h1))
        h3 = F.dropout(F.relu(self.l3(h2)))
        h4 = F.dropout(F.relu(self.l4(h3)))
        return F.relu(self.l5(h4))


class MnistMLPParallel(chainer.Chain):

    """An example of model-parallel MLP.

    This chain combines four small MLPs on two different devices.

    """
    def __init__(self, n_in, n_units, n_out):
        super(MnistMLPParallel, self).__init__(
            first0=MnistMLP(n_in, n_units // 2, n_units).to_gpu(0),
            first1=MnistMLP(n_in, n_units // 2, n_units).to_gpu(1),
            second0=MnistMLP(n_units, n_units // 2, n_out).to_gpu(0),
            second1=MnistMLP(n_units, n_units // 2, n_out).to_gpu(1),
        )

    def __call__(self, x):
        # assume x is on GPU 0
        x1 = F.copy(x, 1)

        z0 = self.first0(x)
        z1 = self.first1(x1)

        # sync
        h0 = z0 + F.copy(z1, 0)
        h1 = z1 + F.copy(z0, 1)

        y0 = self.second0(F.relu(h0))
        y1 = self.second1(F.relu(h1))

        # sync
        y = y0 + F.copy(y1, 0)
        return y

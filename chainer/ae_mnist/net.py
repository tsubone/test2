import six

import chainer
import chainer.functions as F
from chainer.functions.loss.vae import gaussian_kl_divergence
import chainer.links as L


class VAE(chainer.Chain):
    """Variational AutoEncoder"""
    def __init__(self,):
        super(VAE, self).__init__(
            # encoder
            le1=L.Convolution2D(1, 16, 5, pad=2),
            le2=L.Linear(3136, 1024),
            le3=L.Linear(1024, 256),
            le4=L.Linear(256, 64),
            le5=L.Linear(64, 32),
            # decoder
            ld5=L.Linear(32, 64),
            ld4=L.Linear(64, 256),
            ld3=L.Linear(256, 1024),
            ld2=L.Linear(1024, 3136),
            ld1=L.Linear(3136, 784),
        )
        self.stack=0

    def __call__(self, x, sigmoid=True):
        """AutoEncoder"""
        return self.decode(self.encode(x), sigmoid)

    def encode(self, x):
        h1 = F.max_pooling_2d(F.relu(self.le1(x)) ,2)
        if self.stack<=0:
            return h1
        h2 = F.dropout(F.relu(self.le2(h1)))
        if self.stack<=1:
            return h2
        h3 = F.dropout(F.relu(self.le3(h2)))
        if self.stack<=2:
            return h3
        h4 = F.dropout(F.relu(self.le4(h3)))
        if self.stack<=3:
            return h4
        h5 = F.dropout(F.relu(self.le5(h4)))
        return h5


    def decode(self, z, sigmoid=True):
        if self.stack >=4:
            h5 = F.relu(self.ld5(z))
        else:
            h5 = z
        if self.stack >=3:
            h4 = F.relu(self.ld4(h5))
        else:
            h4 = h5
        if self.stack >=2:
            h3 = F.relu(self.ld3(h4))
        else:
            h3 = h4
        if self.stack >=1:
            h2 = F.relu(self.ld2(h3))
        else:
            h2 = h3
        h1 = F.relu(self.ld1(h2))
        return chainer.Variable(h1.data.reshape (len(h1.data), 1, 28, 28))


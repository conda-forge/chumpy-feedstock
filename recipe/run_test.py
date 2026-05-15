import numpy as np

import chumpy as ch


x = ch.array([1.0, 2.0, 3.0])
y = ch.sum(x * x)
derivative = np.asarray(y.dr_wrt(x))

assert np.allclose(y.r, [14.0])
assert np.allclose(derivative, [[2.0, 4.0, 6.0]])

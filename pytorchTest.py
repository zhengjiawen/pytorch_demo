import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

m = torch.randn(32,32,32,32)
# m = np.array([[[2,3,4,8],
#               [1,5,3,2],
#               [7,1,5,3],
#               [1,2,3,4]],
#               [[2, 3, 4, 8],
#                [1, 5, 3, 2],
#                [7, 1, 5, 3],
#                [1, 2, 3, 4]]
#              ])
#
# m = torch.from_numpy(m)


print(m.size())


n = F.max_pool2d(m, (2,2))
print(n.size())
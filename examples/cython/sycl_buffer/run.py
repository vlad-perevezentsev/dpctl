#                      Data Parallel Control (dpctl)
#
# Copyright 2020-2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import syclbuffer as sb
import numpy as np
import dpctl

X = np.random.randn(100, 4)

print("Result computed by NumPy")
print(X.sum(axis=0))
print("Result computed by SYCL extension using default offloading target")
print(sb.columnwise_total(X))


print("")

# controlling where to offload

q = dpctl.SyclQueue("opencl:gpu")
print("Running on: ", q.sycl_device.name)
print(sb.columnwise_total(X, queue=q))

q = dpctl.SyclQueue("opencl:cpu")
print("Running on: ", q.sycl_device.name)
print(sb.columnwise_total(X, queue=q))

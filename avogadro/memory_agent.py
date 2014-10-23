#------------------------------------------------------------------------------
# Copyright 2013-2014 Numenta Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
from agent import AvogadroAgent
import psutil

from model_params import getModelParams



class AvogadroMemoryAgent(AvogadroAgent):
  name = "MemoryPercent"
  minVal = 0.0
  maxVal = 100.0
  numBuckets = 284.0
  resolution = max(0.001, (maxVal - minVal) / numBuckets)

  ENCODER_PARAMS = {
    name: {
      "name": name,
      "fieldname": name,
      "resolution": resolution,
      "seed": 42,
      "type": "RandomDistributedScalarEncoder"
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    return psutil.virtual_memory().percent

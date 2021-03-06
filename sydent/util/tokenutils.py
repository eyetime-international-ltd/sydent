# -*- coding: utf-8 -*-

# Copyright 2014 OpenMarket Ltd
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

import string
import random

r = random.SystemRandom()

def generateTokenForMedium(medium):
    if medium == 'email':
        return generateAlphanumericTokenOfLength(32)
    else:
        return generateNumericTokenOfLength(6)

def generateNumericTokenOfLength(length):
    return "".join([r.choice(string.digits) for _ in range(length)])

def generateAlphanumericTokenOfLength(length):
    return "".join([r.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase) for _ in range(length)])

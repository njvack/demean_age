#!/usr/bin/env python

import sys
import numpy as np

age = np.loadtxt(sys.argv[1], skiprows=1, usecols=3)

mean_age = sum(age)/len(age)

np.savetxt("demeaned_age.txt", age-mean_age)

print("done!")

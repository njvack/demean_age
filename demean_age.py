#!/usr/bin/env python

import sys
import numpy as np
import pandas

participant_data = pandas.read_csv(sys.argv[1], sep='\t')

mean_age = participant_data.age.mean()

assert mean_age > 12
assert mean_age < 100

np.savetxt("demeaned_age.txt", participant_data.age-mean_age)

print("done!")

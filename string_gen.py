import string
import random
import numpy as np

def id_generator(N=6, chars=string.ascii_uppercase + string.digits, size = 100):
	str_list = []
	for i in range(100):
		str_list.append(''.join(random.choice(chars) for i in range(N)))
	return str_list

print(np.random.random_sample((5,)))
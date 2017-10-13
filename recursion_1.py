def is_even(x):

	if x % 2 == 0:
		return True
	else:
		return is_odd(x-1)

def is_odd(x):

	return not is_even(x)

print(is_even(19))
print(is_odd(17))

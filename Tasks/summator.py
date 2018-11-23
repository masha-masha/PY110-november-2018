import numpy as np


class SummatorError(Exception):
    pass


class NotAList(SummatorError):
    pass


class InvalidType(SummatorError):
    pass


class EmptyList(SummatorError):
    pass

# additional task: check if types of all elements in array are the same as in numpy


def _check_types(arr: list):
    for x in arr:
        if type(x) not in np.core.numerictypes.allTypes.values():
            return False
    return True


def sum(arr):
	if type(arr) != list:
		raise NotAList
	if len(arr) == 0:
		raise EmptyList
		#return 0  # to safe some time if list is empty
	sum1 = 0
	for x in arr:
		if type(x) != (int or float):
			raise InvalidType
		sum1 += x
	return sum1

	
def avg(arr):
	if type(arr) != list:
		raise NotAList
	if len(arr) == 0:
		raise EmptyList
		#return 0  # to prevent a division by zero
	if _check_types(arr):
		print('All types are presented in numpy')
	else:
		print('At least one item has not numpy type')
	sum1 = 0
	for x in arr:
		if type(x) != (int or float):
			raise InvalidType
		sum1 += x
	return sum1 / len(arr)
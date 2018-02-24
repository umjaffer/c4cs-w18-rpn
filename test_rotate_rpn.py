#!/usr/bin/env python3

import rpn

def main():
	print("testing rotate function...")

	print("testing '1 2 3 4 5 6 7 rotate'")
	result = rpn.calculate("1 2 3 4 5 6 7 rotate")
	assert [7, 6, 5, 4, 3, 2, 1] == result
	print("The result is %s" %result)

	print("testing '99 555 3 rotate'")
	result = rpn.calculate("99 555 3 rotate")
	assert [3, 555, 99] == result
	print("The result is %s" %result)

	print("testing '7 6 5 4 3 2 1 rotate'")
	result = rpn.calculate("7 6 5 4 3 2 1 rotate")
	assert [1, 2, 3, 4, 5, 6, 7] == result
	print("The result is %s" %result)

	print("testing '2 4 6 rotate'")
	result = rpn.calculate("2 4 6 rotate")
	assert [6, 4, 2] == result
	print("The result is %s" %result)

	print("all tests passed!!")

if __name__ == '__main__':
	main()
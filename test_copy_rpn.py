#!/usr/bin/env python3

import rpn

def main():
	print("testing copy function...")

	print("testing '2 4 6 copy'")
	result = rpn.calculate("2 4 6 copy")
	assert [2, 2, 4, 6] == result
	print("The result is %s" %result)

	print("testing '4 66 4 copy'")
	result = rpn.calculate("4 66 4 copy")
	assert [4, 4, 66, 4] == result
	print("The result is %s" %result)

	print("testing '1 2 3 copy'")
	result = rpn.calculate("1 2 3 copy")
	assert [1, 1, 2, 3] == result
	print("The result is %s" %result)

	print("testing 100 100 100 copy")
	result = rpn.calculate("100 100 100 copy")
	assert [100, 100, 100, 100] == result
	print("The result is %s" %result)

	print("all tests passed!!")

if __name__ == '__main__':
	main()
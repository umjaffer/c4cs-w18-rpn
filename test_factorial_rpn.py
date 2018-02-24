#!/usr/bin/env python3

import rpn

def main():
	print("testing factorial (!) function...")

	print("testing '4 !'")
	result = rpn.calculate("4 !")
	assert 24 == result
	print("The result is %s" %result)

	print("testing '8 !'")
	result = rpn.calculate("8 !")
	assert 40320 == result
	print("The result is %s" %result)

	print("testing '5 !'")
	result = rpn.calculate("5 !")
	assert 120 == result
	print("The result is %s" %result)

	print("testing '0 !'")
	result = rpn.calculate("0 !")
	assert 1 == result
	print("The result is %s" %result)

	print("testing '1 !'")
	result = rpn.calculate("1 !")
	assert 1 == result
	print("The result is %s" %result)

	print("all tests passed!!")

if __name__ == '__main__':
	main()
from base64 import b64decode as b64d
from base64 import b64encode as b64e
from random import randint

def flag_generator():
	flag = "CBA{Reverse_engineering_is_awesome!}"

	flag = flag.encode('zlib')

	for i in range(randint(0, 10)):
		flag = b64e(flag)

	return b64e(flag)


# The last step of the generator is base64 encoding a random number of times between 0-10 inclusive. 
# So create a loop that repeats 11 times. 
# Use a try block to attempt to 'decode' - the next required step. If it fails, keep looping, if not
# end the loop early with a break, then
# decode the file to reverse the zlib encoding on line 8
# print the flag
def flag_degenerator(flag):

	for i in range(11):
		try:
				flag.decode('zlib')
				break
		except:
				print ("Count no: " + str(i))
				flag = b64d(flag)

	currentFlag = flag.decode('zlib')
	print ("The flag is: " + currentFlag)


# Alternative solution - Using recursion to find the solution
# Use a try block to test whether we can successfully decode the file.
# If it can't, the function does a single base64 decode, then calls itself recusively until it can decode the file. 
# When it can decode the file, it does so and then prints, knowing that there are no more base64 decodes required. 
def flag_degenerator_recusion(flag):
		try:
				print ("The flag is: " + flag.decode('zlib'))
		except:
				flag_degenerator_recusion(b64d(flag))


if __name__ == '__main__':
	flag = "Vm0xd1MwNUdXWGxWV0dSUFZsZG9XRmx0ZUV0V01XeDBaVWRHVjFac1NsWlZWbEpIVlRKS1NHVkdXbFpOVmtwWVZrZDRTMk14V25GWApiSEJYVWxSV2VWZFdaRFJaVjAxNFZHNUdWQXBpUmxwWVdXdG9RMUpXV2toTlZGSmFWbTFTV0ZkcmFFOVZkM0JwVjBkb2RsWkdXbUZqCk1EQjRWMjVLWVZKRlNsQlZha0poVFVaYVNFNVZkRlZhTTBKWVdXdFdkMVZXV2xkaFNHUnFDazFXV25wV01uUmhWakpLY21ORk9WZGkKV0dob1ZXcEdkMVpzV25SU2JGcFNWMFZLVmxaWE1UQmpiVlpYV2taV1ZXSnRVbkZEYXpGWFVtcFNWMDFxVmxSV1ZFcEhZMnMxVjFWcwpjRmNLVWxWd2IxWldVa2RXYlZaSFYyNVNVMkpGTlZkV01GWkxaR3hrVjFWclpGZGhlbFpZVld4b2MxZHRWblJsUmtwRVlrWmFXVlF3ClVuTlNSbkEyVFVSc1JGcDZNRGxEWnowOUNnPT0K"
	#flag = flag_generator()
	print ("Try to get the flag reversing the python script that generated it!")
	print ("Flag string: " + flag)
	
	flag_degenerator(flag)
	#flag_degenerator_recusion(flag)

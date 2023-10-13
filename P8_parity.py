nibble_to_bits = [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
def countSetBits(num):
	nibble = 0
	if (0 == num):
		return nibble_to_bits[0]
	nibble = num & 0xf
	return nibble_to_bits[nibble] + countSetBits(num >> 4)
def getParity(num):
	return countSetBits(num) % 2
n = 1
print("Parity of no", n, " = ", ["even", "odd"][getParity(n)])

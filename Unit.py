import unittest

def add (a,b,c=0):
		return a + b + c

class TestAddition(unittest.TestCase):
	
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_positive(self):
		self.assertEqual(add(3,4,5), 12)
		self.assertEqual(add(3,4), 7)
		self.assertEqual(add(1,1,5), 7)
	def test_negative(self):
		self.assertEqual(add(-1,3,4), 6)
		self.assertEqual(add(-2,-2,-1), -5)

if __name__=="__main__":
	unittest.main()

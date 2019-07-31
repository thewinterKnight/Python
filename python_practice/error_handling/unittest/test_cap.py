import unittest
import cap

class TestCap(unittest.TestCase):
	text = 'whats love gotta do with it'

	def test_one_word(self):
		result = cap.cap_first(self.text)
		expected_result = 'Whats love gotta do with it'

		self.assertEqual(result, expected_result)

	def test_all_words(self):
		self.text = 'mary had a little lamb'
		result = cap.cap_all(self.text)
		# print(TestCap.text, '\n', self.text)
		expected_result = 'Mary Had A Little Lamb'

		self.assertEqual(result, expected_result)

if __name__=='__main__':
	unittest.main()
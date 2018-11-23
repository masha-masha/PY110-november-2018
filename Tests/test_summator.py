import unittest
from Tasks.summator import sum as sum_, avg as avg_, SummatorError


class MyTestCase(unittest.TestCase):

	def test_sum_type(self):
		a = "something strange"
		with self.assertRaises(SummatorError, msg="На вход была подана строка"):
			sum_(a)

	def test_avg_type(self):
		a = "Hi!"
		with self.assertRaises(SummatorError, msg="На вход была подана строка"):
			avg_(a)

	def test_avg_inner_type(self):
		a = [3, 5, True, "O_o"]
		with self.assertRaises(SummatorError, msg="На вход был подан массив с некорректными данными"):
			avg_(a)

	def test_sum_inner_type(self):
		a = [3, 5, True, "O_o"]
		with self.assertRaises(SummatorError, msg="На вход был подан массив с некорректными данными"):
			sum_(a)

	def test_avg_empty(self):
		a = []
		with self.assertRaises(SummatorError, msg="На вход был подан пустой массив"):
			avg_(a)

	def test_sum_valid(self):
		a = [i for i in range(10)]
		self.assertEqual(sum(a), sum_(a), "Подсчет суммы неверен, должно было получиться {}".format(sum(a)))

	def test_avg_valid(self):
		a = [i for i in range(32)]
		self.assertEqual(avg_(a), sum(a)/len(a), "Подсчет среднего неверен, должно было получиться {}".format(sum(a)/len(a)))


if __name__ == '__main__':
	unittest.main()

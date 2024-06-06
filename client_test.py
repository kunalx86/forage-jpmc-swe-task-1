import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        bid, ask = quote['top_bid']['price'], quote['top_ask']['price']
        self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask, (bid + ask) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        bid, ask = quote['top_bid']['price'], quote['top_ask']['price']
        self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask, (bid + ask) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    price_a, price_b = 127.8, 129.45
    self.assertEqual(price_a / price_b, getRatio(price_a, price_b))
    
  def test_getRatio_calculateRationPriceBis0(self):
    price_a, price_b = 1.23, 0
    self.assertEqual(None, getRatio(price_a, price_b))



if __name__ == '__main__':
    unittest.main()

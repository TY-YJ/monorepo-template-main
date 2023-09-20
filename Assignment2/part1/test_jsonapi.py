import jsonapi
import unittest


class Test(unittest.TestCase):
  def test_encode_complex(self):
    obj = complex(2,5)
    encoded = jsonapi.dumps(obj)
    self.assertEqual(encoded,'{"real": 2.0, "img": 5.0, "__extended_json_type__": "complex"}')

  def test_encode_range(self):
    obj = range(2, 10, 3)
    encoded = jsonapi.dumps(obj)
    self.assertEqual(encoded,'{"start": 2, "stop": 10, "step": 3, "__extended_json_type__": "range"}')
  
  def test_decode_complex(self):
    obj = '{"real": 2.0, "img": 5.0, "__extended_json_type__": "complex"}'
    decoded = jsonapi.loads(obj)
    self.assertEqual(decoded, complex(2,5))

  def test_decode_range(self):
    obj = '{"start": 2, "stop": 10, "step": 3, "__extended_json_type__": "range"}'
    decoded = jsonapi.loads(obj)
    self.assertEqual(decoded, range(2, 10, 3))


if __name__ == '__main__':
  unittest.main()
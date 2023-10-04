# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_normal_item(self):
      items = [Item("Coke", sell_in=10, quality=40),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(9, items[0].sell_in)
      self.assertEqual(39, items[0].quality)

    def test_normal_item_quality_over_fifty(self):
      items = [Item("Coke", sell_in=20, quality=55),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(50, items[0].quality)
  
    def test_normal_item_sell_in_below_zero(self):
      items = [Item("Coke", sell_in=-1, quality=50),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(-2, items[0].sell_in)
      self.assertEqual(48, items[0].quality)      

    def test_aged_brie(self):
      items = [Item("Aged Brie", sell_in=10, quality=40),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(9, items[0].sell_in)
      self.assertEqual(41, items[0].quality)    

    def test_aged_brie_quality_over_fifty(self):
      items = [Item("Aged Brie", sell_in=10, quality=51),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(9, items[0].sell_in)
      self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
      items = [Item("Sulfuras, Hand of Ragnaros", sell_in=1, quality=60),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(1, items[0].sell_in)
      self.assertEqual(60, items[0].quality)
    
    def test_backstage_ten_or_less_days(self):
      items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=40),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(9, items[0].sell_in)
      self.assertEqual(42, items[0].quality)

    def test_backstage_five_or_less_days(self):
      items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(4, items[0].sell_in)
      self.assertEqual(43, items[0].quality)

    def test_backstage_after_concert(self):
      items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=40),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(-1, items[0].sell_in)
      self.assertEqual(0, items[0].quality)

    def test_backstage_normal(self):
      items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=30),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(10, items[0].sell_in)
      self.assertEqual(31, items[0].quality)

    def test_conjured(self):
      items = [Item("Conjured Mana Cake", sell_in=10, quality=40),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(9, items[0].sell_in)
      self.assertEqual(38, items[0].quality)

    def test_conjured_quality_over_fifty(self):
      items = [Item("Conjured Mana Cake", sell_in=10, quality=55),
      ]
      gilded_rose = GildedRose(items)
      gilded_rose.update_quality()
      self.assertEqual(9, items[0].sell_in)
      self.assertEqual(50, items[0].quality)

if __name__ == '__main__':
    unittest.main()

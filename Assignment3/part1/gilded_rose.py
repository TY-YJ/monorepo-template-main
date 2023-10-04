# -*- coding: utf-8 -*-
class Item:
  """ DO NOT CHANGE THIS CLASS!!!"""
  def __init__(self, name, sell_in, quality):
    self.name = name
    self.sell_in = sell_in
    self.quality = quality

  def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater:
  def update_quality(self, item):
    pass
  
  def quality_validater(self, item):
    if item.quality < 0:
      item.quality = 0
    elif item.quality > 50:
      item.quality = 50
    

class NormalItemUpdater(ItemUpdater):
  def update_quality(self, item):

    if 0 < item.quality <= 50:
      if item.sell_in <= 0:
        item.quality -= 2
      else:
        item.quality -= 1

    item.sell_in -= 1
    self.quality_validater(item)


class AgedBrieUpdater(ItemUpdater):
  def update_quality(self, item):
    if item.quality <= 50:
      item.quality += 1
    item.sell_in -= 1
    self.quality_validater(item)

class SulfurasUpdater(ItemUpdater):
  def update_quality(self, item):
    pass


class BackstagePassesUpdater(ItemUpdater):
  def update_quality(self, item):
    if 0 < item.sell_in <= 5:
      item.quality += 3
    elif 0 < item.sell_in <= 10:
      item.quality += 2
    elif item.sell_in <= 0:
      item.quality = 0
    else:
      item.quality += 1

    item.sell_in -= 1
    self.quality_validater(item)



class ConjuredUpdater(ItemUpdater):
  def update_quality(self, item):
    if 0 < item.quality <= 50:
      if item.sell_in <= 0:
        item.quality -= 4
      else:
        item.quality -= 2

    item.sell_in -= 1
    self.quality_validater(item)


# Factory design. 
# static method decorator allows to use function without creating instances
class ItemUpdaterFactory:
  @staticmethod
  def create_item_updater(item):
    if item.name == "Aged Brie":
      return AgedBrieUpdater()
    elif item.name == "Sulfuras, Hand of Ragnaros":
      return SulfurasUpdater()
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
      return BackstagePassesUpdater()
    elif item.name == "Conjured Mana Cake":
      return ConjuredUpdater()
    else:
      return NormalItemUpdater()


class GildedRose:
  def __init__(self, items: list[Item]):
    self.items = items

  def update_quality(self):
    updater_factory = ItemUpdaterFactory()
    for item in self.items:
      item_updater = updater_factory.create_item_updater(item)
      item_updater.update_quality(item)






# Strategy design

# class GildedRose(object):

#     def __init__(self, items: list[Item]):
#         # DO NOT CHANGE THIS ATTRIBUTE!!!
#         self.items = items

    # def update_quality(self):
    #     for item in self.items:
    #       if item.name == "Aged Brie":
    #         self.aged_brie_updater(item)
    #       elif item.name == "Sulfuras, Hand of Ragnaros":
    #         self.sulfuras_updater(item)
    #       elif item.name == "Backstage passes to a TAFKAL80ETC concert":
    #         self.backstage_passes_updater(item)
    #       elif item.name == "Conjured Mana Cake":
    #         self.conjured_updater(item)
    #       else:
    #         self.normal_item_updater(item)
    
    # def normal_item_updater(self, item):
    #   if 0 < item.quality <= 50:
    #     if item.sell_in <= 0:
    #       item.quality -= 2
    #     else:
    #       item.quality -= 1
    #   item.sell_in -= 1
      
    # def aged_brie_updater(self, item):
    #   if item.quality < 50:
    #     item.quality += 1
    #   item.sell_in -= 1

    # def sulfuras_updater(self, item):
    #   pass

    # def backstage_passes_updater(self, item):
    #   if item.sell_in <= 5:
    #     item.quality += 3
    #   elif item.sell_in <= 10:
    #     item.quality += 2
    #   elif item.sell_in <= 0:
    #     item.quality = 0
    #   else:
    #     item.quality += 1
      
    #   if item.quality > 50:
    #     item.quality = 50

    #   item.sell_in -= 1

    # def conjured_updater(self, item):
    #   if 0 < item.quality <= 50:
    #       if item.sell_in <= 0:
    #           item.quality -= 4
    #       else:
    #           item.quality -= 2
      
    #   item.sell_in -= 1


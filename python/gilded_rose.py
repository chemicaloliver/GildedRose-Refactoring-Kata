# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = []
        for item in items:
            self.items.append(self.categorize_item(item))

    def update_quality(self):
        for item in self.items:
            item.updateQuality()

    def categorize_item(self, item):
        if item.name == "Conjured Item":
            return ConjuredItem(item)
        if item.name == "Aged Brie":
            return AgedBrieItem(item)
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassItem(item)
        if item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItem(item)

        return GenericItem(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GenericItem(Item):

    def __init__(self, item):
         super().__init__(item.name, item.sell_in, item.quality)

    def updateQuality(self):
        if self.quality > 0:
            self.quality -= 1

        if self.sell_in < 0:
            self.quality -= 1

class ConjuredItem(Item):

    def __init__(self, item):
         super().__init__(item.name, item.sell_in, item.quality)

    def updateQuality(self):
         if self.quality > 0:
            self.quality -= 2

    
class SulfurasItem(Item):

    def __init__(self, item):
         super().__init__(item.name, item.sell_in, item.quality)

    def updateQuality(self):
        pass

class AgedBrieItem(Item):

    def __init__(self, item):
         super().__init__(item.name, item.sell_in, item.quality)

    def updateQuality(self):
         if self.quality < 50:
                self.quality += 1

class BackstagePassItem(Item):

    def __init__(self, item):
         super().__init__(item.name, item.sell_in, item.quality)

    def updateQuality(self):
        if self.sell_in < 6:
            if self.quality < 50:
                self.quality +=  3

        elif self.sell_in < 11:
            if self.quality < 50:
                self.quality += 2
        
        if self.sell_in <= 0:
            self.quality = 0



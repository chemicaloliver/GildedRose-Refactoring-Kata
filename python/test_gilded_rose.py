# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


    def test_sulfuras_quality_always_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

        items = [Item("Sulfuras, Hand of Ragnaros", -10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_quality_degrades_faster_after_sell__by_date(self):
        starting_quality = 10
        items = [
            Item("foo", 5, starting_quality), # 5 days left to sell
            Item("foo", -1, starting_quality) # 1 day over sell by date
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertGreater((starting_quality - items[1].quality), (starting_quality - items[0].quality) )

    def test_quality_is_never_less_than_zero(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual( 0 , items[0].quality)

    def test_aged_brie_increases_quality_with_age(self):
        starting_quality = 10
        
        items = [Item("Aged Brie", 5, starting_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertGreater(items[0].quality, starting_quality)

    def test_backstage_passes_increases_by_2_under_10_days(self):
        starting_quality = 10
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, starting_quality)]
        gilded_rose = GildedRose(items)
        
        previous_quality = starting_quality

        for i in range(5):
            gilded_rose.update_quality()
            self.assertEqual(2, items[0].quality - previous_quality)
            previous_quality = items[0].quality

    def test_backstage_passes_decreases_by_3_under_5_days(self):
        starting_quality = 10
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, starting_quality)]
        gilded_rose = GildedRose(items)
        
        previous_quality = starting_quality

        for i in range(5):
            gilded_rose.update_quality()
            self.assertEqual(3, items[0].quality - previous_quality)
            previous_quality = items[0].quality

    def test_backstage_passes_decrease_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual( 0 , items[0].quality)

    def test_conjured_items_degrade_in_quality_faster(self):
        starting_quality = 10
        items = [
            Item("Conjured Item", 10, starting_quality),
            Item("foo", 10, starting_quality)
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual((starting_quality - items[1].quality), (starting_quality - items[0].quality)/2 )

if __name__ == '__main__':
    unittest.main()

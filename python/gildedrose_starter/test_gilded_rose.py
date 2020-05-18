# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # Any other item
    def test_quality_decreases_for_any_other_item(self):

    def test_quality_is_never_negative(self):
        # Arrange
        items = [Item("any_other_item", 0, 0)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(0, items[0].quality)

    def test_sell_in_goes_down(self):
        # Arrange
        items = [Item("any_other_item", 0, 0)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_degrades_twice_as_fast_when_sell_in_is_negative(self):
        # Arrange
        items = [Item("any_other_item", -1, 4)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(2, items[0].quality)

    def test_sulfuras_does_not_decrease_in_quality(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 4)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(4, items[0].quality)

    def test_aged_brie_does_not_decrease_in_quality(self):
        # Arrange
        items = [Item("Aged Brie", -1, 4)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertGreater(items[0].quality, 4)




if __name__ == "__main__":
    unittest.main()

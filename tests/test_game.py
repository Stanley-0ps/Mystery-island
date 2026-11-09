
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import main


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        main.player_inventory = []
        main.player_energy = 5
        main.player_location = "Beach"
        main.game_running = True

    def test_collect_item(self):
        main.collect_items("lantern")
        self.assertIn("lantern", main.player_inventory)

    def test_prevent_duplicate_item(self):
        main.collect_items("rope")
        main.collect_items("rope")
        self.assertEqual(main.player_inventory.count("rope"), 1)

    def test_empty_inventory(self):
        output = StringIO()
        with redirect_stdout(output):
            main.show_inventory()
        self.assertIn("Your inventory is empty.", output.getvalue())

    def test_inventory_contains_item(self):
        main.player_inventory = ["lantern"]
        output = StringIO()
        with redirect_stdout(output):
            main.show_inventory()
        self.assertIn("lantern", output.getvalue())

    def test_travel_to_jungle(self):
        with patch("builtins.input", return_value="2"):
            main.explore_island()
        self.assertEqual(main.player_location, "Jungle")
        self.assertEqual(main.player_energy, 4)

    def test_cave_requires_lantern(self):
        with patch("builtins.input", return_value="3"):
            main.explore_island()
        self.assertEqual(main.player_location, "Beach")
        self.assertEqual(main.player_energy, 5)

    def test_bridge_requires_rope(self):
        with patch("builtins.input", return_value="4"):
            main.explore_island()
        self.assertEqual(main.player_location, "Beach")
        self.assertEqual(main.player_energy, 5)

    def test_lighthouse_win(self):
        main.player_inventory = ["lantern", "rope"]
        with patch("builtins.input", return_value="5"):
            main.explore_island()
        self.assertEqual(main.player_location, "Lighthouse")
        self.assertFalse(main.game_running)


if __name__ == "__main__":
    unittest.main()

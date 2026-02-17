import os
import unittest
from unittest.mock import patch

import meme_generator


class MemeGeneratorTests(unittest.TestCase):
    def test_create_meme_generates_file(self):
        with patch("meme_generator.random.randint", return_value=1234):
            output_path = meme_generator.create_meme("bugs")

        self.assertEqual(output_path, "static/meme_1234.jpg")
        self.assertTrue(os.path.exists(output_path))

    def test_create_meme_handles_blank_topic(self):
        with patch("meme_generator.random.randint", return_value=5678):
            output_path = meme_generator.create_meme("   ")

        self.assertEqual(output_path, "static/meme_5678.jpg")
        self.assertTrue(os.path.exists(output_path))


if __name__ == "__main__":
    unittest.main()

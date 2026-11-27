from pathlib import Path
import tempfile
import unittest

from scripts.validate_xray import validate


class XrayValidationTests(unittest.TestCase):
    def test_duplicate_ids_are_rejected_before_publication(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / 'xray/acceptance'
            directory.mkdir(parents=True)
            feature = directory / 'core.feature'
            feature.write_text('Feature: Digest\n  @id:1\n  Scenario: First\n    Given a change\n')
            self.assertEqual(validate(root), 1)
            feature.write_text(feature.read_text() + '  @id:1\n  Scenario: Second\n    Given a change\n')
            with self.assertRaisesRegex(ValueError, 'unique'):
                validate(root)

    def test_symlink_cannot_import_files_outside_the_acceptance_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / 'xray/acceptance'
            directory.mkdir(parents=True)
            outside = root / 'outside.feature'
            outside.write_text('Feature: Outside\n  @id:1\n  Scenario: First\n    Given a change\n')
            (directory / 'core.feature').symlink_to(outside)
            with self.assertRaisesRegex(ValueError, 'escapes'):
                validate(root)

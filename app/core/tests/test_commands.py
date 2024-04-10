"""
Tests for custom django commands
"""

from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase
from django.db.utils import OperationalError
from django.core.management import call_command
from psycopg2.errors import OperationalError as Psycopg2OpError


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """
    Tests for custom django commands
    """

    def test_wait_for_db_ready(self, patched_check: MagicMock) -> None:
        """
        Tests for wait for db command when db is ready
        """
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delayed(self,
                                 patched_sleep: MagicMock,
                                 patched_check: MagicMock) -> None:
        """
        Tests the wait for db command when the db is startup is delayed
        """
        patched_sleep.return_value = None
        patched_check.side_effect = (
            [Psycopg2OpError] * 2 +
            [OperationalError] * 3 +
            [True]
        )
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

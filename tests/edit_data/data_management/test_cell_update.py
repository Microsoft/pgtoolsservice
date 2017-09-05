# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import unittest

from pgsqltoolsservice.edit_data.update_management import CellUpdate
from pgsqltoolsservice.query_execution.contracts.common import DbColumn, DbCellValue
from pgsqltoolsservice.edit_data.contracts import EditCell


class TestCellUpdate(unittest.TestCase):

    def setUp(self):
        self._db_column = DbColumn()
        self._db_column.data_type = 'varchar'
        self._new_cell_value = 'New Value'
        self._cell_update = CellUpdate(self._db_column, self._new_cell_value)

    def test_value_set_to_right_text_with_str_datatype(self):
        self.assertEqual(self._new_cell_value, self._cell_update.value)

        self.assertTrue(type(self._cell_update.value) is str)

    def test_value_as_string(self):

        value = self._cell_update.value_as_string

        self.assertTrue(value is self._new_cell_value)

    def test_as_edit_cell(self):

        edit_cell = self._cell_update.as_edit_cell

        self.assertTrue(edit_cell.display_value is self._new_cell_value)
        self.assertTrue(edit_cell.is_dirty)
        self.assertTrue(type(edit_cell) is EditCell)

    def test_as_db_cell_value(self):

        db_cell_value = self._cell_update.as_db_cell_value

        self.assertTrue(db_cell_value.display_value is self._cell_update.value_as_string)
        self.assertTrue(db_cell_value.is_null is False)
        self.assertTrue(db_cell_value.raw_object is self._cell_update.value)
        self.assertTrue(type(db_cell_value) is DbCellValue)


if __name__ == '__main__':
    unittest.main()

# Copyright (c) 2024, Test and Contributors
# See license.txt

import frappe
import unittest

from frappe.tests.utils import FrappeTestCase

class TestGitWorkflow(FrappeTestCase):
	def test_sum_of_list(self):
		a = self.sum_of_list()
		self.assertEqual(a , 15)	

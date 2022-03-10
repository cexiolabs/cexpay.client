from unittest import TestCase
import unittest

from cexpay.api.v2 import ApiV2

class OrderFetchTest(TestCase):
	def setUp(self):
		"Hook method for setting up the test fixture before exercising it."
		pass

	def tearDown(self):
		"Hook method for deconstructing the test fixture after testing it."
		pass

	@unittest.skip("Set order id")
	def test_order_fetch(self):
		cexpay_api_key="11111111111111111111111111111111"
		cexpay_api_passphrase="meow-meow"
		cexpay_api_secret="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
		cexpay_api_url="http://127.0.0.1:38080"
		api_v2 = ApiV2(cexpay_api_key, cexpay_api_passphrase, cexpay_api_secret, cexpay_api_url)
		order_id="CPO-5e70a10110ac4b599579be6dc90e016b"
		order=api_v2.order_fetch(order_id)

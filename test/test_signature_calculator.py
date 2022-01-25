from unittest import TestCase

from cexpay.api.security import SignatureCalculator

class SignatureCalculatorTest(TestCase):
	def setUp(self):
		"Hook method for setting up the test fixture before exercising it."
		pass

	def tearDown(self):
		"Hook method for deconstructing the test fixture after testing it."
		pass

	def test_signature_calculator(self):
		secret: str = "cNmgFLOwbckPszgJdUe4rdpcUo2IBHtNPsyxAScjl7CN4omMN64UJAvODT8PsrPIfR7TosKUfEFROyhz/YJxsw=="
		timestamp: str = "1573753848"
		http_method: str = "POST"
		url_path: str = "/v2/order?something=42"
		body_str: str = "{\"clientOrderId\":\"1490548887804-XA-1112-TU\",\"clientOrderTag\":\"Any merchant data\",\"instrument\":\"CRYPTO_SELL\",\"feeModel\":\"INCLUDED\",\"from\":{\"currency\":\"BTC\"},\"to\":{\"currency\":\"USD\",\"amount\":\"150.42\"}}"
		body_raw: str = body_str.encode("UTF-8")
		signatureCalculator = SignatureCalculator(secret)
		signature = signatureCalculator.sing(timestamp, http_method, url_path, body_raw)
		self.assertIsInstance(signature, str, "'signature' should be instace of str")
		self.assertEqual(signature, "00O36QWCSc9/rmtxiqCnPQiHXr5xaXlZIf2nkdm9PUk=")
		pass

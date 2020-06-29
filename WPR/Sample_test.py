import pytest
#from WPR.TransferSiteTest import tssite
class TestMethod():

	#@pytest.mark.p2
	'''def test_fileA(self):
		tssite.test_ts(self)
		#x=5

		#y=6
		#assert x+1 == y,"test failed"'''

	@pytest.mark.p2R
	def test_fileB(self):
		x=5
		y=6
		assert x+1 == y,"test failed"
		#assert x == y,"test failed"


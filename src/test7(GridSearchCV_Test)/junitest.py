import unittest
import core
from sklearn.model_selection import train_test_split
import sklearn.ensemble as ske

class BytesHistogramTest(unittest.TestCase):
    def test(self):
        X = core.ByteHistogram(r'C:\Users\kgg19\Documents\dataset\TrainSet\000aadad7b6e9316638e920f863855e7.vir')
        print(X)

if __name__=='__main__':
    unittest.main()
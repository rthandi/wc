import unittest
import sys
import wc

class NameSpace:
    def __init__(self, l, w, c, filename):
        self.l = l
        self.w = w
        self.c = c
        self.filename = filename

class TestValidInputs(unittest.TestCase):
    def testEmpty(self):
        inputs = NameSpace(False, False, False, [['testinputs/empty.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,0,0, False, False))

    def test1Byte(self):
        inputs = NameSpace(False, False, False, [['testinputs/1byte.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,1,1, False, False))

    def test1Word(self):
        inputs = NameSpace(False, False, False, [['testinputs/1word.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,1,4, False, False))

    def test2Words(self):
        inputs = NameSpace(False, False, False, [['testinputs/2words.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,2,8, False, False))

    def testMultipleLines(self):
        inputs = NameSpace(False, False, False, [['testinputs/multipleLines.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (2,3,11, False, False))

    def testMultipleLinesAndWords(self):
        inputs = NameSpace(False, False, False, [['testinputs/multipleWordsAndLines.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (2,7,41, False, False))

    def testMultipleEmptyLines(self):
        inputs = NameSpace(False, False, False, [['testinputs/multipleEmptyLines.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (7,0,7, False, False))

    def testMixedEmptyLines(self):
        inputs = NameSpace(False, False, False, [['testinputs/mixedEmptyLines.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (6,15,72, False, False))

    def testPdf(self):
        inputs = NameSpace(False, False, False, [['testinputs/pdfTestMultipleLines.pdf']])
        out = wc.run(inputs, [])
        # Will fail due to bug in code not test
        self.assertEqual(out, (183,641,18548, False, False))

    def testUnicode(self):
        inputs = NameSpace(False, False, False, [['testinputs/unicodeTest.txt']])
        out = wc.run(inputs, [])
        # Will fail due to bug in code not test
        self.assertEqual(out, (1522,77501,327679, False, False))

class TestInvalidInputs(unittest.TestCase):
    def testIncorrectPath(self):
        inputs = NameSpace(False, False, False, [['testinputs/notARealFile.txt']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,0,0, False, True))

    def testHyphen(self):
        inputs = NameSpace(False, False, False, [['-']])
        out = wc.run(inputs, [])
        self.assertEqual(out, "not handled")

    def testTwoHyphen(self):
        out = wc.verifyInputs(['--'])
        self.assertEqual(out, "not handled")

    def testNotSupportedFlag(self):
        out = wc.verifyInputs(['-L'])
        self.assertEqual(out, "not handled")

    def testBadFlag(self):
        out = wc.verifyInputs(['-asd'])
        self.assertEqual(out, "invalid")

    def testDirectoryNoSlash(self):
        inputs = NameSpace(False, False, False, [['testinputs/directoryTest']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,0,0, True, False))

    def testDirectoryWithSlash(self):
        inputs = NameSpace(False, False, False, [['testinputs/directoryTest/']])
        out = wc.run(inputs, [])
        self.assertEqual(out, (0,0,0, True, False))

class testFlags(unittest.TestCase):
    def testFlagL(self):
        inputs = NameSpace(True, False, False, [['testinputs/1word.txt']])
        out = wc.processFlags(inputs)
        self.assertEqual(out, (True, False, False))

class testOutputBuilder(unittest.TestCase):
    def testLines(self):
        out = wc.outputBuilder('1','2','3',True, False, False,'test.txt')
        self.assertEqual(out, '\t1\ttest.txt')

    def testWords(self):
        out = wc.outputBuilder('1','2','3',False, True, False,'test.txt')
        self.assertEqual(out, '\t2\ttest.txt')

    def testChars(self):
        out = wc.outputBuilder('1','2','3',False, False, True,'test.txt')
        self.assertEqual(out, '\t3\ttest.txt')

    def testChars(self):
        out = wc.outputBuilder('1','2','3',False, False, True,'test.txt')
        self.assertEqual(out, '\t3\ttest.txt')

    def testLinesAndWords(self):
        out = wc.outputBuilder('1','2','3',True, True, False,'test.txt')
        self.assertEqual(out, '\t1\t2\ttest.txt')

    def testLinesAndChars(self):
        out = wc.outputBuilder('1','2','3',True, False, True,'test.txt')
        self.assertEqual(out, '\t1\t3\ttest.txt')

    def testWordsAndChars(self):
        out = wc.outputBuilder('1','2','3',False, True, True,'test.txt')
        self.assertEqual(out, '\t2\t3\ttest.txt')

    def testAll(self):
        out = wc.outputBuilder('1','2','3',True, True, True,'test.txt')
        self.assertEqual(out, '\t2\t3\ttest.txt')


if __name__ == '__main__':
    unittest.main()
# def generate_expected(line, word, byte, file):
#     return "b'" + line + "\t" + word + "\t" + byte + "\t" + file + "\n'"

r""""
Empty
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/empty.txt', shell=True)
b'0\t0\t0\ttestinputs/empty.txt\n'

1 byte
>>> subprocess.check_output('python3 wc.py testinputs/1byte.txt', shell=True)
b'0\t1\t1\ttestinputs/1byte.txt\n'

1 word
>>> subprocess.check_output('python3 wc.py testinputs/1word.txt', shell=True)
b'0\t1\t4\ttestinputs/1word.txt\n'

2 words
>>> subprocess.check_output('python3 wc.py testinputs/2words.txt', shell=True)
b'0\t2\t8\ttestinputs/2words.txt\n'

Multiple lines
>>> subprocess.check_output('python3 wc.py testinputs/multipleLines.txt', shell=True)
b'2\t3\t11\ttestinputs/multipleLines.txt\n'

Multiple words and lines
>>> subprocess.check_output('python3 wc.py testinputs/multipleWordsAndLines.txt', shell=True)
b'2\t7\t41\ttestinputs/multipleWordsAndLines.txt\n'

A file with multiple empty lines
>>> subprocess.check_output('python3 wc.py testinputs/multipleEmptyLines.txt', shell=True)
b'7\t0\t7\ttestinputs/multipleEmptyLines.txt\n'

Empty lines between lines with words
>>> subprocess.check_output('python3 wc.py testinputs/mixedEmptyLines.txt', shell=True)
b'6\t15\t72\ttestinputs/mixedEmptyLines.txt\n'

Incorrect file path
>>> subprocess.check_output('python3 wc.py testinputs/notARealFile.txt', shell=True)
b'wc: testinputs/notARealFile.txt: No such file or directory\n'

- as input
>>> subprocess.check_output('python3 wc.py -', shell=True)
b"We don't handle that situation yet!\n"

-- as input
>>> subprocess.check_output('python3 wc.py --', shell=True)
b"We don't handle that situation yet!\n"

Valid but not currently supported flag
>>> subprocess.check_output('python3 wc.py -c', shell=True)
b"We don't handle that situation yet!\n"

--asd as input
>>> subprocess.check_output('python3 wc.py -asd', shell=True)
b"wc: invalid option -- a'\nTry 'python3 wc --help' for more information.\n"

-asd as input
>>> subprocess.check_output('python3 wc.py --asd', shell=True)
b"wc: unrecognised option '--asd'\nTry 'python3 wc --help' for more information.\n"

directory as test no ending /
>>> subprocess.check_output('python3 wc.py testinputs/directoryTest', shell=True)
b'wc: testinputs/directoryTest: Is a directory\n0\t0\t0\ttestinputs/directoryTest\n'

directory as test with ending /
>>> subprocess.check_output('python3 wc.py testinputs/directoryTest/', shell=True)
b'wc: testinputs/directoryTest/: Is a directory\n0\t0\t0\ttestinputs/directoryTest/\n'

Test with a pdf
>>> subprocess.check_output('python3 wc.py testinputs/pdfTestMultipleLines.pdf', shell=True)
b'183\t641\t18548\ttestinputs/pdfTestMultipleLines.pdf\n'

Test with a jpeg
>>> subprocess.check_output('python3 wc.py testinputs/jpgTest.jpg', shell=True)
b'4813\t26088\t1238933\ttestinputs/jpgTest.jpg\n'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

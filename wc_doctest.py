
r""""
Empty
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/empty.txt', shell=True)
b'\t0\t0\t0\ttestinputs/empty.txt\n'

1 byte
>>> subprocess.check_output('python3 wc.py testinputs/1byte.txt', shell=True)
b'\t0\t1\t1\ttestinputs/1byte.txt\n'

1 word
>>> subprocess.check_output('python3 wc.py testinputs/1word.txt', shell=True)
b'\t0\t1\t4\ttestinputs/1word.txt\n'

2 words
>>> subprocess.check_output('python3 wc.py testinputs/2words.txt', shell=True)
b'\t0\t2\t8\ttestinputs/2words.txt\n'

Multiple lines
>>> subprocess.check_output('python3 wc.py testinputs/multipleLines.txt', shell=True)
b'\t2\t3\t11\ttestinputs/multipleLines.txt\n'

Multiple words and lines
>>> subprocess.check_output('python3 wc.py testinputs/multipleWordsAndLines.txt', shell=True)
b'\t2\t7\t41\ttestinputs/multipleWordsAndLines.txt\n'

A file with multiple empty lines
>>> subprocess.check_output('python3 wc.py testinputs/multipleEmptyLines.txt', shell=True)
b'\t7\t0\t7\ttestinputs/multipleEmptyLines.txt\n'

Empty lines between lines with words
>>> subprocess.check_output('python3 wc.py testinputs/mixedEmptyLines.txt', shell=True)
b'\t6\t15\t72\ttestinputs/mixedEmptyLines.txt\n'

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
>>> subprocess.check_output('python3 wc.py -L', shell=True)
b"We don't handle that situation yet!\n"

-asd as input
>>> subprocess.check_output('python3 wc.py --asd', shell=True)
b"wc: invalid option -- '-'\nTry 'python3 wc --help' for more information.\n"

directory as test no ending /
>>> subprocess.check_output('python3 wc.py testinputs/directoryTest', shell=True)
b'wc: testinputs/directoryTest: Is a directory\n\t0\t0\t0\ttestinputs/directoryTest\n'

directory as test with ending /
>>> subprocess.check_output('python3 wc.py testinputs/directoryTest/', shell=True)
b'wc: testinputs/directoryTest/: Is a directory\n\t0\t0\t0\ttestinputs/directoryTest/\n'

Test directory in list of multiple files
>>> subprocess.check_output('python3 wc.py testinputs/multipleWordsAndLines.txt testinputs/directoryTest/ testinputs/mixedEmptyLines.txt', shell=True)
b'\t2\t7\t41\ttestinputs/multipleWordsAndLines.txt\nwc: testinputs/directoryTest/: Is a directory\n\t0\t0\t0\ttestinputs/directoryTest/\n\t6\t15\t72\ttestinputs/mixedEmptyLines.txt\n\t8\t22\t113\ttotal\n'

Test with a pdf
>>> subprocess.check_output('python3 wc.py testinputs/pdfTestMultipleLines.pdf', shell=True)
b'\t183\t641\t18548\ttestinputs/pdfTestMultipleLines.pdf\n'

Test with a jpeg
>>> subprocess.check_output('python3 wc.py testinputs/jpgTest.jpg', shell=True)
b'\t4813\t26088\t1238933\ttestinputs/jpgTest.jpg\n'

Test all unicode characters
>>> subprocess.check_output('python3 wc.py testinputs/unicodeTest.txt', shell=True)
b'\t1522\t77501\t327679\ttestinputs/unicodeTest.txt\n'

Test multiple files as input
>>> subprocess.check_output('python3 wc.py testinputs/mixedEmptyLines.txt testinputs/multipleWordsAndLines.txt', shell=True)
b'\t6\t15\t72\ttestinputs/mixedEmptyLines.txt\n\t2\t7\t41\ttestinputs/multipleWordsAndLines.txt\n\t8\t22\t113\ttotal\n'

Test flag -l
>>> subprocess.check_output('python3 wc.py -l testinputs/multipleWordsAndLines.txt', shell=True)
b'\t2\ttestinputs/multipleWordsAndLines.txt\n'

Test flag -w
>>> subprocess.check_output('python3 wc.py -w testinputs/multipleWordsAndLines.txt', shell=True)
b'\t7\ttestinputs/multipleWordsAndLines.txt\n'

Test flag -c
>>> subprocess.check_output('python3 wc.py -c testinputs/multipleWordsAndLines.txt', shell=True)
b'\t41\ttestinputs/multipleWordsAndLines.txt\n'

Test flag -lw
>>> subprocess.check_output('python3 wc.py -lw testinputs/multipleWordsAndLines.txt', shell=True)
b'\t2\t7\ttestinputs/multipleWordsAndLines.txt\n'

Test flag -lc
>>> subprocess.check_output('python3 wc.py -lc testinputs/multipleWordsAndLines.txt', shell=True)
b'\t2\t41\ttestinputs/multipleWordsAndLines.txt\n'

Test flag -wc
>>> subprocess.check_output('python3 wc.py -wc testinputs/multipleWordsAndLines.txt', shell=True)
b'\t7\t41\ttestinputs/multipleWordsAndLines.txt\n'

Test flag -lwc
>>> subprocess.check_output('python3 wc.py -lwc testinputs/multipleWordsAndLines.txt', shell=True)
b'\t2\t7\t41\ttestinputs/multipleWordsAndLines.txt\n'

Test that flag order does not matter using -wcl
>>> subprocess.check_output('python3 wc.py -wcl testinputs/multipleWordsAndLines.txt', shell=True)
b'\t2\t7\t41\ttestinputs/multipleWordsAndLines.txt\n'

Test flags seperated
>>> subprocess.check_output('python3 wc.py -l -c testinputs/multipleWordsAndLines.txt -w', shell=True)
b'\t2\t7\t41\ttestinputs/multipleWordsAndLines.txt\n'

Test flags after files
>>> subprocess.check_output('python3 wc.py testinputs/multipleWordsAndLines.txt -lw', shell=True)
b'\t2\t7\ttestinputs/multipleWordsAndLines.txt\n'

Test flags between files and on multiple files
>>> subprocess.check_output('python3 wc.py testinputs/mixedEmptyLines.txt -c testinputs/multipleWordsAndLines.txt', shell=True)
b'\t72\ttestinputs/mixedEmptyLines.txt\n\t41\ttestinputs/multipleWordsAndLines.txt\n\t113\ttotal\n'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

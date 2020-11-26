import argparse

def outputBuilder(lines, words, chars, maxLength, lPresent, wPresent, cPresent, LPresent, fileName):
    outputString = "\t"
    if not lPresent and not wPresent and not cPresent and not LPresent:
        outputString += lines + "\t" + words + "\t" + chars + "\t"
    else:
        if lPresent:
            outputString += lines + "\t"
        if wPresent:
            outputString += words + "\t"
        if cPresent:
            outputString += chars + "\t"
        if LPresent:
            outputString += maxLength + "\t"
    output = outputString + fileName
    print(output)
    return output

def processInput():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("filename", type=str, action="append", nargs='*')
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-lines", action="store_true")
    parser.add_argument("-w", action="store_true")
    parser.add_argument("-words", action="store_true")
    parser.add_argument("-c", action="store_true")
    parser.add_argument("-chars", action="store_true")
    parser.add_argument("-L", action="store_true")
    parser.add_argument("--max-line-length", action="store_true")
    parser.add_argument("--files0-from", action="store")
    return parser.parse_known_intermixed_args()

def verifyInputs(knownArgs):
    validInputs = ["--bytes", "-m", "--chars", "--lines", "--words", "--"]
    if knownArgs:
        for i in range(0, len(knownArgs)):
            currentArg = knownArgs[i]
            if currentArg == "--help" or currentArg == "-h":
                printHelp()
                return "help"
            elif currentArg == "--version":
                printVersion()
                return "version"
            elif currentArg in validInputs:
                return notHandled()
            else:
                print("wc: invalid option -- '" + currentArg[1] + "'")
                print("Try 'python3 wc --help' for more information.")
                return "invalid"
    else:
        return True

def processFlags(args):
    return args.l, args.w, args.c, args.L, args.max_line_length

def printHelp():
    print(
'''Usage: python3 wc.py [OPTION]... [FILE]...
or:  python3 wc.py [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the maximum display width
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/wc>
or available locally via: info '(coreutils) wc invocation\'''')

def printVersion():
    print(
'''wc (GNU coreutils) 8.30
Copyright (C) 2018 Free Software Foundation, Inc.
Licence GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Paul Rubin and David MacKenzie.''')

def filesFrom(input):
    try:
        inputFile = open(input).read()
        inputFileSplit = inputFile.split('\0')
        if inputFileSplit[-1] == '':
            inputFileSplit.pop()
        return inputFileSplit
    except FileNotFoundError:
        print('wc: cannot open ' + input + ' for reading: No such file or directory')
        return "error"

def processFiles(args):
    # Process arguments
    lPresent, wPresent, cPresent, LPresent, maxLineLength = processFlags(args)
    maxLineLengthPresent = LPresent or maxLineLength
    # hPresent = hPresent or helpPresent
    filesFromInput = args.files0_from

    fileInputs = args.filename[0]

    if filesFromInput and len(fileInputs) > 0:
        print('wc: extra operand ' + fileInputs[0])
        print('file operands cannot be combined with --files0-from')
        print('Try \'wc --help\' for more information.')
        return "error"
    elif(filesFromInput):
        fileInputs = filesFrom(filesFromInput)
        if(fileInputs == "error"):
            return "error"

    #Init totals
    totalL = 0
    totalW = 0
    totalC = 0
    totalMaxLength = 0

    isDir = False
    notFound = False

    if len(fileInputs) > 0:
        for i in range(0, len(fileInputs)):
            userInput = fileInputs[i]
            if userInput == "-":
                return notHandled()
            try:
                file = open(userInput, mode='r+b')
                fileRead = file.read()
                charCount = len(fileRead)
                wordCount = len(fileRead.split())
                lineCount = len(fileRead.split('\n'.encode())) - 1
                maxLength = len(max(open(userInput, mode='r', encoding="latin1"), key=len)) - 1
                # If the last character is a new line we need to add another line on
                if charCount > 0 and fileRead[-1] == '\n'.encode():
                    lineCount += 1
                outputBuilder(str(lineCount), str(wordCount), str(charCount), str(maxLength), lPresent, wPresent, cPresent, maxLineLengthPresent, userInput)
                totalC += charCount
                totalW += wordCount
                totalL += lineCount
                #update longest line
                if maxLength > totalMaxLength:
                    totalMaxLength = maxLength
                file.close()
            except FileNotFoundError:
                print("wc: " + userInput + ": No such file or directory")
                notFound = True
            except IsADirectoryError:
                print("wc: " + userInput + ": Is a directory")
                outputBuilder("0", "0", "0", "0", lPresent, wPresent, cPresent, maxLineLengthPresent, userInput)
        if len(fileInputs) > 1:
            outputBuilder(str(totalL), str(totalW), str(totalC), str(totalMaxLength), lPresent, wPresent, cPresent, maxLineLengthPresent, "total")
        return totalL, totalW, totalC, isDir, notFound
    else:
        # This would usually allow stdin until ctrl-d is pressed when it will execute with that input
        return notHandled()

def notHandled():
    print("We don't handle that situation yet!")
    return "not handled"

def run(args, knownArgs):
    print(knownArgs)
    verif = verifyInputs(knownArgs)
    if verif and verif != 'invalid' and verif != 'not handled' and verif != 'help' and verif != 'version':
        return processFiles(args)
    else:
        return False

args, knownArgs = processInput()
run(args, knownArgs)
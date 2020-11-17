import sys
import argparse

def outputBuilder(lines, words, chars, lPresent, wPresent, cPresent, fileName):
    outputString = "\t"
    if not lPresent and not wPresent and not cPresent:
        outputString += lines + "\t" + words + "\t" + chars + "\t"
    else:
        if lPresent:
            outputString += lines + "\t"
        if wPresent:
            outputString += words + "\t"
        if cPresent:
            outputString += chars + "\t"
    print(outputString + fileName)

def processInput():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("filename", type=str, action="append", nargs='*')
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-w", action="store_true")
    parser.add_argument("-c", action="store_true")
    return parser.parse_known_intermixed_args()

#"--bytes", "-m", "--chars", "--lines", "-L", "--max-line-length", "--words", "--help", "--version", "--"
# argv =  sys.argv

validInputs = ["--bytes", "-m", "--chars", "--lines", "-L", "--max-line-length", "--words", "--help", "--version", "--"]
args, knownArgs = processInput()
print(knownArgs)
print(args)
if knownArgs:
    for i in range(0, len(knownArgs)):
        currentArg = knownArgs[i]
        if currentArg in validInputs or currentArg[0:13] == "--files0-from":
            print("We don't handle that situation yet!")
            sys.exit()
        else:
            print("wc: invalid option -- '" + currentArg[1] + "'")
            print("Try 'python3 wc --help' for more information.")
            sys.exit()

# argLength = len(argv)
# Process arguments
lPresent = args.l
wPresent = args.w
cPresent = args.c
fileInputs = args.filename


# for i in range(1, argLength):
#     currentArg = argv[i]
#     if currentArg in validInputs or currentArg[0:13] == "--files0-from":
#         print("We don't handle that situation yet!")
#         sys.exit()
#     elif currentArg[0] == '-':
#         for j in range(1, len(currentArg)):
#             currentChar = currentArg[j]
#             if currentChar == 'l':
#                 lPresent = True
#             elif currentChar == 'w':
#                 wPresent = True
#             elif currentChar == 'c':
#                 cPresent = True
#             else:
#                 print("wc: invalid option -- '" + currentChar + "'")
#                 print("Try 'python3 wc --help' for more information.")
#                 sys.exit()
#     else:
#         fileInputs.append(currentArg)

#Init totals
totalL = 0
totalW = 0
totalC = 0

if len(fileInputs) > 0:
    for i in range(0, len(fileInputs)):
        userInput = fileInputs[i]
        if userInput[0:2] == "--":
            if userInput == "--":
                # This would usually allow stdin input until ctrl-d is pressed when it will execute with that input
                print("We don't handle that situation yet!")
            else:
                # As per the error from wc
                print("wc: unrecognised option '" + userInput + "'\nTry 'python3 wc --help' for more information.")
        elif userInput[0] == "-":
            if userInput == "-":
                # This would usually allow stdin until ctrl-d is pressed when it will execute with that input
                print("We don't handle that situation yet!")
            else:
                # As per the error from wc
                print("wc: invalid option -- " + userInput[1] + "'\nTry 'python3 wc --help' for more information.")
        else:
            try:
                file = open(userInput, mode='r+b')
                fileRead = file.read()
                charCount = len(fileRead)
                wordCount = len(fileRead.split())
                lineCount = len(fileRead.split('\n'.encode())) - 1
                # If the last character is a new line we need to add another line on
                if charCount > 0 and fileRead[-1] == '\n'.encode():
                    lineCount += 1
                outputBuilder(str(lineCount), str(wordCount), str(charCount), lPresent, wPresent, cPresent, userInput)
                totalC += charCount
                totalW += wordCount
                totalL += lineCount
                file.close()
            except FileNotFoundError:
                print("wc: " + userInput + ": No such file or directory")
            except IsADirectoryError:
                print("wc: " + userInput + ": Is a directory")
                outputBuilder("0", "0", "0", lPresent, wPresent, cPresent, userInput)
    if len(fileInputs) > 1:
        outputBuilder(str(totalL), str(totalW), str(totalC), lPresent, wPresent, cPresent, "total")
else:
    # This would usually allow stdin until ctrl-d is pressed when it will execute with that input
    print("We don't handle that situation yet!")
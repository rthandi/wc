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
    output = outputString + fileName
    print(output)
    return output

def processInput():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("filename", type=str, action="append", nargs='*')
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-w", action="store_true")
    parser.add_argument("-c", action="store_true")
    return parser.parse_known_intermixed_args()

def verifyInputs(knownArgs):
    validInputs = ["--bytes", "-m", "--chars", "--lines", "-L", "--max-line-length", "--words", "--help", "--version", "--"]
    if knownArgs:
        for i in range(0, len(knownArgs)):
            currentArg = knownArgs[i]
            if currentArg in validInputs or currentArg[0:13] == "--files0-from":
                return notHandled()
            else:
                print("wc: invalid option -- '" + currentArg[1] + "'")
                print("Try 'python3 wc --help' for more information.")
                return "invalid"
    else:
        return True

def processFlags(args):
    return args.l, args.w, args.c

def processFiles(args):
    # Process arguments
    lPresent, wPresent, cPresent = processFlags(args)
    fileInputs = args.filename[0]

    #Init totals
    totalL = 0
    totalW = 0
    totalC = 0

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
                notFound = True
            except IsADirectoryError:
                print("wc: " + userInput + ": Is a directory")
                isDir = True
                outputBuilder("0", "0", "0", lPresent, wPresent, cPresent, userInput)
        if len(fileInputs) > 1:
            outputBuilder(str(totalL), str(totalW), str(totalC), lPresent, wPresent, cPresent, "total")
        return totalL, totalW, totalC, isDir, notFound
    else:
        # This would usually allow stdin until ctrl-d is pressed when it will execute with that input
        return notHandled()

def notHandled():
    print("We don't handle that situation yet!")
    return "not handled"

def run(args, knownArgs):
    verif = verifyInputs(knownArgs)
    if verif and verif != 'invalid' and verif != 'not handled':
        return processFiles(args)
    else:
        return False

args, knownArgs = processInput()
run(args, knownArgs)
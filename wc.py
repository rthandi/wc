import sys

argv =  sys.argv
if len(argv) > 1:
    userInput = argv[1]
    validInputs = ["-c", "--bytes", "-m", "--chars", "-l", "--lines" "-L" "--max-line-length", "-w", "--words",
                   "--help", "--version"]
    if userInput in validInputs or userInput[0:13] == "--files0-from":
        print("We don't handle that situation yet!")
    else:
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
                byteCount = len(fileRead)
                wordCount = len(fileRead.split())
                lineCount = len(fileRead.split('\n'.encode())) - 1
                # If the last character is a new line we need to add another line on
                if byteCount > 0 and fileRead[-1] == '\n'.encode():
                    lineCount += 1
                print(str(lineCount) + "\t" + str(wordCount) + "\t" + str(byteCount) + "\t" + userInput)
                file.close()
            except FileNotFoundError:
                print("wc: " + userInput + ": No such file or directory")
            except IsADirectoryError:
                print("wc: " + userInput + ": Is a directory")
                print("0\t0\t0\t" + userInput)

else:
    # This would usually allow stdin until ctrl-d is pressed when it will execute with that input
    print("We don't handle that situation yet!")
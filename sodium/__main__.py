import sys

if len(sys.argv) < 2:
    print("usage: venv [-hc] COMMAND")
else:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help":
        print("usage: venv [-h] COMMAND\n")
        print("positional arguments:")
        print("    COMMAND         the command to execute")
        print("\noptions:")
        print("    -h, --help      show this help message and exit")
        print("    -c, --commands  shows a list of available commands")
    if sys.argv[1] == "-c" or sys.argv[1] == "--commands":
        print("commands:")
        print("    theme           prints the default theme out")
        print("    help            shows the help message")
    if sys.argv[1] == "theme":
        print("Theme:")
        with open("sodium/themes/dark_blue.json", encoding="utf-8") as file:
            for line in file.readlines():
                sys.stdout.write(line)
        file.close()
        print()

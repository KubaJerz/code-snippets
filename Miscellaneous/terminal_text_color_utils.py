"""
Color Codes:

    \033[30m: Black
    \033[31m: Red
    \033[32m: Green
    \033[33m: Yellow
    \033[34m: Blue
    \033[35m: Magenta
    \033[36m: Cyan
    \033[37m: White (or Light Gray)
    \033[90m: Dark Gray 

Reset Code: \033[0m resets all formatting to default.

"""


RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

print(f"{RED}This text is red.{RESET}")
print(f"{GREEN}This text is green.{RESET}")
print("This text is back to default color.")

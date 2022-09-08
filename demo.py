from datetime import datetime
import sys
from src.passwordgenerator import DatesGenerator
from src.pdfbruteforcer import PdfBruteForcer
from datetime import datetime

generator = DatesGenerator(datetime(1990, 1, 1),datetime(2020, 1, 1), "%d%m%Y")

# set default name for file
filename = "password-protected-document.pdf"
if len(sys.argv) > 1:
    filename = sys.argv[1]

bruteforcer = PdfBruteForcer("password-protected-document.pdf", generator)
print("starting bruteforce attack...")
password = bruteforcer.bruteforce()

if password == None:
    print("did not find the password")
else:
    print("password is: " + password)
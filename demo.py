from datetime import datetime
from src.passwordgenerator import DatesGenerator
from src.pdfbruteforcer import PdfBruteForcer
from datetime import datetime

generator = DatesGenerator(datetime(1980, 1, 1),datetime(2020, 1, 1), "%d%m%Y")
bruteforcer = PdfBruteForcer("demopath", generator)
password = bruteforcer.bruteforce()
print("Found the password: " + password)
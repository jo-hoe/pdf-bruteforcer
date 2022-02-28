import pikepdf

from src.passwordgenerator import PasswordGenerator

class PdfBruteForcer():

    def __init__(self, pdfFilePath: str, generator: PasswordGenerator):
        self.generator = generator
        self.pdfFilePath = pdfFilePath

    def bruteforce(self)-> str:
        for password in self.generator.get_next_password():
            try:
                # open PDF file
                with pikepdf.open(self.pdfFilePath, password=password) as pdf:
                    # Password decrypted successfully, break out of the loop
                    return password
                    break
            except pikepdf._qpdf.PasswordError as e:
                # wrong password, just continue in the loop
                continue

        return None
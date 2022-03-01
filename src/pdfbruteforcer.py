import pikepdf

from src.passwordgenerator import PasswordGenerator

class PdfBruteForcer():

    def __init__(self, pdfFilePath: str, generator: PasswordGenerator):
        self.generator = generator
        self.pdfFilePath = pdfFilePath

    def bruteforce(self)-> str:
        for password in self.generator.get_next_password():
            try:
                with pikepdf.open(self.pdfFilePath, password=password) as pdf:
                    # password found, return it
                    return password
            except pikepdf._qpdf.PasswordError as ex:
                # password incorrect, test next one
                continue
        # no password found, return None
        return None

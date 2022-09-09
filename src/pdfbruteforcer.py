import pikepdf
from tqdm import tqdm

from src.passwordgenerator import PasswordGenerator

class PdfBruteForcer():

    def __init__(self, pdfFilePath: str, generator: PasswordGenerator):
        self.generator = generator
        self.pdfFilePath = pdfFilePath

    def bruteforce(self)-> str:
        progess_bar = tqdm(total=self.generator.get_password_count())
        for password in self.generator.get_next_password():
            try:
                with pikepdf.open(self.pdfFilePath, password=password) as pdf:
                    # password found, return it
                    return password
            except pikepdf._qpdf.PasswordError as ex:
                # password incorrect, test next one
                continue
            finally:
                progess_bar.update(1)
        
        # no password found, return None
        progess_bar.close()
        return None

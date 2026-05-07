class EmptyFileError(Exception):
    def __init__(self, *args):
        # self.message = "Podany plik jest pusty."
        super().__init__(*args)

class TextAnalyzer():
    def __init__(self):
        self.slowa = {}


    def load_file(self, sciezka):
        try:
            file = open(sciezka, 'r')
            self.dane = file
            if not file.read():
                raise EmptyFileError('halo pusto')
            file.seek(0)
            for line in self.dane:
                words = line.split()
                print(words)
                words1 = [x.lower() for x in words]
                for slowo in words1:
                    try: 
                        self.slowa[slowo] += 1
                    except KeyError:
                        self.slowa[slowo] = 1
                        
            
        except FileNotFoundError as e:
            print(f'Brak pliku o podanej ścieżce: {e}.')

        finally:
            file.close()

    def get_word_count(self, szukane):
        try:
            print(f'występuje {self.slowa[szukane]} razy')
        except KeyError:
            print('nie wustepuje')

spr = TextAnalyzer()
spr.load_file('/dmj/2025/ag479781/Pobrane/tadeusz.txt')
print(spr.get_word_count('i'))






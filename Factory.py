class Document:
    def create(self):
        raise NotImplementedError("Metoda create() musi byt predpisane.")


class PDFDocument(Document):
    def create(self):
        return "Vytvaram PDF Document."


class WordDocument(Document):
    def create(self):
        return "Vytvaram Word Document."


class TXTDocument(Document):
    def create(self):
        return "Vytvaram txt Document."


class Factory:
    def create_document(self, type):
        if type == 'pdf':
            return PDFDocument()
        elif type == 'word':
            return WordDocument()
        elif type == 'txt':
            return TXTDocument()
        else:
            raise ValueError("Neznamy typ document")

factory = Factory()
pdf = factory.create_document("pdf")
print(pdf.create())
word = factory.create_document("word")
print(word.create())
txt = factory.create_document("txt")
print(txt.create())



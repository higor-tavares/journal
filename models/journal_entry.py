from time import localtime, strftime

class JournalEntryEntity(): 

    def __init__(self, id, description, amount, type):
        self.id = id
        self.description = description
        self.amount = amount
        self.type = type
        self.entryDate = strftime('%d/%m/%Y %H:%M:%S', localtime())
    
    def get_journal_entry(self):
        return {
            'id':self.id,
            'description':self.description,
            'amount':self.amount,
            'type':self.type,
            'entryDate': self.entryDate
        }
    
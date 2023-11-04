from time import localtime, strftime

class JournalEntryEntity(): 

    def __init__(self, id, username, description, amount, type):
        self.username = username
        self.id = id
        self.description = description
        self.amount = amount
        self.type = type
        self.entryDate = strftime('%d/%m/%Y %H:%M:%S', localtime())
    
    def get_journal_entry(self):
        return {
            'id':self.id,
            'username':self.username,
            'description':self.description,
            'amount':self.amount,
            'type':self.type,
            'entryDate': self.entryDate
        }
    
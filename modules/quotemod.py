"""Handles a quote database
@package ppbot

@syntax quote <add/del/search> <nick/quote>
"""
from modules import *

#id = Column(Integer, primary_key=True)
#quote = Column(Text, nullable=False)
#added_by = Column(String(250), nullable=False)
#source = Column(String(250), nullable=False)
#time = Column(DateTime, default=func.now())
#nickname = Column(String(250), nullable=True)

class Quotemod(Module):

    def __init__(self, *args, **kwargs):
        """Constructor"""

        Module.__init__(self, kwargs=kwargs)

    def _register_events(self):
        self.add_command('quote', 'subcommand')

    def subcommand(self, event):
        """ temporary, will refactor into Module later on. """

        try:
            getattr(self, event['args'][0])(event)
        except:
            import traceback
            traceback.print_exc()

    def add(self, event):
        """Adds a new quote."""

        data = {'quote': ' '.join(event['args'][1:]),
                'added_by': event['source'],
                'time': datetime.now(),
                'source': event['target']}
        self.db.quotes.insert(data)

        self.msg(event['target'], 'Quote added.')

    def delete(self, event):
        """Deletes a quote by id."""

        self.db.quotes.remove({'_id': event['args'][0]})
        self.msg(event['target'], 'Quote deleted.')

    def search(self, event):
        #quotes = Quote().find(' '.join(event['args'][1:-1]))
        print quotes
        print quotes.count()

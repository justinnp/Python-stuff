#!/usr/bin/env python3
import datetime
from collections import OrderedDict
import sys
from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

def initialize():
    """Create Database and table if dne"""
    db.connect()
    db.create_tables([Entry], safe=True)

    ## to check entries
    # in terminal
    # sqlite3 diary.db
    # .tables  shows table
    # select * from entry
def menu_loop():
    """Show menu"""
    choice = None
    while choice != 'q':
        print("Enter 'q' to quit")
        for key, value in menu.items():
            if key != 'd':
                print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        if choice in menu:
            menu[choice]()

def add_entry():
    """Add entry"""
    print('Enter your entry. Press ctrl+D when finished.')
    data = sys.stdin.read().strip()
    if data:
        if input('Save entry? [y/n] ').lower() != 'n':
            Entry.create(content=data)
            print('Saved successfully.')


def view_entries(search_query=None):
    """View previous entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print('\n\n' + '=' *len(timestamp))
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')
        next_action = input('Action [n/d/q] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

def search_entries():
    """Search for an entry"""
    view_entries(input('Search query: '))

def delete_entry(entry):
    """Delete an entry"""
    if input('Are you sure? [y/n] ').lower() == 'y':
        entry.delete_instance()

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
    ('d', delete_entry),
])

if __name__ == '__main__':
    initialize()
    menu_loop()
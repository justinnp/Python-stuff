# CharDeeMacDennis

from peewee import *

db = SqliteDatabase('members.db')

class Member(Model):
    name = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)
    class Meta:
        database = db

members = [
    {'name': 'charlie',
     'points': 4888},
    {'name': 'mac',
     'points': 11912},
    {'name': 'dennis',
     'points': 7362},
    {'name': 'dee',
     'points': 4879},
    {'name': 'frank',
     'points': 14717}
]

def add_member():
    for member in members:
        try:
            Member.create(name=member['name'], points=member['points'])
        except IntegrityError:
            member_record = Member.get(name=member['name'])
            member_record.points = member['points']
            member_record.save()

def top_score():
    member = Member.select().order_by(Member.points.desc()).get()
    return member


if __name__ == '__main__':
    db.connect()
    db.create_tables([Member], safe=True)
    add_member()
    print('Top score: {0.name}'.format(top_score()))
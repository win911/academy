#import sqlalchemy
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import sessionmaker
#Base = declarative_base()

from app import app, db
import hashlib


class User(db.Model):
    __tablename__ = 'user'
 
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String)
    password = db.Column(db.String)
 
    def __init__(self, account, password):
        self.account = account
        self.password = hashlib.sha1(password).hexdigest()
 
    def __repr__(self):
       return "User('%s', '%s')" % \
           (self.account, self.password)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


'''
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
 
    Session = sessionmaker(bind=engine)
    session = Session()
 
    #create
    session.add_all([
    	User("ed_user", "edpasswd"),
    	User("u1_user", "u1passwd"),
    	User("u2_user", "u2passwd")])
    sel_user = session.query(User).filter(User.account == 'ed_user').first()
    print sel_user
    #update
    sel_user.account = "Andy Jones"
    print sel_user
    #delete
    session.delete(sel_user)
    #read
    for row in session.query(User).order_by(User.id):
    	print row
    session.add(User("u3_user", "u3passwd"))
    #read
    for row in session.query(User).order_by(User.id):
    	print row
	
    session.commit()
'''
    
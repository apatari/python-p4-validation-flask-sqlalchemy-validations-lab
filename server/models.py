from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

   
    @validates('name')
    def validate_name(self, key, nam):
        if nam == "":
            raise ValueError("Name cannot be blank")
        return nam

    @validates('phone_number')
    def validate_phone_number(self, key, num):
        if len(num) != 10:
            raise ValueError("Phone number must be 10 digits")
        return num
        

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, val):
        if len(val) < 250:
            raise ValueError("Must be at least 250 characters")
        return val
    
    @validates('summary')
    def validate_summary(self, key, val):
        if len(val) > 249:
            raise ValueError("Cannot be longet than 250 characters")
        return val

    @validates('category')
    def validate_cat(self, key, val):
        if val not in {'Fiction', 'Non-Fiction'}:
            raise ValueError("Not a valid category")
        return val
    
    @validates('title')
    def validate_title(self, key, val):
        must_haves = {
            "Wont't Believe",
            "Secret",
            "Top",
            "Guess"
        }
        valid = False
        for item in must_haves:
            if item in val:
                valid = True
        if not valid:
            raise ValueError("Title doesn't contain clickbaity phrase")
        return val

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

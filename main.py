
from sqlalchemy import create_engine
from config import DATABASE_URI
import datetime
from sqlalchemy.orm import sessionmaker

from models import Base, Book
engine = create_engine(DATABASE_URI)

# Base.metadata.create_all(engine) #Создаем модели
# Base.metadata.drop_all(engine) #удаляем все модели в БД


Session = sessionmaker(bind=engine)
s = Session()

# book = Book(
#     title='Deep Learning',
#     author='Ian Goodfellow',
#     pages=775,
#     published='2016, 11, 18'
# )
#
#
# s.add(book)
# s.commit()

print(s.query(Book).first())



s.close()
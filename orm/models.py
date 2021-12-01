from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine('sqlite:///testdb.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# 엔티티(테이블) 생성
Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    passwd = Column(String)

Base.metadata.create_all(engine)
print(Base.metadata.tables)

member1 = Member(name="kims", passwd="1001")
session.add(member1)
session.commit()
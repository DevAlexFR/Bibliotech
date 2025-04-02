import datetime
import subprocess
import time
import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base



Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    due_date = Column(DateTime)

# Só inicia o proxy se não estiver no Fly.io

engine = None
Session = None
session = None
Base = declarative_base()

if os.getenv('BUILDING') != 'true':
    # Configurações locais
    if not os.getenv('FLY_APP_NAME'):
        try:
            proxy_command = ["flyctl", "proxy", "13306:3306", "-a", "bibliotech"]
            proxy_process = subprocess.Popen(
                proxy_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            time.sleep(5)
        except FileNotFoundError:
            print("Aviso: flyctl não encontrado, usando configuração local direta")

    # Configuração dinâmica do banco
    DATABASE_URL = os.getenv('DATABASE_URL', 
        "mysql+pymysql://non_root_user:1234@127.0.0.1:13306/some_db" if not os.getenv('FLY_APP_NAME') 
        else "mysql+pymysql://non_root_user:1234@bibliotech.internal:3306/some_db"
    )

    engine = create_engine(DATABASE_URL, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Cria tabelas apenas se explicitamente solicitado
    if os.getenv('INIT_DB') == 'true':
        Base.metadata.create_all(engine)

def add_loan(loan_data):
    new_loan = Loan(title=loan_data["title"], due_date=loan_data["due_date"])
    session.add(new_loan)
    session.commit()


def get_loans():
    loans = session.query(Loan).all()
    result = []
    for l in loans:
        result.append({
            "id": l.id,
            "title": l.title,
            "due_date": l.due_date.isoformat() if l.due_date else None
        })
    return result


def update_loan(loan_data):
    loan = session.query(Loan).filter(Loan.id == loan_data["id"]).first()
    if loan:
        loan.due_date = loan_data["due_date"]
        session.commit()


def delete_loan_by_title(title):
    session.query(Loan).filter(Loan.title == title).delete()
    session.commit()


if __name__ == "__main__":

    from sqlalchemy import create_engine

    DATABASE_URL = "mysql+pymysql://non_root_user:1234@127.0.0.1:13306/some_db"


    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            print("✅ Conexão bem-sucedida!")
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")

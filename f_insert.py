from sqlalchemy import create_engine, URL, insert, MetaData
import credenziali

url_object = URL.create(
    "mysql",
    username=credenziali.user,
    password=credenziali.pw,
    host=credenziali.hostname,
    database=credenziali.database
)

engine = create_engine(url_object)
meta = MetaData()
meta.reflect(bind=engine)

def insertData(dictList, tableName):
    with engine.connect() as conn:
        conn.execute(insert(meta.tables[tableName]), dictList)
        conn.commit()
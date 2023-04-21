from sqlalchemy import create_engine, URL, insert, MetaData

url_object = URL.create(
    "mysql",
    username="root",
    password="",
    host="localhost",
    database="libreria"
)

engine = create_engine(url_object)
meta = MetaData()
meta.reflect(bind=engine)

def insertData(dictList, tableName):
    with engine.connect() as conn:
        conn.execute(insert(meta.tables[tableName]), dictList)
        conn.commit()
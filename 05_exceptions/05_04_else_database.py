# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.
import sqlalchemy
from sqlalchemy.exc import OperationalError

try:
    engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
    print(actor.columns.keys())
except:
    print('Not connecting')
else:
    print('Yee haaw')


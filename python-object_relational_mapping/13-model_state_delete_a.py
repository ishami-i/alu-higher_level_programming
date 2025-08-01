#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

It connects to a MySQL server running on localhost at port 3306.
The script takes three command-line arguments: mysql username,
mysql password, and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql_username> \
<mysql_password> <database_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306

    # Create the SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:{port}/{database}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session_class = sessionmaker(bind=engine)

    # Create a Session
    with Session_class() as session:
        # Query and delete all State objects where the name contains the letter 'a'
        # The filter(State.name.like("%a%")) finds names with 'a' anywhere in them.
        # The synchronize_session=False parameter is used for more efficient
        # bulk deletion without loading all objects into memory first.
        try:
            num_deleted = session.query(State).filter(
                State.name.like("%a%")
            ).delete(synchronize_session=False)

            # Commit the changes to the database
            session.commit()
            print(f"Deleted {num_deleted} state(s) with 'a' in their name.")
        except Exception as e:
            # Handle potential errors during the database operation
            session.rollback()
            print(f"An error occurred: {e}")

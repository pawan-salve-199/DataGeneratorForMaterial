import pyodbc

class PyodbcSetup:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = None
        self.cursor = None


    def disconnect_from_database(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def connect_to_database(self):
        try:
            self.conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes')
            self.cursor = self.conn.cursor()
            return self.cursor
        except Exception as e:
            print(f"Database connection error: {str(e)}")


    def insert_data(self,data,query):
        # Define SQL queries
        try:
            # Insert data using executemany
            self.cursor.execute(query,data)
            table_name=query.split(" ")[2]
            print(f"data inserted into {table_name}")
        except Exception as e:
            print(f"An error occurred while inserting data: {str(e)}")
    
    
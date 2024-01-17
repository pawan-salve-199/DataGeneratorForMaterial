# Function to generate random phone numbers
from faker import Faker
import random
from datetime import datetime, timedelta

fake=Faker()

def random_phone_number():
    return fake.phone_number()

# Function to generate random email addresses
def random_email():
    return fake.email()

# Function to generate random decimal values
def random_decimal():
    return round(random.uniform(1, 1000), 2)


# Function to generate a random start date within the last decade
def random_start_date():
    start_date = datetime.now() - timedelta(days=random.randint(1, 3650))
    return start_date.strftime('%Y-%m-%d')


# Function to generate a random end date within the next decade
def random_end_date():
    end_date = datetime.now() + timedelta(days=random.randint(1, 3650))
    return end_date.strftime('%Y-%m-%d')




def check_zero(cursor,query):
    res=cursor.execute(query).fetchone()[0]
    res = res if not res is None else 0
    return res


def generate_query_insert(table_name,data,cursor):
    # Define a dictionary to map table names to their respective data
        tables_data = {
            'Suppliers': ('SupplierName', 'ContactPerson', 'Phone', 'Email'),
            'Materials': ('MaterialName','description', 'UnitPrice', 'Unit','Categoryid'),
            'Cities': ('CityName', 'Country'),
            'SupplierMaterials': ('SupplierID', 'MaterialID'),
            'Customers': ('CustomerName', 'ContactPerson', 'Phone', 'Email', 'CityID'),
            'Orders': ('CustomerID', 'MaterialID', 'Quantity', 'OrderDate'),
            'Projects': ('ProjectName', 'StartDate', 'EndDate', 'CityID'),
            'ProjectMaterials': ('ProjectID', 'MaterialID', 'Quantity'),
            'MaterialCategories': ('CategoryName',),
            'MaterialCategoryMapping': ('MaterialID', 'CategoryID'),
            'SupplierCertifications': ('CertificationName',),
            'SupplierCertificationMapping': ('SupplierID', 'CertificationID'),
            'Inventory':('MaterialID','Quantity'),
            'Transactions': ('SupplierID', 'MaterialID', 'CityID', 'Quantity', 'TransactionDate')
        }

        # Iterate over the tables_data dictionary to create SQL insert statements
        for table, columns in tables_data.items():
            if table==table_name:
          
                placeholders = ', '.join('?' for _ in columns[0:])
                sql_query = f"INSERT INTO {table} ({', '.join(columns[0:])}) VALUES ({placeholders})"
                print('inserting...')
                cursor.executemany(sql_query,data)
                cursor.commit()
                print(f"{len(data)} rows inserted into {table_name}")
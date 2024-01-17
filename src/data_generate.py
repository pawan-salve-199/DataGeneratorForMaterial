from faker import Faker
import random
from datetime import datetime, timedelta
from time import sleep
from dataset_final import material_dataset
from utils import *

fake = Faker()

# Generate random start and end dates
start_date = random_start_date()
end_date = random_end_date()


class RetailDataGenerator:
        def __init__(self):
            self.cursor = None
            self.fake = Faker()
            self.Suppliers = []
            self.Orders =[]
            self.Materials =[]
            self.Cities =[]
            self.Customers =[]
            self.SupplierMaterials = []
            self.Projects =[]
            self.ProjectMaterials =[]
            self.MaterialCategories =[]
            self.SupplierCertifications =[]
            self.SupplierCertificationMapping =[]
            self.Transactions =[]
            self.Inventory =[]


        def generate_suppliers(self,num_suppliers):
            for i in range(1,num_suppliers+1):
                self.Suppliers.append((fake.name(),
                                        fake.company(),
                                        random_phone_number(),
                                        fake.email()
                                    ))
            return self.Suppliers
        

        def generate_materials_with_categories(self,material_category_dataset):
            for i in material_category_dataset:
                category_info = i['CategoryName']
                for material in i['MaterialNames']:
                    self.Materials.append((material['MaterialName'],
                                           fake.text(), 
                                           material['unitprice'],
                                           material['unit'],
                                           category_info))

            return self.Materials




        def generate_cities(self,num_cities):
            for i in range(1, num_cities + 1):
                self.Cities.append((
                                        fake.city(),
                                        fake.country()
                                    ))
            return self.Cities



        # Function to generate data for the SupplierMaterials table
        def generate_supplier_materials(self,num_supplier_materials, max_supplier_id, max_material_id):
            for i in range(1, num_supplier_materials+400):
                self.SupplierMaterials.append(
                                            (
                            random.randint(1, max_supplier_id),
                            random.randint(1, max_material_id)
                        ))
            return self.SupplierMaterials



        # Function to generate data for the Customers table
        def generate_customers(self,num_customers, max_city_id):
            for i in range(1, num_customers + 1):
                self.Customers.append((
                                        fake.name(),         # CustomerName
                                        fake.company(),         # ContactPerson
                                        random_phone_number(),
                                        random_email(),
                                        random.randint(1, max_city_id)  # CityID
                                    ))
            return self.Customers




        # Function to generate data for the Orders table
        def generate_orders(self,num_orders, max_customer_id, max_material_id):

            for i in range(1, num_orders + 1):
                self.Orders.append((
                                    random.randint(1, max_customer_id),        # CustomerID
                                    random.randint(1, max_material_id),        # MaterialID
                                    random.randint(1, 100),                     # Quantity
                                    fake.date_time_this_decade()
                 
                                ))
            return self.Orders




        # Function to generate data for the Projects table
        def generate_projects(self,num_projects, max_city_id):
            for i in range(1, num_projects + 1):
                self.Projects.append((
                                        fake.word(),                 # ProjectName
                                        start_date,     # StartDate
                                        end_date,     # EndDate
                                        random.randint(1, max_city_id)  # CityID
                                    ))
            return self.Projects



        # Function to generate data for the ProjectMaterials table
        def generate_project_materials(self,num_project_materials,max_project_id, max_material_id):
            for i in range(1, num_project_materials + 1):
                self.ProjectMaterials.append((
                                                random.randint(1, max_project_id),     # ProjectID
                                                random.randint(1, max_material_id),    # MaterialID
                                                random.randint(1, 100)                  # Quantity
                                            ))
            return self.ProjectMaterials




        # Function to generate data for the MaterialCategories table
        def generate_material_categories(self,material_dataset):
            for i in material_dataset:
                self.MaterialCategories.append([i['CategoryName']])
            return self.MaterialCategories



        # Function to generate data for the SupplierCertifications table
        def generate_supplier_certifications(self,num_supplier_certifications):
            for i in range(1, num_supplier_certifications + 1):
                self.SupplierCertifications.append([fake.word()])
            return self.SupplierCertifications



        # Function to generate data for the SupplierCertificationMapping table
        def generate_supplier_certification_mapping(self,num_supplier_certification_mapping, max_supplier_id, max_supplier_certification_id):
            for i in range(1, num_supplier_certification_mapping + 1):
                self.SupplierCertificationMapping.append((random.randint(1, max_supplier_id),random.randint(1, max_supplier_certification_id)
                                                            ))
            return self.SupplierCertificationMapping



        # Function to generate data for the Transactions table
        def generate_transactions(self,num_transactions, max_supplier_id, max_material_id, max_city_id):
            for i in range(1, num_transactions + 1):
                self.Transactions.append( (
                                                random.randint(1, max_supplier_id),      # SupplierID
                                                random.randint(1, max_material_id),      # MaterialID
                                                random.randint(1, max_city_id),          # CityID
                                                random.randint(1, 100),                  # Quantity
                                                fake.date_time_this_decade()
       
                                            ))
            return self.Transactions
        

        
        def generate_inventory_data(self,max_material_id):
            for i in range(1, max_material_id + 1):
                self.Inventory.append((random.randint(1,max_material_id),random.randint(1, 100)
                                       ))
            return self.Inventory













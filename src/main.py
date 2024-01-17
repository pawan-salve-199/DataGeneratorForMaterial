from data_generate import *  
from pyodbc_setup import *  
import sys
from data_generate import * 
from utils import *
import json


def main(num_records=None):
    server = 'DESKTOP-LUKC2EF\\SQLEXPRESS'
    database = 'ConstructionMaterialProject'
    num_records = num_records

    pyodbcobj=PyodbcSetup(server,database)
    cursor=pyodbcobj.connect_to_database()


    # # Generate data for each table
    obj=RetailDataGenerator()

    # suppliers_data = obj.generate_suppliers(num_suppliers)
    # generate_query_insert("Suppliers",suppliers_data,cursor)
    max_supplier_id = check_zero(cursor,"SELECT MAX(SupplierID) FROM Suppliers")

    # supplier_certifications_data = obj.generate_supplier_certifications(num_supplier_certifications)
    # generate_query_insert(table_name='SupplierCertifications',data=supplier_certifications_data,cursor=cursor)
    max_supplier_certificate_id = check_zero(cursor,"SELECT MAX(CertificationID) FROM SupplierCertifications")

    # materials_data = obj.generate_materials_with_categories(material_dataset)
    # generate_query_insert("Materials",materials_data,cursor)
    max_material_id = check_zero(cursor,"SELECT MAX(MaterialId) FROM materials")

    # material_categories_data = obj.generate_material_categories(material_dataset)
    # generate_query_insert("MaterialCategories",material_categories_data,cursor)
 
    cities_data = obj.generate_cities(num_cities)
    max_city_id = check_zero(cursor,"SELECT MAX(CityID) FROM Cities")
    generate_query_insert("Cities",cities_data,cursor)

    # supplier_materials_data = obj.generate_supplier_materials(max_material_id, max_supplier_id, max_material_id)
    # generate_query_insert("SupplierMaterials",supplier_materials_data,cursor)


    # supplier_certification_mapping_data = obj.generate_supplier_certification_mapping(num_supplier_certification_mapping, max_supplier_id, max_supplier_certificate_id)
    # generate_query_insert("SupplierCertificationMapping",supplier_certification_mapping_data,cursor)
    
    
    # inventory_data=obj.generate_inventory_data(max_material_id)
    # generate_query_insert("Inventory",inventory_data,cursor)

 
    customers_data = obj.generate_customers(num_customers, max_city_id)
    generate_query_insert("Customers",customers_data,cursor)
    max_customer_id = check_zero(cursor,"SELECT MAX(CustomerID) FROM customers")

    orders_data = obj.generate_orders(num_orders, max_customer_id, max_material_id)
    generate_query_insert("Orders",orders_data,cursor)

    projects_data = obj.generate_projects(num_projects, max_city_id)
    generate_query_insert("Projects",projects_data,cursor)
    max_project_id=check_zero(cursor,"SELECT MAX(ProjectID) FROM Projects")

    project_materials_data = obj.generate_project_materials(num_project_materials, max_project_id, max_material_id)
    generate_query_insert("ProjectMaterials",project_materials_data,cursor)

    transactions_data = obj.generate_transactions(num_transactions, max_supplier_id, max_material_id, max_city_id)
    generate_query_insert("Transactions",transactions_data,cursor)

    cursor.close()

if __name__=="__main__":
    num_suppliers = 1000
    num_supplier_certifications = 300
    num_supplier_certification_mapping = num_suppliers

    num_cities = 50
    num_customers = 10000
    num_orders = 100000
    num_projects = 100
    num_project_materials = 80
    num_transactions = 70000
    
    for i in range(1,9):
        main()


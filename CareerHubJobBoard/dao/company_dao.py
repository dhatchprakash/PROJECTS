import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from util.db_conn_util import get_db_connection
from entity.company import Company

class CompanyDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert_company(self, company):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Companies (CompanyName, Location)
                VALUES (?, ?)
            """, company.company_name, company.location)
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting company: {str(e)}")

    
    def get_company_by_id(self, company_id):
        cursor = self.conn.cursor()
        
        query = "SELECT CompanyID, CompanyName, Location FROM Companies WHERE CompanyID = ?"
        cursor.execute(query, (company_id,))
        result = cursor.fetchone()

        if result:
            return Company(result[0], result[1], result[2])  
        return None
    
    def get_all_companies(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Companies")  # Assuming your companies table is named 'Companies'
            rows = cursor.fetchall()
            companies = []

            for row in rows:
                company = Company(
                    company_id=row[0],
                    company_name=row[1],
                    location=row[2]
                )
                companies.append(company)

            return companies
        except Exception as e:
            print(f"Error retrieving all companies: {e}")
            raise
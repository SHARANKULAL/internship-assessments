import pandas as pd
import os

OUT_SQL = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\mysql_raw_data_insert.txt'
RAW_DIR = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\dataset\raw'

tables = ['learners', 'courses', 'assessments', 'course_enrollments', 'transactions', 'academic_calendar']

sql_script = '-- =========================================================================\n'
sql_script += '-- MySQL Script to Create Database, Tables (with Primary Keys) and Insert Raw DQA Data\n'
sql_script += '-- =========================================================================\n\n'

sql_script += 'CREATE DATABASE IF NOT EXISTS `edtech_dqa`;\n'
sql_script += 'USE `edtech_dqa`;\n\n'

for table_name in tables:
    csv_file = os.path.join(RAW_DIR, f'{table_name}.csv')
    if not os.path.exists(csv_file):
        print(f'Warning: {csv_file} not found.')
        continue
    
    df = pd.read_csv(csv_file)
    # Fill NaN with 'NULL_VAL' string to distinguish from actual text
    df = df.fillna('NULL_VAL')
    
    # Create Table Statement (with Primary Key inferred from column name)
    cols = []
    for col in df.columns:
        if col.endswith('_id') and col.split('_')[0] in table_name or col == 'calendar_id':
             cols.append(f'`{col}` VARCHAR(255) PRIMARY KEY')
        else:
             cols.append(f'`{col}` VARCHAR(255)')
    
    sql_script += f'DROP TABLE IF EXISTS `{table_name}`;\n'
    sql_script += f'CREATE TABLE `{table_name}` (\n    ' + ',\n    '.join(cols) + '\n);\n\n'
    
    # Insert Statements
    sql_script += f'-- Inserting data into {table_name}\n'
    
    for _, row in df.iterrows():
        vals = []
        for val in row:
            if val == 'NULL_VAL':
                vals.append('NULL')
            else:
                val_str = str(val).replace("'", "''") # escape single quotes for SQL
                vals.append(f"'{val_str}'")
        
        sql_script += f'INSERT IGNORE INTO `{table_name}` VALUES (' + ', '.join(vals) + ');\n'
    
    sql_script += '\n'

with open(OUT_SQL, 'w', encoding='utf-8') as f:
    f.write(sql_script)

print('MySQL script successfully generated at:', OUT_SQL)

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
    
    # Create Table Statement
    cols = []
    has_pk = False
    pk_col = ''
    for col in df.columns:
        if (col.endswith('_id') and col.split('_')[0] in table_name) or col == 'calendar_id':
             cols.append(f'  `{col}` VARCHAR(255) NOT NULL')
             pk_col = col
             has_pk = True
        else:
             cols.append(f'  `{col}` VARCHAR(255)')
             
    if has_pk:
        cols.append(f'  PRIMARY KEY (`{pk_col}`)')
    
    sql_script += f'DROP TABLE IF EXISTS `{table_name}`;\n'
    sql_script += f'CREATE TABLE `{table_name}` (\n' + ',\n'.join(cols) + '\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n'
    
    # Insert Statements (Batch Inserts for proper MySQL format)
    sql_script += f'-- Inserting data into `{table_name}`\n'
    
    insert_header = f'INSERT IGNORE INTO `{table_name}` (' + ', '.join([f'`{c}`' for c in df.columns]) + ') VALUES\n'
    sql_script += insert_header
    
    values_list = []
    for _, row in df.iterrows():
        vals = []
        for val in row:
            if val == 'NULL_VAL':
                vals.append('NULL')
            else:
                val_str = str(val).replace("'", "''") # escape single quotes for SQL
                vals.append(f"'{val_str}'")
        values_list.append('(' + ', '.join(vals) + ')')
        
    sql_script += ',\n'.join(values_list) + ';\n\n'

with open(OUT_SQL, 'w', encoding='utf-8') as f:
    f.write(sql_script)

print('Proper MySQL script successfully generated at:', OUT_SQL)

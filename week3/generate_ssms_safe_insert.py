import pandas as pd
import os

OUT_SQL = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\ssms_raw_data_insert.sql'
RAW_DIR = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\dataset\raw'

tables = ['learners', 'courses', 'assessments', 'course_enrollments', 'transactions', 'academic_calendar']

sql_script = '-- =========================================================================\n'
sql_script += '-- SSMS T-SQL Script to Create Database, Tables with PRIMARY KEYs and Insert Raw DQA Data\n'
sql_script += '-- =========================================================================\n\n'

sql_script += 'IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = \'edtech_dqa\')\n'
sql_script += 'BEGIN\n'
sql_script += '    CREATE DATABASE [edtech_dqa];\n'
sql_script += 'END\n'
sql_script += 'GO\n\n'
sql_script += 'USE [edtech_dqa];\nGO\n\n'

for table_name in tables:
    csv_file = os.path.join(RAW_DIR, f'{table_name}.csv')
    if not os.path.exists(csv_file):
        print(f'Warning: {csv_file} not found.')
        continue
    
    df = pd.read_csv(csv_file)
    # Fill NaN with 'NULL_VAL' string to distinguish from actual text
    df = df.fillna('NULL_VAL')
    
    # Create Table Statement with Primary Key Inference
    cols = []
    has_pk = False
    pk_col = ''
    
    for col in df.columns:
        if (col.endswith('_id') and col.split('_')[0] in table_name) or col == 'calendar_id':
             cols.append(f'    [{col}] VARCHAR(255) NOT NULL PRIMARY KEY')
             pk_col = col
             has_pk = True
        else:
             cols.append(f'    [{col}] VARCHAR(MAX)')
    
    sql_script += f'IF OBJECT_ID(\'{table_name}\', \'U\') IS NOT NULL DROP TABLE [{table_name}];\n'
    sql_script += f'CREATE TABLE [{table_name}] (\n' + ',\n'.join(cols) + '\n);\nGO\n\n'
    
    # Insert Statements
    sql_script += f'-- Inserting data into {table_name}\n'
    
    for _, row in df.iterrows():
        vals = []
        for val in row:
            if val == 'NULL_VAL':
                vals.append('NULL')
            else:
                val_str = str(val).replace("'", "''") # escape single quotes
                vals.append(f"'{val_str}'")
        
        # We need to handle duplicates in SSMS since it lacks INSERT IGNORE
        if has_pk:
            pk_val = str(row[pk_col]).replace("'", "''")
            sql_script += f"IF NOT EXISTS (SELECT 1 FROM [{table_name}] WHERE [{pk_col}] = '{pk_val}')\n"
            sql_script += f"    INSERT INTO [{table_name}] VALUES (" + ', '.join(vals) + ');\n'
        else:
             sql_script += f'INSERT INTO [{table_name}] VALUES (' + ', '.join(vals) + ');\n'
    
    sql_script += 'GO\n\n'

with open(OUT_SQL, 'w', encoding='utf-8') as f:
    f.write(sql_script)

print('SSMS SQL script with Safe Inserts successfully generated at:', OUT_SQL)

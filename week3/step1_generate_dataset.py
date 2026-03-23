"""
step1_generate_dataset.py
Generates 6 EdTech raw (dirty) CSV files with realistic data quality issues:
  learners, courses, assessments, course_enrollments, transactions, academic_calendar
"""

import csv, os, random
from datetime import date, timedelta

OUT = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\dataset\raw'
os.makedirs(OUT, exist_ok=True)

random.seed(42)

def w(folder, filename, rows, headers):
    path = os.path.join(folder, filename)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows([headers] + rows)
    print(f'  ✅ {filename}  ({len(rows)} rows)')

def rdate(start='2022-01-01', end='2024-12-31'):
    s = date.fromisoformat(start)
    e = date.fromisoformat(end)
    return str(s + timedelta(days=random.randint(0, (e-s).days)))

# ─────────────────────────────────────────────────────────────────────────────
# 1. LEARNERS  (50 records)
# ─────────────────────────────────────────────────────────────────────────────
print('\n📋  Generating learners.csv ...')
statuses   = ['Active','active','ACTIVE','Inactive','Pending']
cohorts    = [f'C{i:03d}' for i in range(1, 8)]
first_names = ['Aarav','Priya','Rahul','Sneha','Vikram','Ananya','Rohan','Neha',
               'Arjun','Divya','Kiran','Meera','Suresh','Pooja','Amit','Kavya',
               'Sanjay','Riya','Ajay','Nisha','Raj','Sunita','Deepak','Anjali',
               'Manoj','Sita','Vinod','Leela','Prakash','Geeta']
last_names  = ['Sharma','Patel','Gupta','Singh','Kumar','Mehta','Joshi','Nair',
               'Iyer','Reddy','Verma','Bansal','Malhotra','Kapoor','Pandey']

rows = []
for i in range(1, 51):
    lid       = f'L{i:04d}'
    fname     = random.choice(first_names)
    lname     = random.choice(last_names)
    email     = f'{fname.lower()}.{lname.lower()}{i}@edu.com'
    dob       = rdate('1990-01-01','2005-12-31')
    enrol_dt  = rdate('2022-01-01','2024-06-01')
    cohort    = random.choice(cohorts)
    status    = random.choice(statuses[:2])    # mostly clean
    phone     = f'+91-{random.randint(7000000000,9999999999)}'
    rows.append([lid,fname,lname,email,dob,enrol_dt,cohort,status,phone])

# ── Inject dirty data ──────────────────────────────────────────────────────
rows[2][3]  = ''                              # null email
rows[6][0]  = rows[3][0]                     # duplicate learner_id (same as row 4)
rows[11][3] = 'invalidemail.format'           # missing @
rows[17][4] = '2030-05-12'                   # date_of_birth in future
rows[21][1] = ''                              # null first_name
rows[29][7] = 'ACTIVE'                        # inconsistent status casing
rows[34]    = rows[14][:]                    # full duplicate row
rows[39][8] = 'CALL-ME'                       # letters in phone field
rows[44][5] = '2019-03-01'                   # enrollment before platform launch
rows[47][3] = rows[5][3]                      # duplicate email

w(OUT, 'learners.csv', rows,
  ['learner_id','first_name','last_name','email','date_of_birth',
   'enrollment_date','cohort_id','status','phone'])

# ─────────────────────────────────────────────────────────────────────────────
# 2. COURSES  (20 records)
# ─────────────────────────────────────────────────────────────────────────────
print('📚  Generating courses.csv ...')
categories   = ['Data Science','Web Dev','Business','Design','Marketing','Cloud']
instructors  = [f'I{i:03d}' for i in range(1, 11)]
course_rows  = []
for i in range(1, 21):
    cid      = f'CRS{i:04d}'
    title    = f'Course in {random.choice(categories)} - Level {random.randint(1,3)}'
    cat      = random.choice(categories)
    inst     = random.choice(instructors)
    dur      = random.randint(20, 120)
    sd       = rdate('2022-01-01','2023-06-01')
    ed       = str(date.fromisoformat(sd) + timedelta(days=random.randint(30,180)))
    status   = random.choice(['Published','published','Draft'])
    price    = round(random.uniform(999, 9999), 2)
    course_rows.append([cid,title,cat,inst,dur,sd,ed,status,price])

# ── Dirty ──────────────────────────────────────────────────────────────────
course_rows[4][1]  = ''                          # null course_title
course_rows[7][4]  = -5                          # negative duration_hours
course_rows[10][6] = '2021-01-01'               # end_date before start_date
course_rows[13][3] = ''                          # null instructor_id
course_rows[16][8] = -100                        # negative price
course_rows[18][7] = 'publihsed'                 # typo in status
course_rows[19][4] = 0                           # zero duration

w(OUT, 'courses.csv', course_rows,
  ['course_id','course_title','category','instructor_id','duration_hours',
   'start_date','end_date','status','price'])

# ─────────────────────────────────────────────────────────────────────────────
# 3. ASSESSMENTS  (25 records)
# ─────────────────────────────────────────────────────────────────────────────
print('📝  Generating assessments.csv ...')
a_types  = ['Quiz','Assignment','Project','Midterm','Final Exam']
valid_cids = [course_rows[i][0] for i in range(20) if i not in [4,7,10,13,16,18,19]]
asmt_rows  = []
for i in range(1, 26):
    aid     = f'ASS{i:04d}'
    cid     = random.choice(valid_cids)
    atype   = random.choice(a_types)
    mxs     = random.choice([50, 100])
    pss     = int(mxs * 0.5)
    cd      = rdate('2022-06-01','2023-12-01')
    dd      = str(date.fromisoformat(cd) + timedelta(days=random.randint(7,30)))
    asmt_rows.append([aid,cid,atype,mxs,pss,dd,cd])

# ── Dirty ──────────────────────────────────────────────────────────────────
asmt_rows[5][3]  = 0                             # max_score = 0
asmt_rows[9][4]  = asmt_rows[9][3] + 10          # passing_score > max_score
asmt_rows[13][5] = '2021-01-01'                  # due_date before created_date
asmt_rows[17][2] = ''                             # null assessment_type
asmt_rows[21][1] = 'CRS9999'                     # non-existent course_id
asmt_rows[24][0] = asmt_rows[10][0]              # duplicate assessment_id

w(OUT, 'assessments.csv', asmt_rows,
  ['assessment_id','course_id','assessment_type','max_score','passing_score',
   'due_date','created_date'])

# ─────────────────────────────────────────────────────────────────────────────
# 4. COURSE_ENROLLMENTS  (70 records)
# ─────────────────────────────────────────────────────────────────────────────
print('📌  Generating course_enrollments.csv ...')
valid_lids = [rows[i][0] for i in range(50) if i not in [6,34]]   # exclude dup/missing
enrl_rows  = []
used_pairs = set()
for i in range(1, 71):
    eid  = f'ENR{i:04d}'
    lid  = random.choice(valid_lids)
    cid  = random.choice(valid_cids)
    pair = (lid, cid)
    used_pairs.add(pair)
    ed   = rdate('2022-03-01','2024-01-01')
    cd_  = str(date.fromisoformat(ed) + timedelta(days=random.randint(60,180)))
    grade= random.randint(40, 100)
    st   = random.choice(['Enrolled','Completed','Dropped'])
    enrl_rows.append([eid,lid,cid,ed,cd_,grade,st])

# ── Dirty ──────────────────────────────────────────────────────────────────
enrl_rows[3][1]  = 'L9999'                        # non-existent learner_id
enrl_rows[8][2]  = 'CRS9998'                      # non-existent course_id
enrl_rows[14][4] = '2020-01-01'                   # completion < enrollment date
enrl_rows[19][0] = enrl_rows[5][0]                # duplicate enrollment_id
enrl_rows[24][5] = 150                            # grade out of range
enrl_rows[30][3] = ''                             # null enrollment_date
enrl_rows[45][5] = -5                             # negative grade
enrl_rows[60]    = enrl_rows[20][:]               # full duplicate row

w(OUT, 'course_enrollments.csv', enrl_rows,
  ['enrollment_id','learner_id','course_id','enrollment_date',
   'completion_date','grade','status'])

# ─────────────────────────────────────────────────────────────────────────────
# 5. TRANSACTIONS  (50 records) — TRANSACTION TABLE
# ─────────────────────────────────────────────────────────────────────────────
print('💳  Generating transactions.csv ...')
pay_methods = ['Credit Card','Debit Card','UPI','Net Banking','Wallet']
currencies  = ['INR','USD','EUR']
txn_rows    = []
for i in range(1, 51):
    tid  = f'TXN{i:05d}'
    lid  = random.choice(valid_lids)
    cid  = random.choice(valid_cids)
    amt  = round(random.uniform(999, 9999), 2)
    pm   = random.choice(pay_methods)
    td   = rdate('2022-01-01','2024-03-01')
    st   = random.choice(['Completed','Failed','Refunded'])
    cur  = 'INR'
    txn_rows.append([tid,lid,cid,amt,pm,td,st,cur])

# ── Dirty ──────────────────────────────────────────────────────────────────
txn_rows[4][3]  = -500                           # negative amount
txn_rows[9][0]  = txn_rows[2][0]                 # duplicate transaction_id
txn_rows[15][4] = ''                              # null payment_method
txn_rows[21][1] = 'L9997'                        # non-existent learner_id
txn_rows[27][6] = 'COMPELTED'                    # status typo
txn_rows[32][5] = ''                              # null transaction_date
txn_rows[37][7] = 'us'                            # invalid currency code
txn_rows[44][3] = 0                               # zero amount
txn_rows[49][3] = 9999999                         # unrealistically large amount
txn_rows[3]     = txn_rows[3][:]                  # will duplicate row 3 at idx 48
txn_rows[48]    = txn_rows[3][:]                  # full duplicate transaction

w(OUT, 'transactions.csv', txn_rows,
  ['transaction_id','learner_id','course_id','amount','payment_method',
   'transaction_date','status','currency'])

# ─────────────────────────────────────────────────────────────────────────────
# 6. ACADEMIC_CALENDAR  (10 records) — CALENDAR TABLE
# ─────────────────────────────────────────────────────────────────────────────
print('📅  Generating academic_calendar.csv ...')
cal_rows = [
    ['CAL001','Semester 1 - 2022','2021-2022','2022-01-10','2022-05-31','Yes','2022-01-26,2022-04-15'],
    ['CAL002','Semester 2 - 2022','2021-2022','2022-07-01','2022-11-30','No', '2022-08-15,2022-10-02'],
    ['CAL003','Semester 1 - 2023','2022-2023','2023-06-15','2023-01-10','No', '2023-01-26'],   # end < start
    ['CAL004','Semester 2 - 2023','2022-2023','2023-07-01','2023-11-30','Yes','2023-08-15'],
    ['CAL005','Semester 1 - 2024','2023-2024','2023-10-15','2024-03-31','Yes','2024-01-26'],   # overlaps CAL004
    ['CAL006','Semester 2 - 2024','2023-2024','2024-07-01','2024-11-30','No', '2024-08-15'],
    ['CAL007','','2024-2025',      '2025-01-10','2025-05-31','Yes','2025-01-26'],               # null term_name
    ['CAL001','Semester 1 - 2025','2024-2025','2025-07-01','2025-11-30','No', '2025-08-15'],   # duplicate calendar_id
    ['CAL009','Summer Intensive',  '2023-2024','2024-04-01','2024-04-30','Yes',''],
    ['CAL010','Workshop Series',   '2024-2025','','2025-02-28','Yes',''],                        # null start_date
]

w(OUT, 'academic_calendar.csv', cal_rows,
  ['calendar_id','term_name','academic_year','start_date','end_date','is_active','holidays'])

print(f'\n✅  All 6 raw CSV files generated in:\n    {OUT}')

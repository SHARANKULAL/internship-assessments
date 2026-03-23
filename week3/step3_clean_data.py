"""
step3_clean_data.py
Reads raw CSVs, resolves all identified quality issues, and saves
cleaned CSVs to dataset/cleaned/ folder.
Prints a cleaning summary log.
"""

import pandas as pd
import os, re
from datetime import date, timedelta

RAW   = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\dataset\raw'
CLEAN = r'C:\Users\shara\OneDrive\Desktop\Aptitude\week3\dataset\cleaned'
os.makedirs(CLEAN, exist_ok=True)

log = []   # (table, action)

def note(table, action):
    log.append((table, action))
    print(f'  [{table}]  {action}')

def safe_date(s):
    try:
        return date.fromisoformat(str(s).strip())
    except:
        return None

EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

# ─────────────────────────────────────────────────────────────────────────────
# 1. LEARNERS
# ─────────────────────────────────────────────────────────────────────────────
print('\n🧹  Cleaning learners ...')
df = pd.read_csv(f'{RAW}/learners.csv', dtype=str).fillna('')

# Remove exact duplicate rows
before = len(df)
df.drop_duplicates(inplace=True)
if len(df) < before:
    note('learners', f'Removed {before - len(df)} exact duplicate rows')

# Remove duplicate learner_id — keep first
before = len(df)
df = df[~df['learner_id'].duplicated(keep='first')]
if len(df) < before:
    note('learners', f'Removed {before - len(df)} rows with duplicate learner_id (kept first)')

# Remove duplicate emails (keep first)
dup_em = df[(df['email'] != '') & df['email'].duplicated(keep='first')]
df = df[~((df['email'] != '') & df['email'].duplicated(keep=False) & ~df['email'].duplicated(keep='first'))]
note('learners', f'Removed {len(dup_em)} rows with duplicate email addresses')

# Null email — mark as 'unknown@placeholder.com' if unresolvable
mask = df['email'] == ''
df.loc[mask, 'email'] = df.loc[mask, 'learner_id'].apply(lambda x: f'{x.lower()}@unknown.com')
note('learners', f'Filled {mask.sum()} blank emails with placeholder')

# Invalid email format — mark as 'invalid_<id>@unknown.com'
bad_em = df['email'].apply(lambda e: bool(e) and not EMAIL_RE.match(e))
df.loc[bad_em, 'email'] = df.loc[bad_em, 'learner_id'].apply(lambda x: f'{x.lower()}.fix@unknown.com')
note('learners', f'Replaced {bad_em.sum()} invalid-format emails with placeholder')

# Null first_name — fill with 'Unknown'
mask2 = df['first_name'].str.strip() == ''
df.loc[mask2, 'first_name'] = 'Unknown'
note('learners', f'Set {mask2.sum()} blank first_name to "Unknown"')

# Future date_of_birth — clear field (mark as Unknown)
def fix_dob(dob):
    d = safe_date(dob)
    if d and d > date.today():
        return ''
    return dob
df['date_of_birth'] = df['date_of_birth'].apply(fix_dob)
note('learners', 'Cleared future date_of_birth values')

# Standardise status to Title Case
valid_statuses = {'active': 'Active', 'inactive': 'Inactive', 'pending': 'Pending'}
df['status'] = df['status'].apply(lambda s: valid_statuses.get(str(s).strip().lower(), str(s).strip()))
note('learners', 'Standardised status field to Title Case')

# Phone — remove non-numeric chars except + and -
df['phone'] = df['phone'].apply(lambda p: re.sub(r'[^0-9+\-]', '', str(p)))
note('learners', 'Cleaned phone — removed non-numeric/non-symbol characters')

# Enrollment before 2021 — clear (set to empty for manual review flag)
def fix_enrol(ed):
    d = safe_date(ed)
    if d and d < date(2021, 1, 1):
        return '2021-01-01'   # set to platform launch date
    return ed
df['enrollment_date'] = df['enrollment_date'].apply(fix_enrol)
note('learners', 'Corrected enrollment_dates before platform launch to 2021-01-01')

df.to_csv(f'{CLEAN}/learners_clean.csv', index=False)
print(f'  ✅  learners_clean.csv  ({len(df)} rows)')

# ─────────────────────────────────────────────────────────────────────────────
# 2. COURSES
# ─────────────────────────────────────────────────────────────────────────────
print('\n🧹  Cleaning courses ...')
df2 = pd.read_csv(f'{RAW}/courses.csv', dtype=str).fillna('')

# Null course_title — fill with 'Untitled Course <id>'
mask3 = df2['course_title'].str.strip() == ''
df2.loc[mask3, 'course_title'] = df2.loc[mask3, 'course_id'].apply(lambda x: f'Untitled Course ({x})')
note('courses', f'Filled {mask3.sum()} blank course_title values')

# Null instructor_id — fill with 'UNASSIGNED'
mask4 = df2['instructor_id'].str.strip() == ''
df2.loc[mask4, 'instructor_id'] = 'UNASSIGNED'
note('courses', f'Set {mask4.sum()} blank instructor_id to UNASSIGNED')

# Negative/zero duration_hours — set to 1 (minimum)
def fix_dur(v):
    try:
        f = float(v)
        return str(max(f, 1))
    except:
        return '1'
df2['duration_hours'] = df2['duration_hours'].apply(fix_dur)
note('courses', 'Set negative/zero duration_hours to minimum 1')

# Negative price — set to 0 (free)
def fix_price(v):
    try:
        f = float(v)
        return str(max(f, 0))
    except:
        return '0'
df2['price'] = df2['price'].apply(fix_price)
note('courses', 'Set negative price to 0')

# end_date < start_date — swap dates
def fix_course_dates(row):
    sd = safe_date(row['start_date'])
    ed = safe_date(row['end_date'])
    if sd and ed and ed < sd:
        return pd.Series({'start_date': str(ed), 'end_date': str(sd)})
    return pd.Series({'start_date': row['start_date'], 'end_date': row['end_date']})
df2[['start_date','end_date']] = df2.apply(fix_course_dates, axis=1)
note('courses', 'Swapped start_date/end_date where end was before start')

# Standardise status — map known typos
def fix_course_status(s):
    s = str(s).strip().lower()
    mapping = {'published': 'Published', 'draft': 'Draft', 'archived': 'Archived',
               'publihsed': 'Published', 'publishd': 'Published'}
    return mapping.get(s, 'Draft')
df2['status'] = df2['status'].apply(fix_course_status)
note('courses', 'Standardised and corrected course status values (fixed typos)')

df2.to_csv(f'{CLEAN}/courses_clean.csv', index=False)
print(f'  ✅  courses_clean.csv  ({len(df2)} rows)')

# ─────────────────────────────────────────────────────────────────────────────
# 3. ASSESSMENTS
# ─────────────────────────────────────────────────────────────────────────────
print('\n🧹  Cleaning assessments ...')
df3 = pd.read_csv(f'{RAW}/assessments.csv', dtype=str).fillna('')

# Remove duplicate assessment_id
before = len(df3)
df3 = df3[~df3['assessment_id'].duplicated(keep='first')]
note('assessments', f'Removed {before - len(df3)} duplicate assessment_id rows')

# Null assessment_type — default to 'Quiz'
mask5 = df3['assessment_type'].str.strip() == ''
df3.loc[mask5, 'assessment_type'] = 'Quiz'
note('assessments', f'Defaulted {mask5.sum()} blank assessment_type to "Quiz"')

# max_score ≤ 0 — set to 100
def fix_max(v):
    try:
        f = float(v)
        return str(f if f > 0 else 100)
    except:
        return '100'
df3['max_score'] = df3['max_score'].apply(fix_max)
note('assessments', 'Set max_score ≤ 0 to default 100')

# passing_score > max_score — cap at 50% of max_score
def fix_pass(row):
    try:
        mx = float(row['max_score'])
        ps = float(row['passing_score'])
        return str(ps if ps <= mx else mx * 0.5)
    except:
        return row['passing_score']
df3['passing_score'] = df3.apply(fix_pass, axis=1)
note('assessments', 'Capped passing_score to 50% of max_score where it exceeded max')

# due_date < created_date — set due_date to created_date + 14 days
def fix_asmt_dates(row):
    dd = safe_date(row['due_date'])
    cd = safe_date(row['created_date'])
    if dd and cd and dd < cd:
        return str(cd + timedelta(days=14))
    return row['due_date']
df3['due_date'] = df3.apply(fix_asmt_dates, axis=1)
note('assessments', 'Set due_date to created_date + 14 days where due was before created')

# Orphan course_id — flag only (cannot auto-fix without knowing correct ID)
valid_cids = set(df2['course_id'].tolist())
orphan_mask = df3['course_id'].apply(lambda x: x.strip() != '' and x.strip() not in valid_cids)
df3.loc[orphan_mask, 'course_id'] = 'CRS_UNLINKED'
note('assessments', f'Flagged {orphan_mask.sum()} assessments with non-existent course_id as CRS_UNLINKED')

df3.to_csv(f'{CLEAN}/assessments_clean.csv', index=False)
print(f'  ✅  assessments_clean.csv  ({len(df3)} rows)')

# ─────────────────────────────────────────────────────────────────────────────
# 4. COURSE ENROLLMENTS
# ─────────────────────────────────────────────────────────────────────────────
print('\n🧹  Cleaning course_enrollments ...')
df4 = pd.read_csv(f'{RAW}/course_enrollments.csv', dtype=str).fillna('')

# Remove exact duplicate rows
before = len(df4)
df4.drop_duplicates(inplace=True)
note('course_enrollments', f'Removed {before - len(df4)} exact duplicate rows')

# Remove duplicate enrollment_id — keep first
before = len(df4)
df4 = df4[~df4['enrollment_id'].duplicated(keep='first')]
note('course_enrollments', f'Removed {before - len(df4)} rows with duplicate enrollment_id')

# Remove orphan learner_id
valid_lids = set(df['learner_id'].tolist())
orphan_lid = df4['learner_id'].apply(lambda x: x.strip() not in valid_lids)
df4 = df4[~orphan_lid]
note('course_enrollments', f'Removed {orphan_lid.sum()} rows with non-existent learner_id')

# Remove orphan course_id
orphan_cid = df4['course_id'].apply(lambda x: x.strip() not in valid_cids)
df4 = df4[~orphan_cid]
note('course_enrollments', f'Removed {orphan_cid.sum()} rows with non-existent course_id')

# Null enrollment_date — set to 2022-01-01 as default
mask6 = df4['enrollment_date'].str.strip() == ''
df4.loc[mask6, 'enrollment_date'] = '2022-01-01'
note('course_enrollments', f'Defaulted {mask6.sum()} blank enrollment_date to 2022-01-01')

# completion_date < enrollment_date — swap
def fix_enrl_dates(row):
    ed = safe_date(row['enrollment_date'])
    cd = safe_date(row['completion_date'])
    if ed and cd and cd < ed:
        return str(ed + timedelta(days=90))
    return row['completion_date']
df4['completion_date'] = df4.apply(fix_enrl_dates, axis=1)
note('course_enrollments', 'Fixed completion_date < enrollment_date by adding 90 days offset')

# Grade out of range — cap to [0, 100]
def fix_grade(v):
    try:
        g = float(v)
        return str(min(max(g, 0), 100))
    except:
        return v
df4['grade'] = df4['grade'].apply(fix_grade)
note('course_enrollments', 'Capped grade to 0–100 range')

df4.to_csv(f'{CLEAN}/course_enrollments_clean.csv', index=False)
print(f'  ✅  course_enrollments_clean.csv  ({len(df4)} rows)')

# ─────────────────────────────────────────────────────────────────────────────
# 5. TRANSACTIONS
# ─────────────────────────────────────────────────────────────────────────────
print('\n🧹  Cleaning transactions ...')
df5 = pd.read_csv(f'{RAW}/transactions.csv', dtype=str).fillna('')

# Remove exact duplicate rows
before = len(df5)
df5.drop_duplicates(inplace=True)
note('transactions', f'Removed {before - len(df5)} exact duplicate rows')

# Remove duplicate transaction_id — keep first
before = len(df5)
df5 = df5[~df5['transaction_id'].duplicated(keep='first')]
note('transactions', f'Removed {before - len(df5)} rows with duplicate transaction_id')

# Remove orphan learner_id
orphan_lid2 = df5['learner_id'].apply(lambda x: x.strip() not in valid_lids)
df5 = df5[~orphan_lid2]
note('transactions', f'Removed {orphan_lid2.sum()} rows with non-existent learner_id')

# Negative amount — set to 0 and flag status as Refunded
def fix_amount(row):
    try:
        a = float(row['amount'])
        if a < 0:
            return pd.Series({'amount': '0', 'status': 'Refunded'})
        return pd.Series({'amount': row['amount'], 'status': row['status']})
    except:
        return pd.Series({'amount': row['amount'], 'status': row['status']})
df5[['amount','status']] = df5.apply(fix_amount, axis=1)
note('transactions', 'Set negative amount to 0 and status to Refunded')

# Zero amount — flag as Waiver
mask7 = df5['amount'].apply(lambda x: str(x).strip() == '0' or (x.strip() != '' and float(x) == 0.0))
df5.loc[mask7, 'status'] = 'Waiver'
note('transactions', f'Flagged {mask7.sum()} zero-amount rows as Waiver')

# Null payment_method — set to Unknown
mask8 = df5['payment_method'].str.strip() == ''
df5.loc[mask8, 'payment_method'] = 'Unknown'
note('transactions', f'Set {mask8.sum()} blank payment_method to "Unknown"')

# Null transaction_date — set to 2022-01-01
mask9 = df5['transaction_date'].str.strip() == ''
df5.loc[mask9, 'transaction_date'] = '2022-01-01'
note('transactions', f'Defaulted {mask9.sum()} blank transaction_date to 2022-01-01')

# Invalid currency — correct 'us' to 'USD', others to 'INR'
def fix_currency(c):
    c = str(c).strip().upper()
    known = {'INR','USD','EUR','GBP','AED'}
    mapping = {'US': 'USD', 'UNITED STATES': 'USD', 'RUPEE': 'INR', 'RS': 'INR'}
    return mapping.get(c, c if c in known else 'INR')
df5['currency'] = df5['currency'].apply(fix_currency)
note('transactions', 'Corrected invalid currency codes to ISO 4217 format')

# Standardise status
def fix_txn_status(s):
    s = str(s).strip().lower()
    mapping = {'completed':'Completed','compelted':'Completed','failed':'Failed',
               'refunded':'Refunded','pending':'Pending','waiver':'Waiver'}
    return mapping.get(s, 'Completed')
df5['status'] = df5['status'].apply(fix_txn_status)
note('transactions', 'Standardised and corrected transaction status values (fixed typos)')

df5.to_csv(f'{CLEAN}/transactions_clean.csv', index=False)
print(f'  ✅  transactions_clean.csv  ({len(df5)} rows)')

# ─────────────────────────────────────────────────────────────────────────────
# 6. ACADEMIC CALENDAR
# ─────────────────────────────────────────────────────────────────────────────
print('\n🧹  Cleaning academic_calendar ...')
df6 = pd.read_csv(f'{RAW}/academic_calendar.csv', dtype=str).fillna('')

# Remove duplicate calendar_id — keep first
before = len(df6)
df6 = df6[~df6['calendar_id'].duplicated(keep='first')]
note('academic_calendar', f'Removed {before - len(df6)} rows with duplicate calendar_id')

# Null term_name — fill with 'Term <id>'
mask10 = df6['term_name'].str.strip() == ''
df6.loc[mask10, 'term_name'] = df6.loc[mask10, 'calendar_id'].apply(lambda x: f'Term ({x})')
note('academic_calendar', f'Filled {mask10.sum()} blank term_name values')

# Null start_date — set to 1 Jan of academic year
def fix_start(row):
    if not str(row['start_date']).strip():
        yr = str(row.get('academic_year','2024-2025')).split('-')[0]
        return f'{yr}-01-01'
    return row['start_date']
df6['start_date'] = df6.apply(fix_start, axis=1)
note('academic_calendar', 'Derived blank start_date from academic_year field')

# end_date < start_date — swap
def fix_cal_dates(row):
    sd = safe_date(row['start_date'])
    ed = safe_date(row['end_date'])
    if sd and ed and ed < sd:
        return pd.Series({'start_date': str(ed), 'end_date': str(sd)})
    return pd.Series({'start_date': row['start_date'], 'end_date': row['end_date']})
df6[['start_date','end_date']] = df6.apply(fix_cal_dates, axis=1)
note('academic_calendar', 'Swapped start_date/end_date where end was before start')

# Overlapping terms — adjust end_date of earlier term to day before next starts
df6_sorted = df6.copy()
df6_sorted['_sd'] = df6_sorted['start_date'].apply(safe_date)
df6_sorted['_ed'] = df6_sorted['end_date'].apply(safe_date)
df6_sorted.sort_values('_sd', inplace=True, na_position='last')
prev_ed = None
for idx in df6_sorted.index:
    sd = df6_sorted.loc[idx, '_sd']
    ed = df6_sorted.loc[idx, '_ed']
    if prev_ed and sd and sd <= prev_ed:
        new_sd = prev_ed + timedelta(days=1)
        df6_sorted.loc[idx, 'start_date'] = str(new_sd)
        df6_sorted.loc[idx, '_sd'] = new_sd
        note('academic_calendar', f'Fixed overlapping term at row {idx+2}: moved start_date to {new_sd}')
    if ed:
        prev_ed = ed
df6 = df6_sorted.drop(columns=['_sd','_ed'])

df6.to_csv(f'{CLEAN}/academic_calendar_clean.csv', index=False)
print(f'  ✅  academic_calendar_clean.csv  ({len(df6)} rows)')

# ─────────────────────────────────────────────────────────────────────────────
# PRINT SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
print(f'\n{"─"*60}')
print(f'  CLEANING SUMMARY — {len(log)} fixes applied')
print(f'{"─"*60}')
for i, (tbl, action) in enumerate(log, 1):
    print(f'  {i:02d}. [{tbl}] {action}')
print(f'\n✅  All cleaned CSVs saved to: {CLEAN}')

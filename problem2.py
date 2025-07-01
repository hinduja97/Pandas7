def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    high=accounts[accounts['income']> 50000]
    avg=accounts[(accounts['income']> 20000) & (accounts['income']<50000)]
    low=accounts[accounts['income']< 20000]
    return pd.DataFrame([
        ['Low Salary',len(low)],
        ['Average Salary',len(avg)],
        ['High Salary',len(high)]],columns=['category','accounts_count'])
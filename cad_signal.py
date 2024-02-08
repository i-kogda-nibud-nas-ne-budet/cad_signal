import pandas as pd

def get_signals(filename):
    df = pd.read_excel(filename + '_obj.xls', engine='xlrd')
    df = df[['INDEX', 'Имя']]
    mask = (
        df['INDEX'].str.len() > 0) & (
        ~df["INDEX"].str.contains('_', na=False))
    df.loc[mask, 'INDEX'] = df['INDEX'].astype(str) + '_XQ02'
    df = df[df["INDEX"].str.contains('_', na=False)]
    df[['KKS', 'signal']] = df['INDEX'].str.split('_', expand=True)
    df.to_excel(filename + '_signal.xls', index=False)
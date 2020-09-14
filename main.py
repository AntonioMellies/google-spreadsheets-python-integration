import gspread
import os
import pandas as pd
import settings
import mail


def main():
    if os.environ.get('CREDENTIALS_FILE'):
        gc = gspread.service_account(os.environ.get('CREDENTIALS_FILE'))
    else:
        raise Exception(
            'Variable CREDENTIALS_FILE not found in Environment (.env)')

    if os.environ.get('URL_SPREADSHEET'):
        sh = gc.open_by_url(os.environ.get('URL_SPREADSHEET'))
    else:
        raise Exception(
            'Variable URL_SPREADSHEET not found in Environment (.env)')

    worksheet = sh.sheet1
    df = pd.DataFrame(worksheet.get_all_records())

    # Filter dataframe
    dfp = df.loc[df['Status (Responsável)'] == 'AJUSTADO']

    count_pendency = dfp.shape[0]
    print(f'Pendencias: {count_pendency}')
    if count_pendency:
        mail.sendNotification(df)


if __name__ == "__main__":
    main()

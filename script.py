import pandas as pd

wb = pd.read_excel('Teste.xlsx')

df = pd.DataFrame(wb)

df.to_csv('TesteCSV.csv',sep=',',index=False, encoding='utf_8')
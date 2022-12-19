import tabula
import csv

pdf_path = './testdata/fraeskatalog_milling_catalogue_1.pdf'
alternative = './testdata/schema.pdf'
output_path = './results/output.csv'

dfs = tabula.read_pdf(pdf_path, stream=True, pages=6)
print(dfs[0])

with open('./results/output2.csv', 'w') as f:

    writer = csv.writer(f)

    for value in dfs[0].values:
        writer.writerow(value)

tabula.convert_into(alternative, output_path, output_format='csv', pages='all')

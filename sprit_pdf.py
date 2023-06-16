import pypdf
from pypdf import PdfReader, PdfWriter


# merger = pypdf.PdfMerger()

# merger.append('./input/input.pdf', pages=(0, 15))
# print("loading pdf file...")
# # merger.append('data/src/pdf/sample2.pdf', pages=(2, 4))
# # print("splitting pdf file...")

# merger.write('./output/output.pdf')
# print("saving pdf file...")

# merger.close()
# print("done")


all_page_count = 615

for i in range(int(all_page_count / 15)):
    merger = pypdf.PdfMerger()
    merger.append('./input/input.pdf', pages=(15 * i , (i * 15) + 15))
    print(f"loading pdf file...{i}")
    merger.write(f'./output/output_{i * 15}' +  "_" + f'{(i*15) + 15}.pdf')
    print("saving pdf file...")
    merger.close()

print("done")
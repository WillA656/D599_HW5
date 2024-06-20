import hashlib
import base64
import os
import pandas as pd

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
book_loc = "C:\\Users\\wt_an\\MSDS\\DATA 599 (Cloud Computing)\\scripts\\books"

url_list = ['austen.txt','bronte.txt','shelley.txt']



def make_tsv(list):
    output_list = []
    output_list.append(['TsvHttpData-1.0'])

    for txt in list:
        url = PREFIX+txt
        prepath = book_loc+"\\"+txt
        file = open(prepath,"rb")
        content = file.read()
        meta = os.path.getsize(prepath)
        md5_hash = hashlib.md5(content).digest()
        md5 = base64.b64encode(md5_hash).decode()
        output_list.append([url,meta,md5])
        file.close()

    pd.DataFrame(output_list).to_csv(book_loc+'\\books.tsv',sep='\t',index=False,header=False)



if __name__ == "__main__":
    make_tsv(url_list)
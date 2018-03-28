import glob
import os
from pdf_extractor import extract_pdf_content
import pandas as pd
import matplotlib.pyplot as plt



def get_mydict_from_pdf_path(mydict, pdf_path):
    pdfs = glob.glob("{}/*.pdf".format(pdf_path))
    for pdf in pdfs:
        content = extract_pdf_content(pdf)
        with open(pdf.replace('.pdf', '.txt'), 'w', encoding='utf-8') as f:
            f.write(content)
        key = pdf.split('/')[-1]
        if not key in mydict:
            print("Extracting content from {} ...".format(pdf))
            mydict[key] = extract_pdf_content(pdf)
    return mydict


def make_df_from_mydict(mydict):
    df = pd.DataFrame.from_dict(mydict, orient='index').reset_index()
    df.columns = ["path", "content"]
    return df


def draw_df(df):
    df["length"] = df.content.apply(lambda x: len(x))
    plt.figure(figsize=(14, 6))
    df.set_index('path').length.plot(kind='bar')
    plt.xticks(rotation=45)
    plt.show()


mydict={}
pdf_path = 'pdf/'
mydict = get_mydict_from_pdf_path(mydict, pdf_path)
df = make_df_from_mydict(mydict)
draw_df(df)
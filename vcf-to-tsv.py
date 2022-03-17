import pandas as pd
from itertools import islice
import os
location= os.getcwd()
print("converting vcfs to tsv")

#function to convert vcf to tsv
def vcf2tsv(vcf,output):
    # Opening a file
    file = open(vcf,"r")
    counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    #counting the lines
    for i in CoList:
        if i:
            counter += 1
    
    #reading vcf and writing it in another text
    with open(vcf, "r") as f:
        for line in f:
            if "#CHROM" in line:
                header1=line
                print ("".join(islice(f,counter)),file=open(output, "w"))
    
    tsv=pd.read_csv(output, sep='\t', header=None)
    tsv.columns=header1.split('\t')
    tsv.to_csv(output, sep='\t',index=False)

def vfolderprocess(vcffolder):
    vcflist=os.listdir(vcffolder)
    os.system('cd '+ vcffolder)
    os.system('mkdir output-tsv')
    
    for f in vcflist:
        vcf= vcffolder+ '/' + f
        output= vcffolder+ '/output-tsv/' + f.split('.vcf')[0] + '.tsv'
        
        vcf2tsv(vcf,output)


vfolderprocess(location)

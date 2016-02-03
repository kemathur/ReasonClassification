#!/usr/bin/env python3
#coding: utf8 

'''
rouge similarity
@author: amita
'''


import os,sys
from pyrouge import Rouge155
import json
from optparse import OptionParser

def get_opts():
    parser = OptionParser()
    parser.add_option("--stringa", dest="str_a",help="First string")
    parser.add_option("--stringb", dest= "str_b",help="second string")
    parser.add_option("--writedir", dest="write_dir", help="Tmp write directory for rouge")
   
    (options, args) = parser.parse_args()

    if options.str_a is None:
        print("Error: requires string")
        parser.print_help()
        sys.exit(-1)

    if options.str_b is  None:
        print("Error:requires string")
        parser.print_help()
        sys.exit(-1)
        
    if options.write_dir is  None:
        print("Error:requires write directory for rouge")
        parser.print_help()
        sys.exit(-1)    

    return (options, args)

def readTextFile(Filename): 
        f = open(Filename, "r", encoding='utf-8')
        TextLines=f.readlines()
        f.close()
        return TextLines

def writeTextFile(Filename,Lines): 
        f = open(Filename, "w",encoding='utf-8')
        f.writelines(Lines)
        f.close()

def rougue(stringa, stringb, writedirRouge):
    newrow={}
    r = Rouge155()
    count=0
    dirname_sys= writedirRouge +"rougue/System/"
    dirname_mod=writedirRouge +"rougue/Model/"
    if not os.path.exists(dirname_sys):
        os.makedirs(dirname_sys)
    if not os.path.exists(dirname_mod):  
        os.makedirs(dirname_mod)
    Filename=dirname_sys +"string_."+str(count)+".txt"
    LinesA=list()
    LinesA.append(stringa)
    writeTextFile(Filename, LinesA)
    LinesB=list()
    LinesB.append(stringb)
    Filename=dirname_mod+"string_.A."+str(count)+ ".txt"
    writeTextFile(Filename, LinesB)
    r.system_dir = dirname_sys
    r.model_dir = dirname_mod
    r.system_filename_pattern = 'string_.(\d+).txt'
    r.model_filename_pattern = 'string_.[A-Z].#ID#.txt'
    output = r.convert_and_evaluate()
    output_dict = r.output_to_dict(output)
    newrow["rouge_1_f_score"]=output_dict["rouge_1_f_score"]
    newrow["rouge_2_f_score"]=output_dict["rouge_2_f_score"]
    newrow["rouge_3_f_score"]=output_dict["rouge_3_f_score"]
    newrow["rouge_4_f_score"]=output_dict["rouge_4_f_score"]
    newrow["rouge_l_f_score"]=output_dict["rouge_l_f_score"]
    newrow["rouge_s*_f_score"]=output_dict["rouge_s*_f_score"]
    newrow["rouge_su*_f_score"]=output_dict["rouge_su*_f_score"]
    newrow["rouge_w_1.2_f_score"]=output_dict["rouge_w_1.2_f_score"]
    rouge_dict=json.dumps(newrow)
    print (rouge_dict)


def run():
    (options, args) = get_opts()   
    stringa=options.str_a
    stringb=options.str_b
    writedir=options.write_dir 
    rougue(stringa, stringb, writedir)
    
        
if __name__ == '__main__':
    run()
    
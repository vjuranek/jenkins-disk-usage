# -*- coding: utf-8 -*-

import db_queries as db
import utils as u

def generate(file_path, limit):
    CAPTION = "Top %i disk consumers"%limit

    jobs = db.top_jobs(limit)
    
    ft = open(file_path,"w")
    
    ft.write("\\begin{table}[h!]\n")
    ft.write("\\centering\n")
    ft.write("\\begin{tabular}{|c|c|}\n")
    ft.write("\t\\hline\n")

    ft.write("\t\\textbf{Job name} & \\textbf{Size [GB]}  \\\\ \n")

    ft.write("\t\\hline\n")
    ft.write("\t\\hline\n")
    
    for item in jobs:
        print "%s\t%i"%(item[0],item[1])
        ft.write("\t\t %s \t & \t  %3.1f"%(u.tex_fix_str(item[0]), item[1]) + " \\\\\n")

    ft.write("\t\\hline\n")
    ft.write("\\end{tabular}\n")
    ft.write("\t\\caption{%s}\n"%CAPTION)
    ft.write("\\end{table}\n")

    ft.close()


# -*- coding: utf-8 -*-

import db_queries as db

def generate(file_path):
    CAPTION = "Size of builds, artifacts and logs. Artifacts and logs are not disjunct sets, logs include also archived logs."

    sizes = db.bal_size()
    
    ft = open(file_path,"w")
    
    ft.write("\\begin{table}[h!]\n")
    ft.write("\\centering\n")
    ft.write("\\begin{tabular}{|c|c|}\n")
    ft.write("\t\\hline\n")

    ft.write("\t\\textbf{Type} & \\textbf{Size [GB]}  \\\\ \n")

    ft.write("\t\\hline\n")
    ft.write("\t\\hline\n")
    
    ft.write("\t\t Builds \t & \t  %3.1f \\\\\n"%sizes[0])
    ft.write("\t\t Artifacts \t & \t  %3.1f \\\\\n"%sizes[1])
    ft.write("\t\t Logs \t & \t  %3.1f \\\\\n"%sizes[2])

    ft.write("\t\\hline\n")        
    ft.write("\\end{tabular}\n")
    ft.write("\t\\caption{%s}\n"%CAPTION)
    ft.write("\\end{table}\n")

    ft.close()

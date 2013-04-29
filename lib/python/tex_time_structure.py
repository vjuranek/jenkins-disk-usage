# -*- coding: utf-8 -*-

import db_queries as db

def generate(file_path, days):
    CAPTION = "Disk space occupied by jobs according to their age."

    sizes = db.size_of_builds_older_than(days)
    
    ft = open(file_path,"w")

    ft.write("\\begin{table}[h!]\n")
    ft.write("\\centering\n")
    ft.write("\\begin{tabular}{|c|c|}\n")
    ft.write("\t\\hline\n")
    
    ft.write("\t\\textbf{Builds older than X [days]} & \\textbf{Size [GB]}  \\\\ \n")

    ft.write("\t\\hline\n")
    ft.write("\t\\hline\n")
     
    for item in sizes:
        print "%i\t%3.1f"%(item[0],item[1])
        ft.write("\t\t %i \t & \t  %3.1f"%(item[0], item[1]) + " \\\\\n")
        
    ft.write("\t\\hline\n")
    ft.write("\\end{tabular}\n")
    ft.write("\t\\caption{%s}\n"%CAPTION)
    ft.write("\\end{table}\n")


    ft.close()

# -*- coding: utf-8 -*-

import db_queries as db

def generate(file_path, days):
    CAPTION = "Disk space occupied by jobs according to their age."

    sizes = db.size_of_builds_older_than(days)
    
    ft = open(file_path,"w")
    
    ft.write("\\begin{longtable}{|c|c|}\n")
    ft.write("\t\\hline\n")
    ft.write("\t\\textbf{Builds older than X [days]} & \\textbf{Size [GB]}  \\\\ \\hline\n")
    ft.write("\t\\hline\n")
    ft.write("\t\\endhead\n")
    ft.write("\t\\hline\n")
    ft.write("\t\\endfoot\n")
    ft.write("\t\\hline\n")
    ft.write("\t\\caption{%s}\n"%CAPTION)
    ft.write("\t\\endlastfoot\n")
    
    for item in sizes:
        print "%i\t%3.1f"%(item[0],item[1])
        ft.write("\t\t %i \t & \t  %3.1f"%(item[0], item[1]) + " \\\\\n")
        
    ft.write("\\end{longtable}\n")

    ft.close()

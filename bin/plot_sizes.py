#!/usr/bin/env python
# -*- coding: utf-8 -*-

import db_queries as db
import plot_mp as mp

for i in [30,60,90,180,360,720]:
    res = db.balsize_older_than(i)
    print "Build youner than %i occupies %4.1f GB, artifacts occupies %4.1f GB and logs occupies %4.1f GB"%(i,res[0],res[1],res[2])
# print "Build sizes: %3.1f GB"%res[0][0]
# print "Artifact sizes: %3.1f GB"%res[0][1]
# print "Log sizes: %3.1f GB"%res[0][2]

# data = []

# for item in res:
#     print "%f\t%s"%(item[0],item[1])
#     data.append([time.strptime(item[1],"%y-%m-%d"), item[0]])


# graph = mp.create_graph(data,'Date [y-m-d]','Average load')
# mp.save(graph,"loadYear",img_dir="../eps_mp")

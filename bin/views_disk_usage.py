#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils as utils
import db_queries as db

base_url = "http://jenkins.mw.lab.eng.bos.redhat.com/hudson/view/"
views = open("../data/views.txt","r")
sizes = []
for view in views:
    view = view.strip()
    view_url = base_url + view.replace(" ","%20")
    jobs = utils.jenkins_get_jobs_from_view(view_url)
    if(len(jobs) > 0):
        size = db.size_of_job_set(jobs)
        print "View %s has %3.1f GB (%i jobs)"%(view,size[0],size[1])
        sizes.append((view,size[0],size[1]))

print "------------"
sizes = sorted(sizes,key = lambda size:-1*size[1])
for size in sizes:
    print "View %s has %3.1f GB (%i jobs)"%(size[0],size[1],size[2])

print "------------"
for size in sizes:
    print "%s & %3.1f & %i \\\\"%(size[0],size[1],size[2])

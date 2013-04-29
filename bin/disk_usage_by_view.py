#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import utils as utils
import db_queries as db

print "Getting jobs for %s"%sys.argv[1]
jobs = utils.jenkins_get_jobs_from_view(sys.argv[1])
print "#jobs: %i"%len(jobs)
size = db.size_of_job_set(jobs)
print "Size of jobs in the view is %3.1f GB (%i jobs)"%(size[0],size[1])

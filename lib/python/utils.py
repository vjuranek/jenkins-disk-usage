# -*- coding: utf-8 -*-

from jenkinsapi.api import get_view_from_url, get_view_by_url

def tex_fix_str(str):
    return str.replace("&","\&").replace("_","\_")

def jenkins_get_jobs_from_view(view_url):
    jobs = []
    view = get_view_by_url(view_url)
    get_jobs_from_view(view, jobs)    
    return set(jobs)

def get_jobs_from_view(view, jobs):
    # print view
    jj = view.get_job_dict()
    for j in jj:
        # print "\t" + j
        jobs.append(j)
    views = view.get_nested_view_dict()
    for v in views:
        nv = get_view_from_url(views[v].replace("%20"," "))
        get_jobs_from_view(nv,jobs)


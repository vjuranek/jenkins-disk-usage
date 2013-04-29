#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

def top_jobs(limit):
    q = "select job as job_name,job_size/(1024^3) as job_size from jobs order by job_size desc limit %i;"%limit
    return do_query(q)

def bsize_younger_than(interval):
    q = "select sum(build_size)/(1024^3) as bsize from builds where (time > (current_date - interval '%i days'));"%interval
    return do_query(q)[0][0]

def asize_younger_than(interval):
    q = "select sum(artif_size)/(1024^3) as asize from builds where (time > (current_date - interval '%i days'));"%interval
    return do_query(q)[0][0]

def lsize_younger_than(interval):
    q = "select sum(log_size)/(1024^3) as lsize from builds where (time > (current_date - interval '%i days'));"%interval
    return do_query(q)[0][0]

def balsize_younger_than(interval):
    q = "select sum(build_size)/(1024^3), sum(artif_size)/(1024^3) as asize, sum(log_size)/(1024^3) as lsize from builds where (time > (current_date - interval '%i days'));"%interval
    return do_query(q)[0]

def bsize_older_than(interval):
    q = "select sum(build_size)/(1024^3) as bsize from builds where (time < (current_date - interval '%i days'));"%interval
    return do_query(q)[0][0]

def asize_older_than(interval):
    q = "select sum(artif_size)/(1024^3) as asize from builds where (time < (current_date - interval '%i days'));"%interval
    return do_query(q)[0][0]

def lsize_older_than(interval):
    q = "select sum(log_size)/(1024^3) as lsize from builds where (time < (current_date - interval '%i days'));"%interval
    return do_query(q)[0][0]

def balsize_older_than(interval):
    q = "select sum(build_size)/(1024^3), sum(artif_size)/(1024^3) as asize, sum(log_size)/(1024^3) as lsize from builds where (time < (current_date - interval '%i days'));"%interval
    return do_query(q)[0]

def bal_size():
    q = "select sum(build_size)/(1024^3), sum(artif_size)/(1024^3) as asize, sum(log_size)/(1024^3) as lsize from builds;"
    return do_query(q)[0]

def size_of_job_set(job_set):
    q_set = ""
    for job in job_set:
        q_set += "'%s',"%job
    q_set = q_set[:(len(q_set)-1)]
    q = "select sum(job_size)/(1024^3), count(job) from jobs where job in (%s);"%q_set
    return do_query(q)[0]

def size_of_builds_older_than(days):
    results = []
    for limit in days:
        q = "select sum(build_size)/(1024^3) from builds where (time < (current_date - interval '%i days'));"%limit
        size = do_query(q)[0][0]
        results.append([limit,size])
    return results

def do_query(query):
    conn = psycopg2.connect("dbname=DiskUsage3 user=vjuranek")
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    return res

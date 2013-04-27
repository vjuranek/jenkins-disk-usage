select job as job_name,job_size as job_size from jobs order by job_size desc;
select job as job_name, sum(artif_size) as asize from builds group by job_name order by asize desc;
select job as job_name, sum(artif_size)as asize from builds where job='JOB_NAME' group by job_name;
select sum(job_size) as job_size from jobs where job like 'JOB_PREFIX%';
select sum(job_size)/(1024^3) as job_size from jobs where job like 'JOB_PREFIX%';


select build_dir, build_size from builds where (job='JOB_NAME') and (time > (current_date - interval '30 days')) order by build_size desc;
select sum(build_size)/(1024^3) from builds where (job='JOB_NAME') and (time > (current_date - interval '30 days'));

select sum(build_size)/(1024^3) from builds where (time > (current_date - interval '30 days'));
select sum(log_size)/(1024^3) from builds where (time > (current_date - interval '30 days'));
select sum(artif_size)/(1024^3) from builds where (time > (current_date - interval '30 days'));


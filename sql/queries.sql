select job as job_name,job_size as job_size from jobs order by job_size desc;
select job as job_name, sum(artif_size) as asize from builds group by job_name order by asize desc;
select job as job_name, sum(artif_size)as asize from builds where job='JOB_NAME' group by job_name;

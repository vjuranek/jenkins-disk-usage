CREATE TABLE jobs(job varchar(256), job_size bigint, builds_size bigint, artif_size bigint, log_size bigint);
CREATE TABLE builds(job varchar(256), build_dir varchar(1024), time timestamp, build_size bigint, artif_size bigint, log_size bigint);

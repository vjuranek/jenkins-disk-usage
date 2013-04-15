#!/bin/bash 

#-----===== General =====-----

get_jobs() {
    local jobs=`find $1 -mindepth 1 -maxdepth 1 -type d`
    echo $jobs
}

job_name() {
    local bname=`echo $1 | awk -F / '{print $NF}'`
    echo $bname
}

dir_size() {
    local dsize=`du -bs $1 | cut -f 1`
    echo $dsize
}

build_size() {
    local bsize=`find $1 -name builds -type d | xargs -r du -bc | awk '{if($2 == "total") print $1}'`
    if [[  -z $bsize ]]; then local bsize=0; fi
    echo $bsize
}

artif_size() {
    local asize=`find $1 -name archive -type d | xargs -r du -bc | awk '{if($2 == "total") print $1}'`
    if [[ -z $asize ]]; then local asize=0; fi
    echo $asize
}

log_size() {
    local lsize=`find $1 -name *log -type f | xargs -r du -bc | awk '{if($2 == "total") print $1}'`
    if [[ -z $lsize ]]; then local lsize=0; fi
    echo $lsize
}

get_build_dirs() {
    local build_dirs=`find $1 -name builds -type d`
    echo $build_dirs
}

get_builds() {
    local builds=`find $1 -mindepth 1 -maxdepth 1 -type d`
    echo $builds
}

build_date() {
    local bdate=`echo "$1" | awk -F / '{print $NF}'`
    local ndate=`echo $bdate | awk -F "_" '{gsub("-",":",$2); print $1, $2}'`
    echo $ndate
}


#-----===== Jobs =====-----

print_sizes() {
    echo -e "\t Dir size: $1"
    echo -e "\t Build size: $2"
    echo -e "\t Artifact size: $3"
    echo -e "\t Log size: $4"
}

print_job_sizes() {
    echo "Job $1:"
    local dsize=`dir_size $1`
    local bsize=`build_size $1`
    local asize=`artif_size $1`
    local lsize=`log_size $1`
    print_sizes $dsize $bsize $asize $lsize
}

print_job_sql_insert() {
    # echo "INSERT INTO jobs(job, job_size, builds_size, artif_size, log_size) VALUES('$1',$2,$3,$4,$5);"
    echo "INSERT INTO jobs VALUES('$1',$2,$3,$4,$5);"
}

job_sql_insert() {
    local job_name=`job_name $job`
    local dsize=`dir_size $1`
    local bsize=`build_size $1`
    local asize=`artif_size $1`
    local lsize=`log_size $1`
    echo `print_job_sql_insert $job_name $dsize $bsize $asize $lsize`
}

list_job_sizes() {
    local jobs=`get_jobs $1`
    echo "Jobs: $jobs"
    for job in $jobs; do
	do_sizes $job
    done
}

#-----===== Builds =====-----

print_builds() {
    for build in $builds; do
	echo -e "\t $build"
	echo -e "\t\t `build_date $build`"
    done
}

print_build_sql_insert() {
    # echo "INSERT INTO builds(job, build_dir, time, build_size, artif_size, log_size) VALUES('$1','$2','$3',$4,$5,$6);"
    echo "INSERT INTO builds VALUES('$1','$2','$3',$4,$5,$6);"
}

build_sql_insert() {
    local job_name=`job_name $1`
    local build_dirs=`get_build_dirs $1`

    if [[ -z $build_dirs ]]; then
	return
    fi

    for build_dir in $build_dirs; do
	local builds=`get_builds $build_dirs`
	if [[ -z $builds ]]; then
	    continue
	fi
	for build in $builds; do
	    local btime=`build_date $build`
	    local bsize=`dir_size $build`
	    local asize=`artif_size $build`
	    local lsize=`log_size`
	    echo `print_build_sql_insert "$job_name" "$build" "$btime" $bsize $asize $lsize`
	done
    done

}

#-----===== Main =====-----

check_args() {
    if [[ !($# -eq 3) ]]; then
	echo "Expecting 3 argument but $# given."
	echo `print_usage`
	exit 1
    fi
}

print_help() {
    echo "Scans Jenkins job directory, count sizes of jobs, builds, artifacts and logs and dump it into SQL insert so it can be imported in database and analyse later on."
    echo "Usage: disk_usage_to_sql jenkins_job_dir jobs_sql_file builds_sql_file"
}

print_usage() {
    echo "Usage: disk_usage_to_sql jenkins_job_dir jobs_sql_file builds_sql_file"
}

prepare_sql_files() {
    echo "DROP TABLE IF EXISTS jobs;" > $1
    echo "CREATE TABLE jobs(job varchar(256), job_size bigint, builds_size bigint, artif_size bigint, log_size bigint);" >> $1
    echo "DROP TABLE IF EXISTS builds;" > $2
    echo "CREATE TABLE builds(job varchar(256), build_dir varchar(1024), time timestamp, build_size bigint, artif_size bigint, log_size bigint);" >> $2
}

create_inserts() {
    check_args $@
    prepare_sql_files $2 $3
    local jobs=`get_jobs $1`
    for job in $jobs; do
	job_sql_insert $job >> $2
	build_sql_insert $job >> $3
    done
}


create_inserts $1 $2 $3


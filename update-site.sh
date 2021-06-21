#!/bin/bash

set -e          # exit on failure
set -o pipefail # pipes pass failure

# << FILL ME IN TO COMPETE TEMPLATE >>
# What is the project name (must be URI compliant)
SITE_NAME='Comport (XStack)'
# What is the URL for the Site (must be URL complient & ommit protocall)
SITE_URL='osterohutan-UofU.github.io/comport' #! Update me latergit

# The main dir of the cpu-website-backend git
REPO_ROOT_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}")" && pwd )"
# Where this file should be located in the cpu-website-backend git
SCRIPT_DIR="$( cd ${REPO_ROOT_DIR} && cd scripts && pwd )"
# The main dir of the cpu-website git
CONTENT_DIR="$( cd ${REPO_ROOT_DIR} && cd site-content && pwd )"
# The location of the jekyll website directory
SITE_SRC_DIR="$( cd ${REPO_ROOT_DIR} && cd site-src && pwd )"
# Logfile is located in the backed git
LOGFILE=${REPO_ROOT_DIR}/logs/update_log.txt
# Get time stamp
TIME_STAMP=$( date +"%Y-%m-%d %T" )

#? unnessisary for hosting on github pages
# # Location on shell that the website will be served from
# FV_TARGET_DIR=/uusoc/sys/www/formalverification.cs.utah.edu/new
# PAR_TARGET_DIR=/uusoc/sys/www/parallel.utah.edu

#! WHILE LOOP UNNESISSARY THIS WILL BE DONE WITH A CHRON JOB INSTEAD
# FIRST=1
# while true
# do

# Go to the repo root and see if there are updates (via git)
cd ${REPO_ROOT_DIR}
CHANGED=1
git pull |& grep -q -v 'Already up-to-date.' && CHANGED=0

# check if local copy is up to date
if [[ -z $( git status -s ) ]]; then
	CHANGED=0
else 
	echo -e "Local Changes detected!\n" |& tee -a ${LOGFILE}
	CHANGED=1
fi

# if [[ ${FIRST} -eq 1 || ${CHANGED} -eq 1 ]]
if [[ ${CHANGED} -eq 1 ]]; then
	# There were
	if [[ ${FIRST} -eq 1 ]]; then
		echo -e "\nMaking sure websites are updated\n\n" |& tee -a ${LOGFILE}
	else
		echo -e "\nUpdate found\n\n" |& tee -a ${LOGFILE}
	fi

	# FIRST=0

	# Do a real pull to get the content
	echo "git pull output:" |& tee -a ${LOGFILE}
	git pull --verbose |& tee -a ${LOGFILE}
	echo -e "\n\n" |& tee -a ${LOGFILE}

	# formalverification.cs.utah.edu
	echo -e "\nUpdating ${SITE_NAME} (${URL})\n" |& tee -a ${LOGFILE}

	# Run the script that takes content and formats it for the backend
	cd ${SCRIPT_DIR}
	echo "update.py output:" |& tee -a ${LOGFILE}
	python3 "${SCRIPT_DIR}/update.py" ${SITE_SRC_DIR} ${CONTENT_DIR} |& tee -a ${LOGFILE}
	echo -e "\n\n" |& tee -a ${LOGFILE}

	# Update blogs
	echo "updating blog output:" |& tee -a ${LOGFILE}
	rm -rf ${SITE_SRC_DIR}/_posts
	mkdir ${SITE_SRC_DIR}/_posts
	find ${CONTENT_DIR} -regex ".*/[0-9][0-9][0-9][0-9]-[0-9]?[0-9]-[0-9]?[0-9]-.*\.md" | xargs -I{} cp -v {} ${SITE_SRC_DIR}/_posts |& tee -a ${LOGFILE}
	echo -e "\n\n" |& tee -a ${LOGFILE}

	# Run jekyll to build the new version of the website
	cd ${SITE_SRC_DIR}
	echo "bundle exec jekyll build output:" |& tee -a ${LOGFILE}
	bundle exec jekyll build |& tee -a ${LOGFILE}
	echo -e "\n\n" |& tee -a ${LOGFILE}

	# Push updated repo to GitHub
	cd ${REPO_ROOT_DIR} && git add --all && git commit -m "AUTO_BUILD :: ${TIME_STAMP}" && git push

	#? unnesissary since it is hosted on github not locally
	# # Tar it up for transfer
	# tar zcf fv_site_tar.gz _site
	#
	# # Transfer it to shell
	# echo "scp output:" |& tee -a ${LOGFILE}
	# scp fv_site_tar.gz ${USER}@shell.cs.utah.edu:${FV_TARGET_DIR} |& tee -a ${LOGFILE}
	# echo -e "\n\n" |& tee -a ${LOGFILE}
	#
	# # Ssh into shell and run the updater script
	# echo "ssh output:" |& tee -a ${LOGFILE}
	# ssh ${USER}@shell.cs.utah.edu "${FV_TARGET_DIR}/updateSite.bash fv_site_tar.gz"  |& tee -a ${LOGFILE}
	# echo -e "\n\n" |& tee -a ${LOGFILE}

	echo -e "\nDone updating ${SITE_NAME} (${URL})\n\n\n" |& tee -a ${LOGFILE}

fi #? added to prevent rest of commented otu code from running

# # Parallel.cs.utah.edu
# echo -e "\nUpdating parallel.cs.utah.edu\n" |& tee -a ${LOGFILE}

# # Run the script that takes content and formats it for the backend
# cd ${SCRIPT_DIR}
# echo "update.py output:" |& tee -a ${LOGFILE}
# ./update.py ${REPO_ROOT_DIR}/parallel ${CONTENT_DIR} -cpu |& tee -a ${LOGFILE}
# echo -e "\n\n" |& tee -a ${LOGFILE}

# # Update blogs
# echo "updating blog output:" |& tee -a ${LOGFILE}
# rm -rf ${REPO_ROOT_DIR}/parallel/_posts
# mkdir ${REPO_ROOT_DIR}/parallel/_posts
# find ${CONTENT_DIR} -regex ".*/[0-9][0-9][0-9][0-9]-[0-9]?[0-9]-[0-9]?[0-9]-.*\.md" | xargs -I{} cp -v {} ${REPO_ROOT_DIR}/parallel/_posts |& tee -a ${LOGFILE}
# echo -e "\n\n" |& tee -a ${LOGFILE}

# # Run jekyll to build the new version of the website
# cd ${REPO_ROOT_DIR}/parallel
# echo "bundle exec jekyll build output:" |& tee -a ${LOGFILE}
# bundle exec jekyll build |& tee -a ${LOGFILE}
# echo -e "\n\n" |& tee -a ${LOGFILE}

# # Tar it up for transfer
# tar zcf par_site_tar.gz _site

# # Transfer it to shell
# echo "scp output:" |& tee -a ${LOGFILE}
# scp par_site_tar.gz ${USER}@shell.cs.utah.edu:${PAR_TARGET_DIR} |& tee -a ${LOGFILE}
# echo -e "\n\n" |& tee -a ${LOGFILE}

# # Ssh into shell and run the updater script
# echo "ssh output:" |& tee -a ${LOGFILE}
# ssh ${USER}@shell.cs.utah.edu "${PAR_TARGET_DIR}/updateSite.bash par_site_tar.gz" |& tee -a ${LOGFILE}
# echo -e "\n\n" |& tee -a ${LOGFILE}

# echo -e "\nDone updating parallell.cs.utah.edu\n" |& tee -a ${LOGFILE}

# else
# # No update
# echo -n "."
# fi

# # Wait a while before trying again
# sleep $[ 60 * 10 ]s
# done

# ScoreBot - Team Gamification Bot

Service has a REST API to collect so called “scores” from various sources (Jira, Gerrit,  
Jenkins, wiki); a set of triggers which check people ranks; and a bot API to post  
events to Slack channels. Scores are POSTed to the service for the actions like  
new review, new bug report and so on. Once person collects enough scores (per day,  
per week...) he receives a message/badge from ScoreBot.

## Requirements
* Docker 1.10 or later
* Docker-compose 1.10 or later

## Installation
Get source code:
```
git clone https://github.com/cloudlinux/scorebot.git && cd scorebot
```
Create and fill your local config file:
```
cp ./config/config{_sample,}.py  
vi ./config/config.py
```

## Usage
###### Start service
```
./ops/start_service.sh
```

###### Stop service
```
./ops/stop_service.sh
```  
WARNING: this drops all the data. Backup before stopping!

###### Backup
Scorebot uses CouchDB to store its data, this is the only state that requires backup.
```
./ops/backup_db.sh
```
You may want to run this from /etc/cron.daily/ (will require `cd` to scorebot).  
Backups will be stored at `./backups/`

###### Restore
Restore does not require stopping the service API, however you may want to do  
this to avoid HTTP 500 ret-codes while DB is being restarted.

```
./ops/restore_db.sh ./backups/<name_of_the_backup>
```

## Integrations 
##### An abstract review system
Can be done via webhook which calls scorebot REST API. Currently supported API endpoints:
* `curl -X POST -d '{"player_name": "mlobur"}' http://server:8080/scores/patchset_reviewed`
* `curl -X POST -d '{"player_name": "mlobur"}' http://server:8080/scores/patchset_proposed`
* `curl -X POST -d '{"player_name": "mlobur"}' http://server:8080/scores/patchset_merged`

##### Gerrit (via Jenkins job)
Gerrit does not have webhooks, but scorebot can still be intergrated though a Jenkins job. See example [HERE](integrations/gerrit_jenkins/job_scorebot.sh)

##### Task trackers (e.g. JIRA)
TBD. More to come once scorebot has corresponding triggers and API endpoints.

## Contributing
Pull requests welcome. Source code is distributed under MIT.

###### Running a dev server:
Create venv: `./dev/mk_venv.sh` (requires virtualenv wrapper)  

Start DB: `./dev/db.sh`  (non-blocking)

Start API: `./dev/server.sh`  (blocking, must be run from venv)

Posting a score:
```
curl -X POST -d '{"player_name": "rnoyce"}' http://localhost:8000/scores/patchset_reviewed
```
Populating DB with a huge batch of test scores:
```
python dev/gen_test_data.py
```

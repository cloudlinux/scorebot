#!/bin/bash
set -x
set -e

#
# Jenkins job running based on a Gerrit event-trigger
#
# 1) Install Gerrit plugin to Jenkins
# 2) Create a Jenkins job with Build Trigger "Gerrit event"
# 3) Configure a job (e.g. add repos, branches, etc)
# 4) Use this script as "Execute shell" body.
#

SCOREBOT_IP='XX.XX.XX.XX'
SCOREBOT='http://$SCOREBOT_IP:8080'

function do_post() {
    local headers
    local json
    local user
    local action
    user=$1
    event=$2
    headers="Content-Type: application/json"
    json="{\"player_name\": \"${user}\"}"

    curl -H "${headers}" -X POST -d "${json}" ${SCOREBOT}/scores/${event}
}

function get_action() {
    case "$GERRIT_EVENT_TYPE" in
      change-merged) ret="patchset_merged";;
      patchset-created) ret="patchset_proposed";;
      comment-added) ret="patchset_reviewed";;
    esac

    echo $ret
}

function get_review_user() {
    echo ${GERRIT_CHANGE_OWNER_EMAIL%@*}
}

function get_event_user() {
    echo ${GERRIT_EVENT_ACCOUNT_EMAIL%@*}
}

function get_user() {
    if [ "$1" = "patchset_merged" ]; then
        get_review_user
    else
        get_event_user
    fi
}

action=$(get_action)
user=$(get_user ${action})

do_post $user $action

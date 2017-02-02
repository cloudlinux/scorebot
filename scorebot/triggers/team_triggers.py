from scorebot.db import db_api, db_utils
from scorebot.triggers.triggers_base import TeamTrigger, GroupOfTeamTriggers

team_triggers = {
    db_api.PatchsetProposed.type: GroupOfTeamTriggers(
        score_db_api=db_api.PatchsetProposed,
        triggers=[
            # week
            TeamTrigger(
                name="team_patchset_proposed_for_week1",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=50,
                msg="{owner} making good progress this week, posted "
                    "their 50th patch-set",
            ),
            TeamTrigger(
                name="team_patchset_proposed_for_week2",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=100,
                msg="{owner} is really active this week, they just posted "
                    "their 100th patch-set!",
            ),
            # month
            TeamTrigger(
                name="team_patchset_proposed_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=200,
                msg="{owner} made 200 patchsets this month! Cheers!",
            ),
            TeamTrigger(
                name="team_patchset_proposed_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=300,
                msg="{owner} even reached 300 patchsets this month!",
            ),
        ]
    ),

    db_api.PatchsetMerged.type: GroupOfTeamTriggers(
        score_db_api=db_api.PatchsetMerged,
        triggers=[
            # today
            TeamTrigger(
                name="team_patchset_merged_for_today1",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=5,
                msg="{owner} just merged their 5th review today!"
            ),
            # week
            TeamTrigger(
                name="team_patchset_merged_for_week1",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=10,
                msg="{owner} is doing great! 10 reviews landed this week!"
            ),
            # month
            TeamTrigger(
                name="team_patchset_merged_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=30,
                msg="{owner} rocks! 30 reviews merged this month already!"
            ),
            TeamTrigger(
                name="team_patchset_merged_for_month2",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=50,
                msg="{owner} keeps putting +2 randomly: 50 reviews merged "
                    "this month. And looks like the're not gonna stop!"
            )
        ]
    ),

    db_api.PatchsetReviewed.type: GroupOfTeamTriggers(
        score_db_api=db_api.PatchsetReviewed,
        triggers=[
            # week
            TeamTrigger(
                name="team_patchset_reviewed_for_week1",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=50,
                msg="{owner} is really keeps an eye on each other, made 50 "
                    "reviews this week already!"
            ),
            # month
            TeamTrigger(
                name="team_patchset_reviewed_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=100,
                msg="{owner} has great review activity this month, reached "
                    "100 reviews just now!"
            )
        ]
    )
}

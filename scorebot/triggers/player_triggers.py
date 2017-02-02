from scorebot.db import db_api, db_utils
from scorebot.triggers.triggers_base import PlayerTrigger, \
    GroupOfPlayerTriggers

# TODO convert to yaml?

player_triggers = {
    db_api.PatchsetProposed.type: GroupOfPlayerTriggers(
        score_db_api=db_api.PatchsetProposed,
        triggers=[
            # today
            PlayerTrigger(
                name="patchset_proposed_for_today1",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=3,
                msg="{owner} is making progress, posted his 3rd patchset "
                    "today!",
            ),
            PlayerTrigger(
                name="patchset_proposed_for_today2",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=5,
                msg="Cheers {owner}! You've just made your 5th patch-set "
                    "for today!",
            ),
            PlayerTrigger(
                name="patchset_proposed_for_today3",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=10,
                msg="{owner} is unstoppable! Just posted a 10th patch-set "
                    "for a day! Someone, ask him to take a rest!",
            ),
            # week
            PlayerTrigger(
                name="patchset_proposed_for_week1",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=20,
                msg="{owner} is rocking this week: 20 patch-sets and "
                    "keeps going!",
            ),
            PlayerTrigger(
                name="patchset_proposed_for_week2",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=30,
                msg="{owner} is a beast! Just proposed 30th patch-set for a "
                    "week!",
            ),
            PlayerTrigger(
                name="patchset_proposed_for_week3",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=50,
                msg="{owner} dude, get some rest, seriously! You just posted "
                    "your 50th patch-set in this week!"
            ),
            # month
            PlayerTrigger(
                name="patchset_proposed_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=50,
                msg="{owner} has a productive month: just proposed "
                    "50th patch-set!"
            ),
            PlayerTrigger(
                name="patchset_proposed_for_month2",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=100,
                msg="{owner} has a crazy month! Over 100 patch-sets already!"
            ),
        ]
    ),

    db_api.PatchsetMerged.type: GroupOfPlayerTriggers(
        score_db_api=db_api.PatchsetMerged,
        triggers=[
            # today
            PlayerTrigger(
                name="patchset_merged_for_today1",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=1,
                msg="{owner} merge day has started for you, 1st review just "
                    "landed!",
            ),
            PlayerTrigger(
                name="patchset_merged_for_today2",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=2,
                msg="{owner} what a day huh? Your 2nd review for today just "
                    "landed!",
            ),
            PlayerTrigger(
                name="patchset_merged_for_today3",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=3,
                msg="{owner}, lucky bastard, you just got your 3rd review "
                    "merged for today!",
            ),
            PlayerTrigger(
                name="patchset_merged_for_today4",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=4,
                msg="{owner}, did you hack gerrit? 4 merged reviews for a day, "
                    "how is that possible?!",
            ),
            # week
            PlayerTrigger(
                name="patchset_merged_for_week1",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=3,
                msg="{owner} is making a good progress, got his 3rd review "
                    "merged for a week!",
            ),
            PlayerTrigger(
                name="patchset_merged_for_week2",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=5,
                msg="{owner}'s 5th review for this week got merged "
                    "just now! w00t!",
            ),
            # month
            PlayerTrigger(
                name="patchset_merged_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=10,
                msg="{owner}, you have a productive month - 10 reviews "
                    "merged by now!",
            ),
        ]
    ),

    db_api.PatchsetReviewed.type: GroupOfPlayerTriggers(
        score_db_api=db_api.PatchsetReviewed,
        triggers=[
            # today
            PlayerTrigger(
                name="patchset_reviewed_for_today1",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=3,
                msg="{owner} is looking through reviews, just put his 3rd "
                    "review score for today",
            ),
            PlayerTrigger(
                name="patchset_reviewed_for_today2",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=6,
                msg="Nothing can hide from {owner}, 6th review today!",
            ),
            PlayerTrigger(
                name="patchset_reviewed_for_today3",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=10,
                msg="{owner} keeps hanging in Gerrit, 10th review today. "
                    "Scorebot suggests him to do some real work instead :D",
            ),
            PlayerTrigger(
                name="patchset_reviewed_for_today4",
                get_date_scope=db_utils.DateScope.today,
                trigger_point=11,
                msg="{owner} ignores Scorebot's suggestion",
            ),
            # week
            PlayerTrigger(
                name="patchset_reviewed_for_week1",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=30,
                msg="{owner} is an eager reviewer! He just left his 30th "
                    "review score this week!",
            ),
            PlayerTrigger(
                name="patchset_reviewed_for_week2",
                get_date_scope=db_utils.DateScope.this_week,
                trigger_point=50,
                msg="{owner} is like an Eye of Sauron! Just did his 50th "
                    "review this week!",
            ),
            # month
            PlayerTrigger(
                name="patchset_reviewed_for_month1",
                get_date_scope=db_utils.DateScope.this_month,
                trigger_point=100,
                msg="Looks like {owner} really wanna know what everyone else "
                    "is doing - just made 100th review this month",
            ),
        ]
    ),
}

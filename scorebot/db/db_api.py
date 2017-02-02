import logging

from scorebot.db import db_utils
from scorebot.db.db_base import BaseScore, DB

LOG = logging.getLogger(__name__)


class TriggerFlag:
    type = "trigger_flag"

    @classmethod
    def create(cls, set_for_trigger, set_for_owner):
        """Saves trigger flag to db. Used to prevent triggers fire >1 times.

        :param set_for_trigger: for which trigger to set flag
        :param set_for_owner: for which owner to set flag
        :return: doc - resulting trigger flag.
        """
        doc = {
            "type": cls.type,
            "set_for_trigger": set_for_trigger,
            "set_for_owner": set_for_owner,
        }
        db_utils.set_created_at(doc)
        return DB.save(doc)

    @classmethod
    def list_for_trigger(cls, for_trigger, date_scope):
        """Get all flags set for particular trigger in a date scope

        :param for_trigger: for which trigger to fetch
        :param date_scope: in what date scope
        :return: Dict {owner: True/False}
        """
        map = """
        function(doc) {
            if (%s && doc.type == '%s' && doc.set_for_trigger == '%s') {
                emit(doc.set_for_owner, 1);
            }
        }""" % (date_scope, cls.type, for_trigger)
        reduce = "_sum"

        res = {}
        for record in DB.temporary_query(map, reduce, group='true'):
            owner = record['key']
            is_set = record['value'] > 0
            res[owner] = is_set
        return res


class PatchsetProposed(BaseScore):
    type = "patchset_proposed"


class PatchsetReviewed(BaseScore):
    type = "patchset_reviewed"


class PatchsetMerged(BaseScore):
    type = "patchset_merged"
    # TODO add affected_loc {lang: loc}
    # TODO add new_ut, edited_ut, new_it, edited_it


# Below classes are not supported yet.

class AffectedLinesOfCode(BaseScore):
    type = "affected_loc"
    required_fields = BaseScore.required_fields + ("loc", "lang")


class TaskCreated(BaseScore):
    type = "task_created"


class TaskCommented(BaseScore):
    type = "task_commented"


class TaskDone(BaseScore):
    type = "task_done"


class BugReported(BaseScore):
    type = "bug_reported"


class BugFixed(BaseScore):
    type = "bug_fixed"

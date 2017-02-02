import os
import logging

from config.config import CONF

LOG = logging.getLogger(__name__)


# When debugging, all channels must point to bot-testing channel
if os.environ.get("SB_DEV", False):
    test_chan = CONF['slack_channels']['bot-testing']
    CONF['slack_channels'] = {k: test_chan for k in CONF['slack_channels']}


class BaseBot:
    @classmethod
    def say(cls, dest, message, owner):
        """
        Say to destination channel

        :param dest: destination channel/thread
        :param message: non-formatted message
        :param owner: str(team_name) or player_info, whom this message is about
        :return: None
        """
        raise NotImplemented

import logging

from slackclient import SlackClient

from config.config import CONF
from scorebot.bots import speech
from scorebot.bots.bot_base import BaseBot

LOG = logging.getLogger(__name__)


class SlackBot(BaseBot):

    @classmethod
    def _connect(cls):
        slack = SlackClient(CONF["slack_token"])
        if slack.rtm_connect():
            LOG.info("SlackBot connected to slack.com")
            return slack
        else:
            raise Exception("SlackBot connection failed.")

    @classmethod
    def _fmt_msg(cls, message, owner):
        if hasattr(owner, 'slack_name'):
            owner = owner.slack_name
        return message.format(owner=owner)

    @classmethod
    def say(cls, dest, message, owner, machine_readable=False):
        msg = cls._fmt_msg(message, owner)

        greeting = speech.hello()
        msg = "{}! {}".format(greeting, msg)

        LOG.info("SENDING MESSAGE TO SLACK '{}' channel: {}".format(dest, msg))
        slack = cls._connect()
        slack.rtm_send_message(dest, msg)

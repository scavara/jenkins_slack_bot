#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : slack_message.py
## Author : Vivek Grover <vivek271091@gmail.com>, Denny Zhang <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-08-27>
## Updated: Time-stamp: <2017-09-25 17:14:34>
##-------------------------------------------------------------------
from slack import WebClient
import os
import slackbot

# update the message after the button click
def update_message(channel_id, ts_id, mesg):
    """

    """
    icon_emoji = ':white_check_mark: %s' % mesg
    slack_client = WebClient(os.environ.get('SLACK_BOT_TOKEN'))
    slack_client.api_call(
        "chat.update",
        channel=channel_id,
        text='%s' % icon_emoji,
        ts=ts_id,
        attachments=[{}]
    )


# send the message with button
def send_interactive_message(username, im_id, chann_id):
    """

    """
    icon_emoji = ':white_check_mark:'
    slack_client = WebClient(os.environ.get('SLACK_BOT_TOKEN'))
    channels_call = slack_client.api_call("im.list")
    slack_client.api_call(
        "chat.postMessage",
        channel='{0}'.format(im_id),
        as_user=False,
        attachments=[{
                         "text": "@{0} has send the request for approval.\n Do you Approve the Request?".format(
                             username), "attachment_type": "default",
                         "callback_id": "{0}_{1}".format(username,chann_id),
                         "actions": [{"name": "option", "text": "Approve", "type": "button", "value": "Approve"}, {
                             "name": "no",
                             "text": "Decline",
                             "type": "button",
                             "value": "Not Approved"
                         }]}]

    )


# send the message without button
def send_message_without_button(username, msg, chann_id):
    """

    """
    slack_client = WebClient(os.environ.get('SLACK_BOT_TOKEN'))
    channels_call = slack_client.api_call("im.list")
    user_id = slackbot.get_bot_id(username, slack_client)
    slack_client.api_call(
        "chat.postMessage",
        channel='{0}'.format(chann_id),
        text='<@{0}>'.format(user_id),
        username='chatbot2',
        as_user=True,
        attachments=[{"text": "{1}".format(user_id, msg), "color": "green", "attachment_type": "default"}]
    )
## File : slack_message.py ends

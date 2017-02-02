CONF = {
    # Retrieved from https://your_company.slack.com/services/XXXXX
    "slack_token": "xoxb-XXXXXX.....",

    # - All teams appearing in players must have corresponding channels
    # - "cross-team" is a required channel (used by BotApi.say_all)
    # - "bot-testing" is a required channel (used during debug)
    "slack_channels": {
        "team1": "product-t1",
        "team2": "product-t2",
        "team3": "product-t3",
        "cross-team": "product-all",
        "bot-testing": "bot-test-chan"
    },

    # key - Name as it will appear in incoming POST requests
    # val - (player's team, player's nickname in slack)
    # Note that nickname in slack does not have to correspond to key.
    "players": {
        "mlobur": ('team1', 'mlobur'),
        "sroberts": ('team1', 'sroberts'),
        "gmoore": ('team1', 'gmoore29'),

        "ekleiner": ('team2', "ekleiner"),
        "vgrinich": ('team2', "vgrinich"),

        "rnoyce": ('team3', "rnoyce27"),
        "jblank": ('team3', "jblank"),
        "jhoerni": ('team3', "jhoerni"),
        "jlast": ('team3', "jlast"),
    }
}

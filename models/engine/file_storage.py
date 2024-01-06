#!/usr/bin/python3
import json
"""storage file"""


class Filesotrage:

    def save(self):
        """save method"""
        return json.dumps(self)

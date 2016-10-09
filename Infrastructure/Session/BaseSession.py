#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from hashlib import sha1


class BaseSession:

    session_id = "__sessionId__"

    create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()


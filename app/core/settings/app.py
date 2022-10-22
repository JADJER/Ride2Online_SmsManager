#  Copyright 2022 Pavel Suprunov
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging

from pydantic import HttpUrl

from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False
    title: str = "SmsManager"
    version: str = "0.0.1"

    rabbitmq_server: str = "localhost"
    rabbitmq_user: str = ""
    rabbitmq_pass: str = ""
    rabbitmq_channel: str = "sms"

    sms_api_host: HttpUrl = "http://127.0.0.1"
    sms_api_user: str = ""
    sms_api_pass: str = ""

    logging_level: int = logging.INFO

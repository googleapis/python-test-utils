# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import random


RESOURCE_PREFIX = "python_bigquery_datatransfer_samples_snippets"
RESOURCE_DATE_FORMAT = "%Y%m%d%H%M%S"
RESOURCE_DATE_LENGTH = 4 + 2 + 2 + 2 + 2 + 2


def resource_prefix() -> str:
    timestamp = datetime.datetime.utcnow().strftime(RESOURCE_DATE_FORMAT)
    random_string = hex(random.randrange(1000000))[2:]
    return f"{RESOURCE_PREFIX}_{timestamp}_{random_string}"


def resource_name_to_date(resource_name: str) -> datetime.datetime:
    start_date = len(RESOURCE_PREFIX) + 1
    date_string = resource_name[start_date : start_date + RESOURCE_DATE_LENGTH]
    parsed_date = datetime.datetime.strptime(date_string, RESOURCE_DATE_FORMAT)
    return parsed_date


def should_cleanup(resource_name: str) -> bool:
    yesterday = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    return (
        resource_name.startswith(RESOURCE_PREFIX)
        and resource_name_to_date(resource_name) < yesterday
    )


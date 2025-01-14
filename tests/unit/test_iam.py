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

import pytest  # type: ignore

import google.auth
import requests
import google.auth.transport.requests


def test_iam():
  credentials, project_id = google.auth.default()
  request = google.auth.transport.requests.Request()
  credentials.refresh(request)
  token = credentials.token
  resp = requests.post(f"https://oauth2.googleapis.com/tokeninfo", data={
    'access_token': token    
  }, headers={
    'content-type': 'application/x-www-form-urlencoded'
  })
  data = resp.json()
  print(data['email'])
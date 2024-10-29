#!/bin/bash
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -eo pipefail

# Start the releasetool reporter
python3 -m pip install --require-hashes -r github/python-test-utils/.kokoro/requirements.txt
python3 -m releasetool publish-reporter-script > /tmp/publisher-script; source /tmp/publisher-script

# Disable buffering, so that the logs stream through.
export PYTHONUNBUFFERED=1

# Move into the package, build the distribution and upload.
TWINE_PASSWORD=$(cat "${KOKORO_KEYSTORE_DIR}/73713_google-cloud-pypi-token-keystore-3")
cd github/python-test-utils

python3 setup.py sdist bdist_wheel
gcloud config get-value core/account

python3 -m pip install -U keyring > /dev/null
python3 -m pip install -U keyrings.google-artifactregistry-auth > /dev/null
python3 -m pip install -U twine > /dev/null

if ! gcloud auth application-default print-access-token --quiet > /dev/null; then
    gcloud auth application-default login
fi

twine upload --repository-url https://us-python.pkg.dev/oss-exit-gate-prod/google-cloud-testutils--pypi/ dist/*

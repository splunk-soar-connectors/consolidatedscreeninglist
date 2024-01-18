# File: consolidatedscreeninglist_consts.py
#
# Copyright (c) 2020-2024 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
BASE_URL = "https://data.trade.gov"
LOOKUP_ENDPOINT = "/consolidated_screening_list/v1/search?"

# Constants relating to '_get_error_message_from_exception'
ERR_CODE_MSG = "Error code unavailable"
ERR_MSG_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters"
PARSE_ERR_MSG = "Unable to parse the error message. Please check the asset configuration and|or action parameters"

# Constants relating to '_validate_integer'
INVALID_INTEGER_ERR_MSG = "Please provide a valid integer value in the {}"
INVALID_NON_ZERO_NON_NEGATIVE_INTEGER_ERR_MSG = "Please provide a valid non-zero positive integer value in the {}"

LIMIT_KEY = "'limit' action parameter"

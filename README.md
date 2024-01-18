[comment]: # "Auto-generated SOAR connector documentation"
# Consolidated Screening List

Publisher: Splunk Community  
Connector Version: 1.0.3  
Product Vendor: Splunk  
Product Name: Consolidated Screening List  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.1.1  

This app integrates with ConsolidatedScreeningList API that consolidates export screening lists of the Departments of Commerce, State and, the Treasury into a single data feed as an aid to industry in conducting electronic screens of potential parties to regulated transactions, to perform investigative actions

[comment]: # "File: README.md"
[comment]: # "Copyright (c) 2020-2024 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Consolidated Screening List asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**auth_token** |  required  | password | API Bearer Token

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[lookup user](#action-lookup-user) - Validate if a specified individual is found in the Consolidated Screening List watchlist  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'lookup user'
Validate if a specified individual is found in the Consolidated Screening List watchlist

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**name** |  required  | Searches against the 'name' and 'alt_names' fields | string | 
**country** |  optional  | 2-character country code | string | 
**limit** |  optional  | Number of records to include in the response | numeric | 
**fuzzy_name** |  optional  | Enables users to query a name and get usable results without knowing the exact spelling of an entry | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.name | string |  |   Example name 
action_result.parameter.country | string |  |  
action_result.parameter.limit | numeric |  |   1 
action_result.parameter.fuzzy_name | boolean |  |   True  False 
action_result.data.\*.total | numeric |  |   135 
action_result.data.\*.search_performed_at | string |  |   2020-12-10T06:59:53.060+00:00 
action_result.data.\*.results.\*.license_policy | string |  |   Example license policy 
action_result.data.\*.results.\*.addresses.\*.city | string |  |   Example city 
action_result.data.\*.results.\*.addresses.\*.state | string |  |   Example state 
action_result.data.\*.results.\*.addresses.\*.address | string |  |   Example address 
action_result.data.\*.results.\*.addresses.\*.postal_code | string |  |   Example postal code 
action_result.data.\*.results.\*.addresses.\*.country | string |  |   Example country 
action_result.data.\*.results.\*.source_list_url | string |  `url`  |   http://example.com 
action_result.data.\*.results.\*.title | string |  |  
action_result.data.\*.results.\*.standard_order | string |  |  
action_result.data.\*.results.\*.alt_names | string |  |   Example name 
action_result.data.\*.results.\*.id | string |  `sha1`  |   1a3ccc08ecbb40155a4cce8d9c9ace917f54cc74 
action_result.data.\*.results.\*.source | string |  |   Example source 
action_result.data.\*.results.\*.federal_register_notice | string |  |   Example register notice 
action_result.data.\*.results.\*.license_requirement | string |  |   Example license requirement 
action_result.data.\*.results.\*.source_information_url | string |  `url`  |   http://example.com 
action_result.data.\*.results.\*.start_date | string |  |   2019-05-21 
action_result.data.\*.results.\*.name | string |  |   Example name 
action_result.data.\*.sources_used.\*.source | string |  |   Example source 
action_result.data.\*.sources_used.\*.last_imported | string |  |   2020-12-10T06:35:04.366+00:00 
action_result.data.\*.sources_used.\*.import_rate | string |  |   Hourly 
action_result.data.\*.sources_used.\*.source_last_updated | string |  |   2020-07-22T15:56:51.583+00:00 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Match: True 
action_result.summary.match | boolean |  |   True  False 
action_result.summary.total_fetched_results | numeric |  |   1 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
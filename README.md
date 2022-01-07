[comment]: # "Auto-generated SOAR connector documentation"
# Consolidated Screening List

Publisher: Splunk Community  
Connector Version: 1\.0\.1  
Product Vendor: Splunk  
Product Name: Consolidated Screening List  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app integrates with ConsolidatedScreeningList API that consolidates export screening lists of the Departments of Commerce, State and, the Treasury into a single data feed as an aid to industry in conducting electronic screens of potential parties to regulated transactions, to perform investigative actions

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Consolidated Screening List asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**auth\_token** |  required  | password | API Bearer Token

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
**name** |  required  | Searches against the 'name' and 'alt\_names' fields | string | 
**country** |  optional  | 2\-character country code | string | 
**limit** |  optional  | Number of records to include in the response | numeric | 
**fuzzy\_name** |  optional  | Enables users to query a name and get usable results without knowing the exact spelling of an entry | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.name | string | 
action\_result\.parameter\.country | string | 
action\_result\.parameter\.limit | numeric | 
action\_result\.parameter\.fuzzy\_name | boolean | 
action\_result\.data\.\*\.total | numeric | 
action\_result\.data\.\*\.search\_performed\_at | string | 
action\_result\.data\.\*\.results\.\*\.license\_policy | string | 
action\_result\.data\.\*\.results\.\*\.addresses\.\*\.city | string | 
action\_result\.data\.\*\.results\.\*\.addresses\.\*\.state | string | 
action\_result\.data\.\*\.results\.\*\.addresses\.\*\.address | string | 
action\_result\.data\.\*\.results\.\*\.addresses\.\*\.postal\_code | string | 
action\_result\.data\.\*\.results\.\*\.addresses\.\*\.country | string | 
action\_result\.data\.\*\.results\.\*\.source\_list\_url | string |  `url` 
action\_result\.data\.\*\.results\.\*\.title | string | 
action\_result\.data\.\*\.results\.\*\.standard\_order | string | 
action\_result\.data\.\*\.results\.\*\.alt\_names | string | 
action\_result\.data\.\*\.results\.\*\.id | string |  `sha1` 
action\_result\.data\.\*\.results\.\*\.source | string | 
action\_result\.data\.\*\.results\.\*\.federal\_register\_notice | string | 
action\_result\.data\.\*\.results\.\*\.license\_requirement | string | 
action\_result\.data\.\*\.results\.\*\.source\_information\_url | string |  `url` 
action\_result\.data\.\*\.results\.\*\.start\_date | string | 
action\_result\.data\.\*\.results\.\*\.name | string | 
action\_result\.data\.\*\.sources\_used\.\*\.source | string | 
action\_result\.data\.\*\.sources\_used\.\*\.last\_imported | string | 
action\_result\.data\.\*\.sources\_used\.\*\.import\_rate | string | 
action\_result\.data\.\*\.sources\_used\.\*\.source\_last\_updated | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.match | boolean | 
action\_result\.summary\.total\_fetched\_results | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
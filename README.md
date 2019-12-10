# Getting started

Send SMS with Onfon Media SMS Platform.

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python)


## How to Use

The following section explains how to use the Onfonmediasmsgateway SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python&projectName=onfonmediasmsgateway)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python&projectName=onfonmediasmsgateway)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python&projectName=onfonmediasmsgateway)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from onfonmediasmsgateway.onfonmediasmsgateway_client import OnfonmediasmsgatewayClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python&libraryName=onfonmediasmsgateway.onfonmediasmsgateway_client&projectName=onfonmediasmsgateway&className=OnfonmediasmsgatewayClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=OnfonMedia%20SMS%20Gateway-Python&libraryName=onfonmediasmsgateway.onfonmediasmsgateway_client&projectName=onfonmediasmsgateway&className=OnfonmediasmsgatewayClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| access_key | Network Layer Access Key |
| api_key | Used for authentication purpose and pass this parameter in URL encoded format. |
| client_id | Used for authentication purpose and pass this parameter in URL encoded format. |



API client can be initialized as following.

```python
# Configuration parameters and credentials
access_key = 'ACCESS_KEY' # Network Layer Access Key
api_key = 'API_KEY' # Used for authentication purpose and pass this parameter in URL encoded format.
client_id = 'CLIENT_ID' # Used for authentication purpose and pass this parameter in URL encoded format.

client = OnfonmediasmsgatewayClient(access_key, api_key, client_id)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [AccountController](#account_controller)
* [TemplateController](#template_controller)
* [SMSController](#sms_controller)
* [GROUPController](#group_controller)
* [CampaignController](#campaign_controller)

## <a name="account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AccountController") AccountController

### Get controller instance

An instance of the ``` AccountController ``` class can be accessed from the API Client.

```python
 account_controller = client.account
```

### <a name="get_credit_balance"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.get_credit_balance") get_credit_balance

> Get Credit Balance

```python
def get_credit_balance(self)
```

#### Example Usage

```python

result = account_controller.get_credit_balance()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="template_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TemplateController") TemplateController

### Get controller instance

An instance of the ``` TemplateController ``` class can be accessed from the API Client.

```python
 template_controller = client.template
```

### <a name="get_template_list"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.get_template_list") get_template_list

> Get Template List

```python
def get_template_list(self)
```

#### Example Usage

```python

result = template_controller.get_template_list()

```


### <a name="create_new_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.create_new_template") create_new_template

> Create New Template

```python
def create_new_template(self,
                            message_template,
                            template_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageTemplate |  ``` Required ```  | Template text. |
| templateName |  ``` Required ```  | Name of template |



#### Example Usage

```python
message_template = 'MessageTemplate'
template_name = 'TemplateName'

result = template_controller.create_new_template(message_template, template_name)

```


### <a name="update_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.update_template") update_template

> Update Template

```python
def update_template(self,
                        message_template,
                        template_name,
                        id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageTemplate |  ``` Required ```  | Template text. |
| templateName |  ``` Required ```  | Name of template |
| id |  ``` Required ```  | id of template |



#### Example Usage

```python
message_template = 'MessageTemplate'
template_name = 'TemplateName'
id = 162

result = template_controller.update_template(message_template, template_name, id)

```


### <a name="delete_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.delete_template") delete_template

> Delete Template

```python
def delete_template(self,
                        id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | id of template |



#### Example Usage

```python
id = 162

result = template_controller.delete_template(id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sms_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMSController") SMSController

### Get controller instance

An instance of the ``` SMSController ``` class can be accessed from the API Client.

```python
 sms_controller = client.sms
```

### <a name="get_sent_message_list"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.get_sent_message_list") get_sent_message_list

> Get Sent Message List

```python
def get_sent_message_list(self,
                              enddate,
                              fromdate,
                              length,
                              start)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| enddate |  ``` Required ```  | Date format must be in yyyy-mm-dd |
| fromdate |  ``` Required ```  | Date format must be in yyyy-mm-dd |
| length |  ``` Required ```  | Ending index value to fetch the campaign detail. |
| start |  ``` Required ```  | Starting index value to fetch the campaign detail. |



#### Example Usage

```python
enddate = datetime.now()
fromdate = datetime.now()
length = 162
start = 162

result = sms_controller.get_sent_message_list(enddate, fromdate, length, start)

```


### <a name="get_sent_message_status"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.get_sent_message_status") get_sent_message_status

> Get Sent Message Status

```python
def get_sent_message_status(self,
                                message_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageId |  ``` Required ```  | MessageId of message |



#### Example Usage

```python
message_id = 162

result = sms_controller.get_sent_message_status(message_id)

```


### <a name="get_create_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.get_create_sms") get_create_sms

> Create SMS

```python
def get_create_sms(self,
                       message,
                       mobile_number,
                       sender_id,
                       co_relator=None,
                       is_flash=None,
                       is_unicode=None,
                       link_id=None,
                       group_id=None,
                       schedule_time=None,
                       service_id=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| message |  ``` Required ```  | text message to send |
| mobileNumber |  ``` Required ```  | Use mobile number as comma sepreated to send message on multiple mobile number e.g. 78461230,78945612 |
| senderId |  ``` Required ```  | Approved Sender Id |
| coRelator |  ``` Optional ```  | Parameter required for using SDP OnDemand Service |
| isFlash |  ``` Optional ```  | Is_Flash is true or false for flash message |
| isUnicode |  ``` Optional ```  | Is_Unicode is true or false for unicode message |
| linkId |  ``` Optional ```  | Parameter required for using SDP OnDemand Service |
| groupId |  ``` Optional ```  | Valid group-id of current user (only for group message otherwise leave empty string) |
| scheduleTime |  ``` Optional ```  | scheduleTime Date in yyyy-MM-dd HH:MM (only for schedule message) |
| serviceId |  ``` Optional ```  | Parameter required for using SDP OnSubscription Service |



#### Example Usage

```python
message = 'Message'
mobile_number = 'MobileNumber'
sender_id = 'SenderId'
co_relator = 'CoRelator'
is_flash = True
is_unicode = True
link_id = 'LinkId'
group_id = 'groupId'
schedule_time = 'scheduleTime'
service_id = 'serviceId'

result = sms_controller.get_create_sms(message, mobile_number, sender_id, co_relator, is_flash, is_unicode, link_id, group_id, schedule_time, service_id)

```


### <a name="create_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_sms") create_sms

> Create SMS

```python
def create_sms(self,
                   message,
                   mobile_number,
                   sender_id,
                   co_relator=None,
                   is_flash=None,
                   is_unicode=None,
                   link_id=None,
                   group_id=None,
                   schedule_time=None,
                   service_id=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| message |  ``` Required ```  | text message to send |
| mobileNumber |  ``` Required ```  | Use mobile number as comma sepreated to send message on multiple mobile number e.g. 78461230,78945612 |
| senderId |  ``` Required ```  | Approved Sender Id |
| coRelator |  ``` Optional ```  | Parameter required for using SDP OnDemand Service |
| isFlash |  ``` Optional ```  | Is_Flash is true or false for flash message |
| isUnicode |  ``` Optional ```  | Is_Unicode is true or false for unicode message |
| linkId |  ``` Optional ```  | Parameter required for using SDP OnDemand Service |
| groupId |  ``` Optional ```  | Valid group-id of current user (only for group message otherwise leave empty string) |
| scheduleTime |  ``` Optional ```  | scheduleTime Date in yyyy-MM-dd HH:MM (only for schedule message) |
| serviceId |  ``` Optional ```  | Parameter required for using SDP OnSubscription Service |



#### Example Usage

```python
message = 'Message'
mobile_number = 'MobileNumber'
sender_id = 'SenderId'
co_relator = 'CoRelator'
is_flash = True
is_unicode = True
link_id = 'LinkId'
group_id = 'groupId'
schedule_time = 'scheduleTime'
service_id = 'serviceId'

result = sms_controller.create_sms(message, mobile_number, sender_id, co_relator, is_flash, is_unicode, link_id, group_id, schedule_time, service_id)

```


### <a name="get_create_bulk_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.get_create_bulk_sms") get_create_bulk_sms

> Create Bulk SMS

```python
def get_create_bulk_sms(self,
                            mobile_number_message,
                            sender_id,
                            co_relator=None,
                            is_flash=None,
                            is_unicode=None,
                            link_id=None,
                            schedule_time=None,
                            service_id=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mobileNumberMessage |  ``` Required ```  | Please ensure while submitting the request the message should be passed in encoded format. e.g. 78461230^test~78945612^hello |
| senderId |  ``` Required ```  | Approved Sender Id |
| coRelator |  ``` Optional ```  | Parameter required for using SDP OnDemand Service |
| isFlash |  ``` Optional ```  | Is_Flash is true or false for flash message |
| isUnicode |  ``` Optional ```  | Is_Unicode is true or false for unicode message |
| linkId |  ``` Optional ```  | Parameter required for using SDP OnDemand Service |
| scheduleTime |  ``` Optional ```  | scheduleTime Date in yyyy-MM-dd HH:MM (only for schedule message) |
| serviceId |  ``` Optional ```  | Parameter required for using SDP OnSubscription Service |



#### Example Usage

```python
mobile_number_message = 'MobileNumber_Message'
sender_id = 'SenderId'
co_relator = 'CoRelator'
is_flash = True
is_unicode = True
link_id = 'LinkId'
schedule_time = datetime.now()
service_id = 'serviceId'

result = sms_controller.get_create_bulk_sms(mobile_number_message, sender_id, co_relator, is_flash, is_unicode, link_id, schedule_time, service_id)

```


### <a name="create_bulk_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_bulk_sms") create_bulk_sms

> Create Bulk SMS

```python
def create_bulk_sms(self,
                        message_parameters,
                        sender_id,
                        is_flash=None,
                        is_unicode=None,
                        schedule_date_time=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageParameters |  ``` Required ```  ``` Collection ```  | TODO: Add a parameter description |
| senderId |  ``` Required ```  | Approved Sender Id |
| isFlash |  ``` Optional ```  | Is_Flash is true or false for flash message |
| isUnicode |  ``` Optional ```  | Is_Unicode is true or false for unicode message |
| scheduleDateTime |  ``` Optional ```  | scheduleTime Date in yyyy-MM-dd HH:MM (only for schedule message) |



#### Example Usage

```python
message_parameters = ['MessageParameters']
sender_id = 'SenderId'
is_flash = True
is_unicode = True
schedule_date_time = datetime.now()

result = sms_controller.create_bulk_sms(message_parameters, sender_id, is_flash, is_unicode, schedule_date_time)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="group_controller"></a>![Class: ](https://apidocs.io/img/class.png ".GROUPController") GROUPController

### Get controller instance

An instance of the ``` GROUPController ``` class can be accessed from the API Client.

```python
 group_controller = client.group
```

### <a name="get_group_list"></a>![Method: ](https://apidocs.io/img/method.png ".GROUPController.get_group_list") get_group_list

> Get Group List

```python
def get_group_list(self)
```

#### Example Usage

```python

result = group_controller.get_group_list()

```


### <a name="create_new_group"></a>![Method: ](https://apidocs.io/img/method.png ".GROUPController.create_new_group") create_new_group

> Create New Group

```python
def create_new_group(self,
                         group_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| groupName |  ``` Required ```  | Name for new group |



#### Example Usage

```python
group_name = 'GroupName'

result = group_controller.create_new_group(group_name)

```


### <a name="update_group"></a>![Method: ](https://apidocs.io/img/method.png ".GROUPController.update_group") update_group

> Update Group

```python
def update_group(self,
                     group_name,
                     id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| groupName |  ``` Required ```  | Name for new group |
| id |  ``` Required ```  | GroupID |



#### Example Usage

```python
group_name = 'GroupName'
id = 'id'

result = group_controller.update_group(group_name, id)

```


### <a name="create_sub_group_group"></a>![Method: ](https://apidocs.io/img/method.png ".GROUPController.create_sub_group_group") create_sub_group_group

> Create Sub-Group Group

```python
def create_sub_group_group(self,
                               group_name,
                               id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| groupName |  ``` Required ```  | Name for new group |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
group_name = 'GroupName'
id = 'Id'

result = group_controller.create_sub_group_group(group_name, id)

```


### <a name="delete_group"></a>![Method: ](https://apidocs.io/img/method.png ".GROUPController.delete_group") delete_group

> Delete Group

```python
def delete_group(self,
                     id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 162

result = group_controller.delete_group(id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="campaign_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CampaignController") CampaignController

### Get controller instance

An instance of the ``` CampaignController ``` class can be accessed from the API Client.

```python
 campaign_controller = client.campaign
```

### <a name="get_campaign_message_status"></a>![Method: ](https://apidocs.io/img/method.png ".CampaignController.get_campaign_message_status") get_campaign_message_status

> Get Campaign Message Status

```python
def get_campaign_message_status(self,
                                    campaign_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| campaignId |  ``` Required ```  | First user have to call Get Campaigns api for CampaignId |



#### Example Usage

```python
campaign_id = 162

result = campaign_controller.get_campaign_message_status(campaign_id)

```


### <a name="get_campaigns"></a>![Method: ](https://apidocs.io/img/method.png ".CampaignController.get_campaigns") get_campaigns

> Get Campaigns

```python
def get_campaigns(self,
                      enddate,
                      fromdate,
                      length,
                      start)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| enddate |  ``` Required ```  | Date format must be in yyyy-mm-dd |
| fromdate |  ``` Required ```  | Date format must be in yyyy-mm-dd |
| length |  ``` Required ```  | Ending index value to fetch the campaign detail. |
| start |  ``` Required ```  | Starting index value to fetch the campaign detail. |



#### Example Usage

```python
enddate = datetime.now()
fromdate = datetime.now()
length = 162
start = 162

result = campaign_controller.get_campaigns(enddate, fromdate, length, start)

```


[Back to List of Controllers](#list_of_controllers)




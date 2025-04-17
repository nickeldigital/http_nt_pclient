# http_nt_pclient.TWAPApi

All URIs are relative to *NT_URL*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TWAPApi.md#create) | **POST** /v1/strategy/twap/{site}/{executionId} | Create twap strategy instance
[**create_multi**](TWAPApi.md#create_multi) | **POST** /v1/strategy/twap/{site} | Create multiple twap strategies
[**replace**](TWAPApi.md#replace) | **PUT** /v1/strategy/twap/{site}/{executionId} | Replace twap strategy instance
[**replace_multi**](TWAPApi.md#replace_multi) | **PUT** /v1/strategy/twap/{site} | Replace multiple twap strategies
[**twap_strategies**](TWAPApi.md#twap_strategies) | **GET** /v1/strategy/twap | Returns list of user strategies
[**twap_strategies_for_site**](TWAPApi.md#twap_strategies_for_site) | **GET** /v1/strategy/twap/{site} | Returns list of user strategies
[**twap_strategy**](TWAPApi.md#twap_strategy) | **GET** /v1/strategy/twap/{site}/{executionId} | Return TWAP strategy
[**update**](TWAPApi.md#update) | **PATCH** /v1/strategy/twap/{site}/{executionId} | Update existing TWAP strategy parameters. Updates only fields provided in request body
[**update_multi**](TWAPApi.md#update_multi) | **PATCH** /v1/strategy/twap/{site} | Update existing multiple TWAP strategy parameters. Updates only fields provided in request body

# **create**
> Twap create(body, site, execution_id)

Create twap strategy instance

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    body = http_nt_pclient.TwapParameters() # TwapParameters | 
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    execution_id = 'execution_id_example' # str | A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters. If an existing identifier is provided, the request will be unsuccessful. 
    try:
        # Create twap strategy instance
        api_response = await api_instance.create(body, site, execution_id)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->create: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TwapParameters**](TwapParameters.md)|  | 
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 
 **execution_id** | **str**| A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters. If an existing identifier is provided, the request will be unsuccessful.  | 

### Return type

[**Twap**](Twap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multi**
> TwapCreateControllerResponse create_multi(body, site)

Create multiple twap strategies

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    body = http_nt_pclient.MultipleTwapParameters() # MultipleTwapParameters | 
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    try:
        # Create multiple twap strategies
        api_response = await api_instance.create_multi(body, site)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->create_multi: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MultipleTwapParameters**](MultipleTwapParameters.md)|  | 
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 

### Return type

[**TwapCreateControllerResponse**](TwapCreateControllerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> TwapReplaceResponse replace(body, site, execution_id)

Replace twap strategy instance

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    body = http_nt_pclient.TwapParameters() # TwapParameters | 
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    execution_id = 'execution_id_example' # str | A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters. If an existing identifier is provided, the current strategy request will overwrite the previously stored strategy. Conversely, if the provided identifier is not found, the request will be unsuccessful. 
    try:
        # Replace twap strategy instance
        api_response = await api_instance.replace(body, site, execution_id)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->replace: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TwapParameters**](TwapParameters.md)|  | 
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 
 **execution_id** | **str**| A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters. If an existing identifier is provided, the current strategy request will overwrite the previously stored strategy. Conversely, if the provided identifier is not found, the request will be unsuccessful.  | 

### Return type

[**TwapReplaceResponse**](TwapReplaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_multi**
> TwapReplaceControllerResponse replace_multi(body, site)

Replace multiple twap strategies

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    body = http_nt_pclient.MultipleTwapParameters() # MultipleTwapParameters | 
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    try:
        # Replace multiple twap strategies
        api_response = await api_instance.replace_multi(body, site)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->replace_multi: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MultipleTwapParameters**](MultipleTwapParameters.md)|  | 
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 

### Return type

[**TwapReplaceControllerResponse**](TwapReplaceControllerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twap_strategies**
> list[TwapWithStatistics] twap_strategies()

Returns list of user strategies

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    try:
        # Returns list of user strategies
        api_response = await api_instance.twap_strategies()
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->twap_strategies: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TwapWithStatistics]**](TwapWithStatistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twap_strategies_for_site**
> list[TwapWithStatistics] twap_strategies_for_site(site)

Returns list of user strategies

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    try:
        # Returns list of user strategies
        api_response = await api_instance.twap_strategies_for_site(site)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->twap_strategies_for_site: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 

### Return type

[**list[TwapWithStatistics]**](TwapWithStatistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twap_strategy**
> TwapWithStatistics twap_strategy(site, execution_id)

Return TWAP strategy

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    execution_id = 'execution_id_example' # str | A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters.
    try:
        # Return TWAP strategy
        api_response = await api_instance.twap_strategy(site, execution_id)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->twap_strategy: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 
 **execution_id** | **str**| A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters. | 

### Return type

[**TwapWithStatistics**](TwapWithStatistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> TwapWithStatistics update(body, site, execution_id)

Update existing TWAP strategy parameters. Updates only fields provided in request body

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    body = http_nt_pclient.TwapUpdateParameters() # TwapUpdateParameters | 
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    execution_id = 'execution_id_example' # str | A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters.
    try:
        # Update existing TWAP strategy parameters. Updates only fields provided in request body
        api_response = await api_instance.update(body, site, execution_id)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->update: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TwapUpdateParameters**](TwapUpdateParameters.md)|  | 
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 
 **execution_id** | **str**| A user-generated unique identifier for the strategy, restricted to a maximum of 8 alphanumerical characters. | 

### Return type

[**TwapWithStatistics**](TwapWithStatistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multi**
> TwapUpdateControllerResponse update_multi(body, site)

Update existing multiple TWAP strategy parameters. Updates only fields provided in request body

### Example
```python
import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint

async def main():
    # Configure HTTP basic authorization: basicAuth
    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration.username = 'API_KEY'
    api_instance.api_client.configuration.password = 'API_SECRET'
    api_instance.api_client.configuration.host = 'NT_URL'
    body = http_nt_pclient.MultipleTwapUpdateParameters() # MultipleTwapUpdateParameters | 
    site = 'site_example' # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites). 
    try:
        # Update existing multiple TWAP strategy parameters. Updates only fields provided in request body
        api_response = await api_instance.update_multi(body, site)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TWAPApi->update_multi: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

if __name__ == '__main__':
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MultipleTwapUpdateParameters**](MultipleTwapUpdateParameters.md)|  | 
 **site** | **str**| Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).  | 

### Return type

[**TwapUpdateControllerResponse**](TwapUpdateControllerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


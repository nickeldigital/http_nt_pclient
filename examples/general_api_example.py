import asyncio
import http_nt_pclient
from http_nt_pclient.rest import ApiException
from pprint import pprint


async def main():
    # Configure HTTP basic authorization: basicAuth
    config = http_nt_pclient.Configuration()
    config.username = None  # Add username
    config.password = None  # Add password
    config.host = None  # Add target host

    assert config.username, 'INVALID USERNAME'
    assert config.password, 'INVALID PASSWORD'
    assert config.host, 'INVALID HOST'

    api_instance = http_nt_pclient.GeneralApi()
    api_instance.api_client.configuration = config

    try:
        # Returns list of available Nickel Trader instances (sites)
        api_response = await api_instance.sites()
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling GeneralApi->sites: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

    site = 'Ext-Tokyo-1'  # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).
    account_id = 'account_id_example'  # str | An exchange account id
    exchange = 'BINANCE_FUTURES_USDT'  # str | Exchange, see [/v1/exchanges](#/General/exchanges)

    try:
        # Returns list of available exchanges
        api_response = await api_instance.exchanges(site)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling GeneralApi->exchanges: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

    try:
        # Returns a list of the exposures
        api_response = await api_instance.exposures_for_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling GeneralApi->exposures: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

    try:
        # Returns a list of the exposures
        api_response = await api_instance.exposures()
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling GeneralApi->exposures: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

    try:
        # Returns list of available instruments
        api_response = await api_instance.instruments(site, exchange)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling GeneralApi->instruments: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()

    try:
        # Returns user limits
        api_response = await api_instance.limits(site, exchange, account_id)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling GeneralApi->limits: {e}\n")
    finally:
        # Explicitly close the session
        await api_instance.api_client.rest_client.pool_manager.close()


if __name__ == '__main__':
    asyncio.run(main())

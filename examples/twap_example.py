import asyncio
import datetime
import http_nt_pclient
from http_nt_pclient.rest import ApiException


async def get_strategies(api_instance):
    try:
        api_response = await api_instance.twap_strategies()
        print(f"Strategies Response: {api_response}")
    except ApiException as e:
        print(f"Exception when calling TwapApi->twap_strategies: {e}\n")
        raise e


async def single_example(api_instance, site, instrument, account, execution_id):
    params = http_nt_pclient.TwapParameters(
        instrument=instrument,
        account=account,
        side='BUY',
        target=0.01,
        guaranteed_execution='NO',
        scheduled_start_time=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=60),
        aggression_cap=1,
        aggression_floor=0,
        step_size=0.01,
        step_time=1,
    )

    try:
        api_response = await api_instance.create(params, site, execution_id)
        print(f"Create TWAP Response: {api_response}")
    except ApiException as e:
        print(f"Exception when calling TwapApi->create: {e}\n")
        raise e

    update_dict = params.to_dict()
    update_dict['target'] = 0.011
    update_params = http_nt_pclient.TwapUpdateParameters(**update_dict)

    try:
        api_response = await api_instance.update(update_params, site, execution_id)
        print(f"Update TWAP Response: {api_response}")
    except ApiException as e:
        print(f"Exception when calling TwapApi->update: {e}\n")
        raise e


async def multi_example(api_instance, site, instrument, account, execution_id):
    multi_params = http_nt_pclient.MultipleTwapParameters(twaps=[
        http_nt_pclient.TwapParametersWithId(
            execution_id=execution_id,
            parameters=http_nt_pclient.TwapParameters(
                instrument=instrument,
                account=account,
                side='SELL',
                target=0.1,
                guaranteed_execution='NO',
                scheduled_start_time=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=60),
                aggression_cap=1,
                aggression_floor=0,
                step_size=0.01,
                step_time=1
            ))
    ])

    try:
        api_response = await api_instance.create_multi(multi_params, site)
        print(f"Create Multiple TWAPs Response: {api_response}")
    except ApiException as e:
        print(f"Exception when calling TwapApi->create: {e}\n")
        raise e

    multi_updates = []
    for t in multi_params.twaps:
        exec_id = t.execution_id
        t.parameters.target = 0.11
        m_dict = t.parameters.to_dict()
        multi_updates.append(http_nt_pclient.TwapUpdateParametersWithId(
            execution_id=exec_id, parameters_to_update=http_nt_pclient.TwapUpdateParameters(**m_dict))
        )
    multi_update_params = http_nt_pclient.MultipleTwapUpdateParameters(updates=multi_updates)

    try:
        api_response = await api_instance.update_multi(multi_update_params, site)
        print(f"Update Multiple TWAPs Response: {api_response}")
        for issue in api_response.issues:
            print("ISSUE:", issue)
    except ApiException as e:
        print(f"Exception when calling TwapApi->update_multi: {e}\n")
        raise e


async def main():
    config = http_nt_pclient.Configuration()
    config.username = None  # Add username
    config.password = None  # Add password
    config.host = None      # Add target host

    assert config.username, 'INVALID USERNAME'
    assert config.password, 'INVALID PASSWORD'
    assert config.host, 'INVALID HOST'

    api_instance = http_nt_pclient.TWAPApi()
    api_instance.api_client.configuration = config

    site = 'Ext-Tokyo-UAT'  # str | Instance of Nickel Trader used for the execution. One or more can be available. For the list of available sites, query [/v1/sites](#/General/sites).
    account_id = 'account_id_example'  # str | An exchange account id
    exchange = 'BINANCE_FUTURES_USDT'  # str | Exchange, see [/v1/exchanges](#/General/exchanges)
    symbol = 'BTCUSDT'

    try:
        await get_strategies(api_instance)
        await single_example(api_instance, site, f'{symbol}@{exchange}', account_id, 'excID1')
        await multi_example(api_instance, site, f'{symbol}@{exchange}', account_id, 'excID11')
    finally:
        await api_instance.api_client.rest_client.pool_manager.close()


if __name__ == '__main__':
    asyncio.run(main())

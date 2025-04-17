# TwapParametersWithStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account to trade. For the list of avaialble accounts, query [/v1/exchanges](#/General/exchanges). Only settable for an existing strategy when in state NEW  | 
**aggression_cap** | **float** | Distance from the current step&#x27;s target when aggressive execution stops and passive execution continues. Expressed in percentage points of the full quantity target. Used in conjunction with aggressionFloor. Must be within [0,100] or, most strictly, [0, aggressionFloor]. Set to 0 for aggressive execution all the way to the current step&#x27;s target. Set close to aggressionFloor for minimal but frequent taker execution. Settable for an existing strategy in all states. | 
**aggression_floor** | **float** | Distance from the current step&#x27;s target when aggressive execution takes over. Expressed in percentage points of the full quantity target. Used in conjunction with aggressionCap, and should be set close to aggressionCap to avoid large taker orders when passive execution is lagging behind the current step&#x27;s target. Must be within [0,100] or, most strictly, [aggressionCap, 100]. Set to 0 for taker-only execution. Set to 100 for maker-only execution. Settable for an existing strategy in all states. | 
**bbo_spread_limit** | **int** | Optional limit for max BBO spread. Settable for an existing strategy in all states. | [optional] 
**guaranteed_execution** | **str** | Ensure complete execution within scheduled execution period by executing more taker orders towards the end of the execution window (TRUE), or continue to quote the final slice until it&#x27;s taken (FALSE). Settable for an existing strategy in all states. | 
**instrument** | **str** | Instrument to trade, following symbol@exchange convention. For the list of avaialble instruments, query [/v1/instruments](#/General/instruments). Only settable for an existing strategy when in state NEW.  | 
**limit_price** | **float** | Optional limit price. Settable for an existing strategy in all states. | [optional] 
**max_display_size** | **float** | The maximum quantity that can be quoted in the orderbook at any one time. Settable for an existing strategy in non RUNNING state. | [optional] 
**scheduled_start_time** | **datetime** | TWAP will start automatically at given start time. Only settable for an existing strategy in state NEW. | [optional] 
**scheduled_stop_time** | **datetime** | TWAP will stop automatically at given stop time. Only settable for an existing strategy in state NEW or STOPPED. | [optional] 
**side** | **str** | Side to trade: can be buy or sell. Required when specifying a target, but overridden if using targetPosition. Only settable for an existing strategy when in state NEW or STOPPED. | 
**start** | **bool** | Start strategy execution immediately after submit. | [optional] [default to False]
**statistics** | [**TwapStatistics**](TwapStatistics.md) |  | [optional] 
**step_size** | **float** | The average increment of each step of TWAP execution (subject to randomisation). Only settable for an existing strategy in state NEW or STOPPED. | 
**step_time** | **int** | The average time delay in seconds between each step of TWAP execution. Required if no scheduledStartTime is provided. Only settable for an existing strategy in state NEW or STOPPED. | [optional] 
**target** | **float** | Full quantity of the base asset to trade. The strategy will stop when target is reached. Only settable for an existing strategy in state NEW or STOPPED. Cannot be set together with targetPosition. | [optional] 
**target_position** | **float** | Signed position size following successful execution of the trading algorithm. Only settable for an existing strategy in state NEW or STOPPED. Cannot be set together with target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


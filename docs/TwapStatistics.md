# TwapStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_execution_price** | **float** | Average price of filled orders (filled amount / filled qty). | [optional] 
**bbo_tick_width** | **int** | The current width between the Best Bid and Best Offer in ticks. | [optional] 
**behind** | **float** | (quoted-traded) / target, behind &#x3D; 0% means execution is on track, behind &gt; 0% means execution is slower. | [optional] 
**initial_best_bid** | **float** | Initial best bid | [optional] 
**initial_best_offer** | **float** | Initial best offer | [optional] 
**progress** | **float** | Traded / target percentage. | [optional] 
**quoted** | **float** | Total quantity of filled and open (submitted) orders, increasing on each TWAP step. | [optional] 
**traded** | **float** | Total quantity of filled orders. | [optional] 
**twap_price** | **float** | Average order book mid price during the execution (sampled on 1sec intervals). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


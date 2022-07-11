import sgqlc.types


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class Account_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'gaugeWeightVotes', 'gauges', 'id', 'proposalVotes', 'proposals')


class AddLiquidityEvent_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'fees', 'id', 'invariant', 'pool', 'provider', 'timestamp', 'tokenAmounts', 'tokenSupply', 'transaction')


class AdminFeeChangelog_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'id', 'pool', 'timestamp', 'transaction', 'value')


class AmplificationCoeffChangelog_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'id', 'pool', 'timestamp', 'transaction', 'value')


class AssetType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('BTC', 'CRYPTO', 'ETH', 'EUR', 'LINK', 'OTHER', 'USD')


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Boolean = sgqlc.types.Boolean

class Bytes(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class Coin_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('balance', 'id', 'index', 'pool', 'rate', 'token', 'underlying', 'updated', 'updatedAtBlock', 'updatedAtTransaction')


class ContractVersion_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('added', 'addedAtBlock', 'addedAtTransaction', 'address', 'contract', 'id', 'version')


class Contract_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('added', 'addedAtBlock', 'addedAtTransaction', 'description', 'id', 'modified', 'modifiedAtBlock', 'modifiedAtTransaction', 'versions')


class DailyVolume_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'pool', 'timestamp', 'volume')


class Exchange_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amountBought', 'amountSold', 'block', 'buyer', 'id', 'pool', 'receiver', 'timestamp', 'tokenBought', 'tokenSold', 'transaction')


class FeeChangelog_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'id', 'pool', 'timestamp', 'transaction', 'value')


Float = sgqlc.types.Float

class GaugeDeposit_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('gauge', 'id', 'provider', 'value')


class GaugeLiquidity_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'gauge', 'id', 'originalBalance', 'originalSupply', 'timestamp', 'transaction', 'user', 'workingBalance', 'workingSupply')


class GaugeTotalWeight_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'time', 'weight')


class GaugeTypeWeight_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'time', 'type', 'weight')


class GaugeType_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('gaugeCount', 'gauges', 'id', 'name', 'weights')


class GaugeWeightVote_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('gauge', 'id', 'time', 'user', 'weight')


class GaugeWeight_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('gauge', 'id', 'time', 'weight')


class GaugeWithdraw_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('gauge', 'id', 'provider', 'value')


class Gauge_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'created', 'createdAtBlock', 'createdAtTransaction', 'id', 'pool', 'type', 'weightVotes', 'weights')


class HourlyVolume_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'pool', 'timestamp', 'volume')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class LpToken_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'decimals', 'gauge', 'id', 'name', 'pool', 'symbol')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asc', 'desc')


class PoolEvent_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'pool', 'timestamp', 'transaction')


class Pool_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('A', 'addedAt', 'addedAtBlock', 'addedAtTransaction', 'adminFee', 'assetType', 'coinCount', 'coins', 'dailyVolumes', 'events', 'exchangeCount', 'exchanges', 'fee', 'gaugeCount', 'gauges', 'hourlyVolumes', 'id', 'isMeta', 'locked', 'lpToken', 'name', 'owner', 'registryAddress', 'removedAt', 'removedAtBlock', 'removedAtTransaction', 'swapAddress', 'underlyingCoins', 'underlyingCount', 'virtualPrice', 'weeklyVolumes')


class ProposalVote_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('created', 'createdAtBlock', 'createdAtTransaction', 'id', 'proposal', 'stake', 'supports', 'voter')


class Proposal_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('app', 'created', 'createdAtBlock', 'createdAtTransaction', 'creator', 'currentQuorum', 'currentSupport', 'executed', 'executedAtBlock', 'executedAtTransaction', 'executionScript', 'expireDate', 'id', 'metadata', 'minimumQuorum', 'negativeVoteCount', 'number', 'positiveVoteCount', 'requiredSupport', 'snapshotBlock', 'stakedSupport', 'text', 'totalStaked', 'updated', 'updatedAtBlock', 'updatedAtTransaction', 'voteCount', 'votes', 'votingPower')


class RemoveLiquidityEvent_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'fees', 'id', 'invariant', 'pool', 'provider', 'timestamp', 'tokenAmounts', 'tokenSupply', 'transaction')


class RemoveLiquidityOneEvent_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'coinAmount', 'id', 'pool', 'provider', 'timestamp', 'tokenAmount', 'transaction')


String = sgqlc.types.String

class SystemState_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('contractCount', 'gaugeCount', 'gaugeTypeCount', 'id', 'poolCount', 'registryContract', 'tokenCount', 'totalPoolCount', 'updated', 'updatedAtBlock', 'updatedAtTransaction')


class Token_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'coins', 'decimals', 'id', 'name', 'pools', 'symbol', 'underlyingCoins')


class TradeVolume_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('pool', 'timestamp', 'volume')


class TransferOwnershipEvent_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'id', 'newAdmin', 'pool', 'timestamp', 'transaction')


class UnderlyingCoin_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('balance', 'coin', 'id', 'index', 'pool', 'token', 'updated', 'updatedAtBlock', 'updatedAtTransaction')


class VotingApp_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'codename', 'id', 'minimumBalance', 'minimumQuorum', 'minimumTime', 'proposalCount', 'proposals', 'requiredSupport', 'token', 'voteCount', 'voteTime')


class WeeklyVolume_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'pool', 'timestamp', 'volume')


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('allow', 'deny')



########################################################################
# Input Objects
########################################################################
class Account_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'gauges_', 'gauge_weight_votes_', 'proposals_', 'proposal_votes_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    gauges_ = sgqlc.types.Field('GaugeLiquidity_filter', graphql_name='gauges_')
    gauge_weight_votes_ = sgqlc.types.Field('GaugeWeightVote_filter', graphql_name='gaugeWeightVotes_')
    proposals_ = sgqlc.types.Field('Proposal_filter', graphql_name='proposals_')
    proposal_votes_ = sgqlc.types.Field('ProposalVote_filter', graphql_name='proposalVotes_')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')


class AddLiquidityEvent_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'provider', 'provider_not', 'provider_gt', 'provider_lt', 'provider_gte', 'provider_lte', 'provider_in', 'provider_not_in', 'provider_contains', 'provider_contains_nocase', 'provider_not_contains', 'provider_not_contains_nocase', 'provider_starts_with', 'provider_starts_with_nocase', 'provider_not_starts_with', 'provider_not_starts_with_nocase', 'provider_ends_with', 'provider_ends_with_nocase', 'provider_not_ends_with', 'provider_not_ends_with_nocase', 'provider_', 'token_amounts', 'token_amounts_not', 'token_amounts_contains', 'token_amounts_contains_nocase', 'token_amounts_not_contains', 'token_amounts_not_contains_nocase', 'fees', 'fees_not', 'fees_contains', 'fees_contains_nocase', 'fees_not_contains', 'fees_not_contains_nocase', 'invariant', 'invariant_not', 'invariant_gt', 'invariant_lt', 'invariant_gte', 'invariant_lte', 'invariant_in', 'invariant_not_in', 'token_supply', 'token_supply_not', 'token_supply_gt', 'token_supply_lt', 'token_supply_gte', 'token_supply_lte', 'token_supply_in', 'token_supply_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    provider = sgqlc.types.Field(String, graphql_name='provider')
    provider_not = sgqlc.types.Field(String, graphql_name='provider_not')
    provider_gt = sgqlc.types.Field(String, graphql_name='provider_gt')
    provider_lt = sgqlc.types.Field(String, graphql_name='provider_lt')
    provider_gte = sgqlc.types.Field(String, graphql_name='provider_gte')
    provider_lte = sgqlc.types.Field(String, graphql_name='provider_lte')
    provider_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_in')
    provider_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_not_in')
    provider_contains = sgqlc.types.Field(String, graphql_name='provider_contains')
    provider_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_contains_nocase')
    provider_not_contains = sgqlc.types.Field(String, graphql_name='provider_not_contains')
    provider_not_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_not_contains_nocase')
    provider_starts_with = sgqlc.types.Field(String, graphql_name='provider_starts_with')
    provider_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_starts_with_nocase')
    provider_not_starts_with = sgqlc.types.Field(String, graphql_name='provider_not_starts_with')
    provider_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_starts_with_nocase')
    provider_ends_with = sgqlc.types.Field(String, graphql_name='provider_ends_with')
    provider_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_ends_with_nocase')
    provider_not_ends_with = sgqlc.types.Field(String, graphql_name='provider_not_ends_with')
    provider_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_ends_with_nocase')
    provider_ = sgqlc.types.Field(Account_filter, graphql_name='provider_')
    token_amounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts')
    token_amounts_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_not')
    token_amounts_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_contains')
    token_amounts_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_contains_nocase')
    token_amounts_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_not_contains')
    token_amounts_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_not_contains_nocase')
    fees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees')
    fees_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_not')
    fees_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_contains')
    fees_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_contains_nocase')
    fees_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_not_contains')
    fees_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_not_contains_nocase')
    invariant = sgqlc.types.Field(BigInt, graphql_name='invariant')
    invariant_not = sgqlc.types.Field(BigInt, graphql_name='invariant_not')
    invariant_gt = sgqlc.types.Field(BigInt, graphql_name='invariant_gt')
    invariant_lt = sgqlc.types.Field(BigInt, graphql_name='invariant_lt')
    invariant_gte = sgqlc.types.Field(BigInt, graphql_name='invariant_gte')
    invariant_lte = sgqlc.types.Field(BigInt, graphql_name='invariant_lte')
    invariant_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='invariant_in')
    invariant_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='invariant_not_in')
    token_supply = sgqlc.types.Field(BigInt, graphql_name='tokenSupply')
    token_supply_not = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_not')
    token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_gt')
    token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_lt')
    token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_gte')
    token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_lte')
    token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenSupply_in')
    token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenSupply_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')


class AdminFeeChangelog_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'value', 'value_not', 'value_gt', 'value_lt', 'value_gte', 'value_lte', 'value_in', 'value_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    value = sgqlc.types.Field(BigDecimal, graphql_name='value')
    value_not = sgqlc.types.Field(BigDecimal, graphql_name='value_not')
    value_gt = sgqlc.types.Field(BigDecimal, graphql_name='value_gt')
    value_lt = sgqlc.types.Field(BigDecimal, graphql_name='value_lt')
    value_gte = sgqlc.types.Field(BigDecimal, graphql_name='value_gte')
    value_lte = sgqlc.types.Field(BigDecimal, graphql_name='value_lte')
    value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_in')
    value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')


class AmplificationCoeffChangelog_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'value', 'value_not', 'value_gt', 'value_lt', 'value_gte', 'value_lte', 'value_in', 'value_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    value = sgqlc.types.Field(BigInt, graphql_name='value')
    value_not = sgqlc.types.Field(BigInt, graphql_name='value_not')
    value_gt = sgqlc.types.Field(BigInt, graphql_name='value_gt')
    value_lt = sgqlc.types.Field(BigInt, graphql_name='value_lt')
    value_gte = sgqlc.types.Field(BigInt, graphql_name='value_gte')
    value_lte = sgqlc.types.Field(BigInt, graphql_name='value_lte')
    value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='value_in')
    value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='value_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')


class BlockChangedFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('number_gte',)
    number_gte = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number_gte')


class Block_height(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number', 'number_gte')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(Int, graphql_name='number')
    number_gte = sgqlc.types.Field(Int, graphql_name='number_gte')


class Coin_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'index', 'index_not', 'index_gt', 'index_lt', 'index_gte', 'index_lte', 'index_in', 'index_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'underlying', 'underlying_not', 'underlying_gt', 'underlying_lt', 'underlying_gte', 'underlying_lte', 'underlying_in', 'underlying_not_in', 'underlying_contains', 'underlying_contains_nocase', 'underlying_not_contains', 'underlying_not_contains_nocase', 'underlying_starts_with', 'underlying_starts_with_nocase', 'underlying_not_starts_with', 'underlying_not_starts_with_nocase', 'underlying_ends_with', 'underlying_ends_with_nocase', 'underlying_not_ends_with', 'underlying_not_ends_with_nocase', 'underlying_', 'balance', 'balance_not', 'balance_gt', 'balance_lt', 'balance_gte', 'balance_lte', 'balance_in', 'balance_not_in', 'rate', 'rate_not', 'rate_gt', 'rate_lt', 'rate_gte', 'rate_lte', 'rate_in', 'rate_not_in', 'updated', 'updated_not', 'updated_gt', 'updated_lt', 'updated_gte', 'updated_lte', 'updated_in', 'updated_not_in', 'updated_at_block', 'updated_at_block_not', 'updated_at_block_gt', 'updated_at_block_lt', 'updated_at_block_gte', 'updated_at_block_lte', 'updated_at_block_in', 'updated_at_block_not_in', 'updated_at_transaction', 'updated_at_transaction_not', 'updated_at_transaction_in', 'updated_at_transaction_not_in', 'updated_at_transaction_contains', 'updated_at_transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    index = sgqlc.types.Field(Int, graphql_name='index')
    index_not = sgqlc.types.Field(Int, graphql_name='index_not')
    index_gt = sgqlc.types.Field(Int, graphql_name='index_gt')
    index_lt = sgqlc.types.Field(Int, graphql_name='index_lt')
    index_gte = sgqlc.types.Field(Int, graphql_name='index_gte')
    index_lte = sgqlc.types.Field(Int, graphql_name='index_lte')
    index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='index_in')
    index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='index_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    token = sgqlc.types.Field(String, graphql_name='token')
    token_not = sgqlc.types.Field(String, graphql_name='token_not')
    token_gt = sgqlc.types.Field(String, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(String, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(String, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(String, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(String, graphql_name='token_contains')
    token_contains_nocase = sgqlc.types.Field(String, graphql_name='token_contains_nocase')
    token_not_contains = sgqlc.types.Field(String, graphql_name='token_not_contains')
    token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token_not_contains_nocase')
    token_starts_with = sgqlc.types.Field(String, graphql_name='token_starts_with')
    token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_starts_with_nocase')
    token_not_starts_with = sgqlc.types.Field(String, graphql_name='token_not_starts_with')
    token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_starts_with_nocase')
    token_ends_with = sgqlc.types.Field(String, graphql_name='token_ends_with')
    token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_ends_with_nocase')
    token_not_ends_with = sgqlc.types.Field(String, graphql_name='token_not_ends_with')
    token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_ends_with_nocase')
    token_ = sgqlc.types.Field('Token_filter', graphql_name='token_')
    underlying = sgqlc.types.Field(String, graphql_name='underlying')
    underlying_not = sgqlc.types.Field(String, graphql_name='underlying_not')
    underlying_gt = sgqlc.types.Field(String, graphql_name='underlying_gt')
    underlying_lt = sgqlc.types.Field(String, graphql_name='underlying_lt')
    underlying_gte = sgqlc.types.Field(String, graphql_name='underlying_gte')
    underlying_lte = sgqlc.types.Field(String, graphql_name='underlying_lte')
    underlying_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='underlying_in')
    underlying_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='underlying_not_in')
    underlying_contains = sgqlc.types.Field(String, graphql_name='underlying_contains')
    underlying_contains_nocase = sgqlc.types.Field(String, graphql_name='underlying_contains_nocase')
    underlying_not_contains = sgqlc.types.Field(String, graphql_name='underlying_not_contains')
    underlying_not_contains_nocase = sgqlc.types.Field(String, graphql_name='underlying_not_contains_nocase')
    underlying_starts_with = sgqlc.types.Field(String, graphql_name='underlying_starts_with')
    underlying_starts_with_nocase = sgqlc.types.Field(String, graphql_name='underlying_starts_with_nocase')
    underlying_not_starts_with = sgqlc.types.Field(String, graphql_name='underlying_not_starts_with')
    underlying_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='underlying_not_starts_with_nocase')
    underlying_ends_with = sgqlc.types.Field(String, graphql_name='underlying_ends_with')
    underlying_ends_with_nocase = sgqlc.types.Field(String, graphql_name='underlying_ends_with_nocase')
    underlying_not_ends_with = sgqlc.types.Field(String, graphql_name='underlying_not_ends_with')
    underlying_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='underlying_not_ends_with_nocase')
    underlying_ = sgqlc.types.Field('UnderlyingCoin_filter', graphql_name='underlying_')
    balance = sgqlc.types.Field(BigDecimal, graphql_name='balance')
    balance_not = sgqlc.types.Field(BigDecimal, graphql_name='balance_not')
    balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='balance_gt')
    balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='balance_lt')
    balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='balance_gte')
    balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='balance_lte')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_in')
    balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_not_in')
    rate = sgqlc.types.Field(BigDecimal, graphql_name='rate')
    rate_not = sgqlc.types.Field(BigDecimal, graphql_name='rate_not')
    rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='rate_gt')
    rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='rate_lt')
    rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='rate_gte')
    rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='rate_lte')
    rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rate_in')
    rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rate_not_in')
    updated = sgqlc.types.Field(BigInt, graphql_name='updated')
    updated_not = sgqlc.types.Field(BigInt, graphql_name='updated_not')
    updated_gt = sgqlc.types.Field(BigInt, graphql_name='updated_gt')
    updated_lt = sgqlc.types.Field(BigInt, graphql_name='updated_lt')
    updated_gte = sgqlc.types.Field(BigInt, graphql_name='updated_gte')
    updated_lte = sgqlc.types.Field(BigInt, graphql_name='updated_lte')
    updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_in')
    updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_not_in')
    updated_at_block = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock')
    updated_at_block_not = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_not')
    updated_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gt')
    updated_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lt')
    updated_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gte')
    updated_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lte')
    updated_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_in')
    updated_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_not_in')
    updated_at_transaction = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction')
    updated_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not')
    updated_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_in')
    updated_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_not_in')
    updated_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_contains')
    updated_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class ContractVersion_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'contract', 'contract_not', 'contract_gt', 'contract_lt', 'contract_gte', 'contract_lte', 'contract_in', 'contract_not_in', 'contract_contains', 'contract_contains_nocase', 'contract_not_contains', 'contract_not_contains_nocase', 'contract_starts_with', 'contract_starts_with_nocase', 'contract_not_starts_with', 'contract_not_starts_with_nocase', 'contract_ends_with', 'contract_ends_with_nocase', 'contract_not_ends_with', 'contract_not_ends_with_nocase', 'contract_', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'version', 'version_not', 'version_gt', 'version_lt', 'version_gte', 'version_lte', 'version_in', 'version_not_in', 'added', 'added_not', 'added_gt', 'added_lt', 'added_gte', 'added_lte', 'added_in', 'added_not_in', 'added_at_block', 'added_at_block_not', 'added_at_block_gt', 'added_at_block_lt', 'added_at_block_gte', 'added_at_block_lte', 'added_at_block_in', 'added_at_block_not_in', 'added_at_transaction', 'added_at_transaction_not', 'added_at_transaction_in', 'added_at_transaction_not_in', 'added_at_transaction_contains', 'added_at_transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    contract = sgqlc.types.Field(String, graphql_name='contract')
    contract_not = sgqlc.types.Field(String, graphql_name='contract_not')
    contract_gt = sgqlc.types.Field(String, graphql_name='contract_gt')
    contract_lt = sgqlc.types.Field(String, graphql_name='contract_lt')
    contract_gte = sgqlc.types.Field(String, graphql_name='contract_gte')
    contract_lte = sgqlc.types.Field(String, graphql_name='contract_lte')
    contract_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='contract_in')
    contract_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='contract_not_in')
    contract_contains = sgqlc.types.Field(String, graphql_name='contract_contains')
    contract_contains_nocase = sgqlc.types.Field(String, graphql_name='contract_contains_nocase')
    contract_not_contains = sgqlc.types.Field(String, graphql_name='contract_not_contains')
    contract_not_contains_nocase = sgqlc.types.Field(String, graphql_name='contract_not_contains_nocase')
    contract_starts_with = sgqlc.types.Field(String, graphql_name='contract_starts_with')
    contract_starts_with_nocase = sgqlc.types.Field(String, graphql_name='contract_starts_with_nocase')
    contract_not_starts_with = sgqlc.types.Field(String, graphql_name='contract_not_starts_with')
    contract_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='contract_not_starts_with_nocase')
    contract_ends_with = sgqlc.types.Field(String, graphql_name='contract_ends_with')
    contract_ends_with_nocase = sgqlc.types.Field(String, graphql_name='contract_ends_with_nocase')
    contract_not_ends_with = sgqlc.types.Field(String, graphql_name='contract_not_ends_with')
    contract_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='contract_not_ends_with_nocase')
    contract_ = sgqlc.types.Field('Contract_filter', graphql_name='contract_')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    version = sgqlc.types.Field(BigInt, graphql_name='version')
    version_not = sgqlc.types.Field(BigInt, graphql_name='version_not')
    version_gt = sgqlc.types.Field(BigInt, graphql_name='version_gt')
    version_lt = sgqlc.types.Field(BigInt, graphql_name='version_lt')
    version_gte = sgqlc.types.Field(BigInt, graphql_name='version_gte')
    version_lte = sgqlc.types.Field(BigInt, graphql_name='version_lte')
    version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='version_in')
    version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='version_not_in')
    added = sgqlc.types.Field(BigInt, graphql_name='added')
    added_not = sgqlc.types.Field(BigInt, graphql_name='added_not')
    added_gt = sgqlc.types.Field(BigInt, graphql_name='added_gt')
    added_lt = sgqlc.types.Field(BigInt, graphql_name='added_lt')
    added_gte = sgqlc.types.Field(BigInt, graphql_name='added_gte')
    added_lte = sgqlc.types.Field(BigInt, graphql_name='added_lte')
    added_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='added_in')
    added_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='added_not_in')
    added_at_block = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock')
    added_at_block_not = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_not')
    added_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_gt')
    added_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_lt')
    added_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_gte')
    added_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_lte')
    added_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAtBlock_in')
    added_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAtBlock_not_in')
    added_at_transaction = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction')
    added_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_not')
    added_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='addedAtTransaction_in')
    added_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='addedAtTransaction_not_in')
    added_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_contains')
    added_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Contract_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'description', 'description_not', 'description_gt', 'description_lt', 'description_gte', 'description_lte', 'description_in', 'description_not_in', 'description_contains', 'description_contains_nocase', 'description_not_contains', 'description_not_contains_nocase', 'description_starts_with', 'description_starts_with_nocase', 'description_not_starts_with', 'description_not_starts_with_nocase', 'description_ends_with', 'description_ends_with_nocase', 'description_not_ends_with', 'description_not_ends_with_nocase', 'added', 'added_not', 'added_gt', 'added_lt', 'added_gte', 'added_lte', 'added_in', 'added_not_in', 'added_at_block', 'added_at_block_not', 'added_at_block_gt', 'added_at_block_lt', 'added_at_block_gte', 'added_at_block_lte', 'added_at_block_in', 'added_at_block_not_in', 'added_at_transaction', 'added_at_transaction_not', 'added_at_transaction_in', 'added_at_transaction_not_in', 'added_at_transaction_contains', 'added_at_transaction_not_contains', 'modified', 'modified_not', 'modified_gt', 'modified_lt', 'modified_gte', 'modified_lte', 'modified_in', 'modified_not_in', 'modified_at_block', 'modified_at_block_not', 'modified_at_block_gt', 'modified_at_block_lt', 'modified_at_block_gte', 'modified_at_block_lte', 'modified_at_block_in', 'modified_at_block_not_in', 'modified_at_transaction', 'modified_at_transaction_not', 'modified_at_transaction_in', 'modified_at_transaction_not_in', 'modified_at_transaction_contains', 'modified_at_transaction_not_contains', 'versions_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_not = sgqlc.types.Field(String, graphql_name='description_not')
    description_gt = sgqlc.types.Field(String, graphql_name='description_gt')
    description_lt = sgqlc.types.Field(String, graphql_name='description_lt')
    description_gte = sgqlc.types.Field(String, graphql_name='description_gte')
    description_lte = sgqlc.types.Field(String, graphql_name='description_lte')
    description_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='description_in')
    description_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='description_not_in')
    description_contains = sgqlc.types.Field(String, graphql_name='description_contains')
    description_contains_nocase = sgqlc.types.Field(String, graphql_name='description_contains_nocase')
    description_not_contains = sgqlc.types.Field(String, graphql_name='description_not_contains')
    description_not_contains_nocase = sgqlc.types.Field(String, graphql_name='description_not_contains_nocase')
    description_starts_with = sgqlc.types.Field(String, graphql_name='description_starts_with')
    description_starts_with_nocase = sgqlc.types.Field(String, graphql_name='description_starts_with_nocase')
    description_not_starts_with = sgqlc.types.Field(String, graphql_name='description_not_starts_with')
    description_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='description_not_starts_with_nocase')
    description_ends_with = sgqlc.types.Field(String, graphql_name='description_ends_with')
    description_ends_with_nocase = sgqlc.types.Field(String, graphql_name='description_ends_with_nocase')
    description_not_ends_with = sgqlc.types.Field(String, graphql_name='description_not_ends_with')
    description_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='description_not_ends_with_nocase')
    added = sgqlc.types.Field(BigInt, graphql_name='added')
    added_not = sgqlc.types.Field(BigInt, graphql_name='added_not')
    added_gt = sgqlc.types.Field(BigInt, graphql_name='added_gt')
    added_lt = sgqlc.types.Field(BigInt, graphql_name='added_lt')
    added_gte = sgqlc.types.Field(BigInt, graphql_name='added_gte')
    added_lte = sgqlc.types.Field(BigInt, graphql_name='added_lte')
    added_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='added_in')
    added_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='added_not_in')
    added_at_block = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock')
    added_at_block_not = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_not')
    added_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_gt')
    added_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_lt')
    added_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_gte')
    added_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_lte')
    added_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAtBlock_in')
    added_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAtBlock_not_in')
    added_at_transaction = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction')
    added_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_not')
    added_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='addedAtTransaction_in')
    added_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='addedAtTransaction_not_in')
    added_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_contains')
    added_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_not_contains')
    modified = sgqlc.types.Field(BigInt, graphql_name='modified')
    modified_not = sgqlc.types.Field(BigInt, graphql_name='modified_not')
    modified_gt = sgqlc.types.Field(BigInt, graphql_name='modified_gt')
    modified_lt = sgqlc.types.Field(BigInt, graphql_name='modified_lt')
    modified_gte = sgqlc.types.Field(BigInt, graphql_name='modified_gte')
    modified_lte = sgqlc.types.Field(BigInt, graphql_name='modified_lte')
    modified_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='modified_in')
    modified_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='modified_not_in')
    modified_at_block = sgqlc.types.Field(BigInt, graphql_name='modifiedAtBlock')
    modified_at_block_not = sgqlc.types.Field(BigInt, graphql_name='modifiedAtBlock_not')
    modified_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='modifiedAtBlock_gt')
    modified_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='modifiedAtBlock_lt')
    modified_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='modifiedAtBlock_gte')
    modified_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='modifiedAtBlock_lte')
    modified_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='modifiedAtBlock_in')
    modified_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='modifiedAtBlock_not_in')
    modified_at_transaction = sgqlc.types.Field(Bytes, graphql_name='modifiedAtTransaction')
    modified_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='modifiedAtTransaction_not')
    modified_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='modifiedAtTransaction_in')
    modified_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='modifiedAtTransaction_not_in')
    modified_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='modifiedAtTransaction_contains')
    modified_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='modifiedAtTransaction_not_contains')
    versions_ = sgqlc.types.Field(ContractVersion_filter, graphql_name='versions_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class DailyVolume_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Exchange_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'buyer', 'buyer_not', 'buyer_gt', 'buyer_lt', 'buyer_gte', 'buyer_lte', 'buyer_in', 'buyer_not_in', 'buyer_contains', 'buyer_contains_nocase', 'buyer_not_contains', 'buyer_not_contains_nocase', 'buyer_starts_with', 'buyer_starts_with_nocase', 'buyer_not_starts_with', 'buyer_not_starts_with_nocase', 'buyer_ends_with', 'buyer_ends_with_nocase', 'buyer_not_ends_with', 'buyer_not_ends_with_nocase', 'buyer_', 'receiver', 'receiver_not', 'receiver_gt', 'receiver_lt', 'receiver_gte', 'receiver_lte', 'receiver_in', 'receiver_not_in', 'receiver_contains', 'receiver_contains_nocase', 'receiver_not_contains', 'receiver_not_contains_nocase', 'receiver_starts_with', 'receiver_starts_with_nocase', 'receiver_not_starts_with', 'receiver_not_starts_with_nocase', 'receiver_ends_with', 'receiver_ends_with_nocase', 'receiver_not_ends_with', 'receiver_not_ends_with_nocase', 'receiver_', 'token_sold', 'token_sold_not', 'token_sold_gt', 'token_sold_lt', 'token_sold_gte', 'token_sold_lte', 'token_sold_in', 'token_sold_not_in', 'token_sold_contains', 'token_sold_contains_nocase', 'token_sold_not_contains', 'token_sold_not_contains_nocase', 'token_sold_starts_with', 'token_sold_starts_with_nocase', 'token_sold_not_starts_with', 'token_sold_not_starts_with_nocase', 'token_sold_ends_with', 'token_sold_ends_with_nocase', 'token_sold_not_ends_with', 'token_sold_not_ends_with_nocase', 'token_sold_', 'token_bought', 'token_bought_not', 'token_bought_gt', 'token_bought_lt', 'token_bought_gte', 'token_bought_lte', 'token_bought_in', 'token_bought_not_in', 'token_bought_contains', 'token_bought_contains_nocase', 'token_bought_not_contains', 'token_bought_not_contains_nocase', 'token_bought_starts_with', 'token_bought_starts_with_nocase', 'token_bought_not_starts_with', 'token_bought_not_starts_with_nocase', 'token_bought_ends_with', 'token_bought_ends_with_nocase', 'token_bought_not_ends_with', 'token_bought_not_ends_with_nocase', 'token_bought_', 'amount_sold', 'amount_sold_not', 'amount_sold_gt', 'amount_sold_lt', 'amount_sold_gte', 'amount_sold_lte', 'amount_sold_in', 'amount_sold_not_in', 'amount_bought', 'amount_bought_not', 'amount_bought_gt', 'amount_bought_lt', 'amount_bought_gte', 'amount_bought_lte', 'amount_bought_in', 'amount_bought_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    buyer = sgqlc.types.Field(String, graphql_name='buyer')
    buyer_not = sgqlc.types.Field(String, graphql_name='buyer_not')
    buyer_gt = sgqlc.types.Field(String, graphql_name='buyer_gt')
    buyer_lt = sgqlc.types.Field(String, graphql_name='buyer_lt')
    buyer_gte = sgqlc.types.Field(String, graphql_name='buyer_gte')
    buyer_lte = sgqlc.types.Field(String, graphql_name='buyer_lte')
    buyer_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='buyer_in')
    buyer_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='buyer_not_in')
    buyer_contains = sgqlc.types.Field(String, graphql_name='buyer_contains')
    buyer_contains_nocase = sgqlc.types.Field(String, graphql_name='buyer_contains_nocase')
    buyer_not_contains = sgqlc.types.Field(String, graphql_name='buyer_not_contains')
    buyer_not_contains_nocase = sgqlc.types.Field(String, graphql_name='buyer_not_contains_nocase')
    buyer_starts_with = sgqlc.types.Field(String, graphql_name='buyer_starts_with')
    buyer_starts_with_nocase = sgqlc.types.Field(String, graphql_name='buyer_starts_with_nocase')
    buyer_not_starts_with = sgqlc.types.Field(String, graphql_name='buyer_not_starts_with')
    buyer_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='buyer_not_starts_with_nocase')
    buyer_ends_with = sgqlc.types.Field(String, graphql_name='buyer_ends_with')
    buyer_ends_with_nocase = sgqlc.types.Field(String, graphql_name='buyer_ends_with_nocase')
    buyer_not_ends_with = sgqlc.types.Field(String, graphql_name='buyer_not_ends_with')
    buyer_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='buyer_not_ends_with_nocase')
    buyer_ = sgqlc.types.Field(Account_filter, graphql_name='buyer_')
    receiver = sgqlc.types.Field(String, graphql_name='receiver')
    receiver_not = sgqlc.types.Field(String, graphql_name='receiver_not')
    receiver_gt = sgqlc.types.Field(String, graphql_name='receiver_gt')
    receiver_lt = sgqlc.types.Field(String, graphql_name='receiver_lt')
    receiver_gte = sgqlc.types.Field(String, graphql_name='receiver_gte')
    receiver_lte = sgqlc.types.Field(String, graphql_name='receiver_lte')
    receiver_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='receiver_in')
    receiver_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='receiver_not_in')
    receiver_contains = sgqlc.types.Field(String, graphql_name='receiver_contains')
    receiver_contains_nocase = sgqlc.types.Field(String, graphql_name='receiver_contains_nocase')
    receiver_not_contains = sgqlc.types.Field(String, graphql_name='receiver_not_contains')
    receiver_not_contains_nocase = sgqlc.types.Field(String, graphql_name='receiver_not_contains_nocase')
    receiver_starts_with = sgqlc.types.Field(String, graphql_name='receiver_starts_with')
    receiver_starts_with_nocase = sgqlc.types.Field(String, graphql_name='receiver_starts_with_nocase')
    receiver_not_starts_with = sgqlc.types.Field(String, graphql_name='receiver_not_starts_with')
    receiver_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='receiver_not_starts_with_nocase')
    receiver_ends_with = sgqlc.types.Field(String, graphql_name='receiver_ends_with')
    receiver_ends_with_nocase = sgqlc.types.Field(String, graphql_name='receiver_ends_with_nocase')
    receiver_not_ends_with = sgqlc.types.Field(String, graphql_name='receiver_not_ends_with')
    receiver_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='receiver_not_ends_with_nocase')
    receiver_ = sgqlc.types.Field(Account_filter, graphql_name='receiver_')
    token_sold = sgqlc.types.Field(String, graphql_name='tokenSold')
    token_sold_not = sgqlc.types.Field(String, graphql_name='tokenSold_not')
    token_sold_gt = sgqlc.types.Field(String, graphql_name='tokenSold_gt')
    token_sold_lt = sgqlc.types.Field(String, graphql_name='tokenSold_lt')
    token_sold_gte = sgqlc.types.Field(String, graphql_name='tokenSold_gte')
    token_sold_lte = sgqlc.types.Field(String, graphql_name='tokenSold_lte')
    token_sold_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenSold_in')
    token_sold_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenSold_not_in')
    token_sold_contains = sgqlc.types.Field(String, graphql_name='tokenSold_contains')
    token_sold_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenSold_contains_nocase')
    token_sold_not_contains = sgqlc.types.Field(String, graphql_name='tokenSold_not_contains')
    token_sold_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenSold_not_contains_nocase')
    token_sold_starts_with = sgqlc.types.Field(String, graphql_name='tokenSold_starts_with')
    token_sold_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenSold_starts_with_nocase')
    token_sold_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenSold_not_starts_with')
    token_sold_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenSold_not_starts_with_nocase')
    token_sold_ends_with = sgqlc.types.Field(String, graphql_name='tokenSold_ends_with')
    token_sold_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenSold_ends_with_nocase')
    token_sold_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenSold_not_ends_with')
    token_sold_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenSold_not_ends_with_nocase')
    token_sold_ = sgqlc.types.Field('Token_filter', graphql_name='tokenSold_')
    token_bought = sgqlc.types.Field(String, graphql_name='tokenBought')
    token_bought_not = sgqlc.types.Field(String, graphql_name='tokenBought_not')
    token_bought_gt = sgqlc.types.Field(String, graphql_name='tokenBought_gt')
    token_bought_lt = sgqlc.types.Field(String, graphql_name='tokenBought_lt')
    token_bought_gte = sgqlc.types.Field(String, graphql_name='tokenBought_gte')
    token_bought_lte = sgqlc.types.Field(String, graphql_name='tokenBought_lte')
    token_bought_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenBought_in')
    token_bought_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenBought_not_in')
    token_bought_contains = sgqlc.types.Field(String, graphql_name='tokenBought_contains')
    token_bought_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenBought_contains_nocase')
    token_bought_not_contains = sgqlc.types.Field(String, graphql_name='tokenBought_not_contains')
    token_bought_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenBought_not_contains_nocase')
    token_bought_starts_with = sgqlc.types.Field(String, graphql_name='tokenBought_starts_with')
    token_bought_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenBought_starts_with_nocase')
    token_bought_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenBought_not_starts_with')
    token_bought_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenBought_not_starts_with_nocase')
    token_bought_ends_with = sgqlc.types.Field(String, graphql_name='tokenBought_ends_with')
    token_bought_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenBought_ends_with_nocase')
    token_bought_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenBought_not_ends_with')
    token_bought_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenBought_not_ends_with_nocase')
    token_bought_ = sgqlc.types.Field('Token_filter', graphql_name='tokenBought_')
    amount_sold = sgqlc.types.Field(BigDecimal, graphql_name='amountSold')
    amount_sold_not = sgqlc.types.Field(BigDecimal, graphql_name='amountSold_not')
    amount_sold_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountSold_gt')
    amount_sold_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountSold_lt')
    amount_sold_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountSold_gte')
    amount_sold_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountSold_lte')
    amount_sold_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountSold_in')
    amount_sold_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountSold_not_in')
    amount_bought = sgqlc.types.Field(BigDecimal, graphql_name='amountBought')
    amount_bought_not = sgqlc.types.Field(BigDecimal, graphql_name='amountBought_not')
    amount_bought_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountBought_gt')
    amount_bought_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountBought_lt')
    amount_bought_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountBought_gte')
    amount_bought_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountBought_lte')
    amount_bought_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountBought_in')
    amount_bought_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountBought_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class FeeChangelog_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'value', 'value_not', 'value_gt', 'value_lt', 'value_gte', 'value_lte', 'value_in', 'value_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    value = sgqlc.types.Field(BigDecimal, graphql_name='value')
    value_not = sgqlc.types.Field(BigDecimal, graphql_name='value_not')
    value_gt = sgqlc.types.Field(BigDecimal, graphql_name='value_gt')
    value_lt = sgqlc.types.Field(BigDecimal, graphql_name='value_lt')
    value_gte = sgqlc.types.Field(BigDecimal, graphql_name='value_gte')
    value_lte = sgqlc.types.Field(BigDecimal, graphql_name='value_lte')
    value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_in')
    value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeDeposit_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'gauge', 'gauge_not', 'gauge_gt', 'gauge_lt', 'gauge_gte', 'gauge_lte', 'gauge_in', 'gauge_not_in', 'gauge_contains', 'gauge_contains_nocase', 'gauge_not_contains', 'gauge_not_contains_nocase', 'gauge_starts_with', 'gauge_starts_with_nocase', 'gauge_not_starts_with', 'gauge_not_starts_with_nocase', 'gauge_ends_with', 'gauge_ends_with_nocase', 'gauge_not_ends_with', 'gauge_not_ends_with_nocase', 'gauge_', 'provider', 'provider_not', 'provider_gt', 'provider_lt', 'provider_gte', 'provider_lte', 'provider_in', 'provider_not_in', 'provider_contains', 'provider_contains_nocase', 'provider_not_contains', 'provider_not_contains_nocase', 'provider_starts_with', 'provider_starts_with_nocase', 'provider_not_starts_with', 'provider_not_starts_with_nocase', 'provider_ends_with', 'provider_ends_with_nocase', 'provider_not_ends_with', 'provider_not_ends_with_nocase', 'provider_', 'value', 'value_not', 'value_gt', 'value_lt', 'value_gte', 'value_lte', 'value_in', 'value_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    gauge = sgqlc.types.Field(String, graphql_name='gauge')
    gauge_not = sgqlc.types.Field(String, graphql_name='gauge_not')
    gauge_gt = sgqlc.types.Field(String, graphql_name='gauge_gt')
    gauge_lt = sgqlc.types.Field(String, graphql_name='gauge_lt')
    gauge_gte = sgqlc.types.Field(String, graphql_name='gauge_gte')
    gauge_lte = sgqlc.types.Field(String, graphql_name='gauge_lte')
    gauge_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_in')
    gauge_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_not_in')
    gauge_contains = sgqlc.types.Field(String, graphql_name='gauge_contains')
    gauge_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_contains_nocase')
    gauge_not_contains = sgqlc.types.Field(String, graphql_name='gauge_not_contains')
    gauge_not_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_contains_nocase')
    gauge_starts_with = sgqlc.types.Field(String, graphql_name='gauge_starts_with')
    gauge_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_starts_with_nocase')
    gauge_not_starts_with = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with')
    gauge_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with_nocase')
    gauge_ends_with = sgqlc.types.Field(String, graphql_name='gauge_ends_with')
    gauge_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_ends_with_nocase')
    gauge_not_ends_with = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with')
    gauge_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with_nocase')
    gauge_ = sgqlc.types.Field('Gauge_filter', graphql_name='gauge_')
    provider = sgqlc.types.Field(String, graphql_name='provider')
    provider_not = sgqlc.types.Field(String, graphql_name='provider_not')
    provider_gt = sgqlc.types.Field(String, graphql_name='provider_gt')
    provider_lt = sgqlc.types.Field(String, graphql_name='provider_lt')
    provider_gte = sgqlc.types.Field(String, graphql_name='provider_gte')
    provider_lte = sgqlc.types.Field(String, graphql_name='provider_lte')
    provider_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_in')
    provider_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_not_in')
    provider_contains = sgqlc.types.Field(String, graphql_name='provider_contains')
    provider_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_contains_nocase')
    provider_not_contains = sgqlc.types.Field(String, graphql_name='provider_not_contains')
    provider_not_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_not_contains_nocase')
    provider_starts_with = sgqlc.types.Field(String, graphql_name='provider_starts_with')
    provider_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_starts_with_nocase')
    provider_not_starts_with = sgqlc.types.Field(String, graphql_name='provider_not_starts_with')
    provider_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_starts_with_nocase')
    provider_ends_with = sgqlc.types.Field(String, graphql_name='provider_ends_with')
    provider_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_ends_with_nocase')
    provider_not_ends_with = sgqlc.types.Field(String, graphql_name='provider_not_ends_with')
    provider_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_ends_with_nocase')
    provider_ = sgqlc.types.Field(Account_filter, graphql_name='provider_')
    value = sgqlc.types.Field(BigDecimal, graphql_name='value')
    value_not = sgqlc.types.Field(BigDecimal, graphql_name='value_not')
    value_gt = sgqlc.types.Field(BigDecimal, graphql_name='value_gt')
    value_lt = sgqlc.types.Field(BigDecimal, graphql_name='value_lt')
    value_gte = sgqlc.types.Field(BigDecimal, graphql_name='value_gte')
    value_lte = sgqlc.types.Field(BigDecimal, graphql_name='value_lte')
    value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_in')
    value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeLiquidity_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'user', 'user_not', 'user_gt', 'user_lt', 'user_gte', 'user_lte', 'user_in', 'user_not_in', 'user_contains', 'user_contains_nocase', 'user_not_contains', 'user_not_contains_nocase', 'user_starts_with', 'user_starts_with_nocase', 'user_not_starts_with', 'user_not_starts_with_nocase', 'user_ends_with', 'user_ends_with_nocase', 'user_not_ends_with', 'user_not_ends_with_nocase', 'user_', 'gauge', 'gauge_not', 'gauge_gt', 'gauge_lt', 'gauge_gte', 'gauge_lte', 'gauge_in', 'gauge_not_in', 'gauge_contains', 'gauge_contains_nocase', 'gauge_not_contains', 'gauge_not_contains_nocase', 'gauge_starts_with', 'gauge_starts_with_nocase', 'gauge_not_starts_with', 'gauge_not_starts_with_nocase', 'gauge_ends_with', 'gauge_ends_with_nocase', 'gauge_not_ends_with', 'gauge_not_ends_with_nocase', 'gauge_', 'original_balance', 'original_balance_not', 'original_balance_gt', 'original_balance_lt', 'original_balance_gte', 'original_balance_lte', 'original_balance_in', 'original_balance_not_in', 'original_supply', 'original_supply_not', 'original_supply_gt', 'original_supply_lt', 'original_supply_gte', 'original_supply_lte', 'original_supply_in', 'original_supply_not_in', 'working_balance', 'working_balance_not', 'working_balance_gt', 'working_balance_lt', 'working_balance_gte', 'working_balance_lte', 'working_balance_in', 'working_balance_not_in', 'working_supply', 'working_supply_not', 'working_supply_gt', 'working_supply_lt', 'working_supply_gte', 'working_supply_lte', 'working_supply_in', 'working_supply_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    user = sgqlc.types.Field(String, graphql_name='user')
    user_not = sgqlc.types.Field(String, graphql_name='user_not')
    user_gt = sgqlc.types.Field(String, graphql_name='user_gt')
    user_lt = sgqlc.types.Field(String, graphql_name='user_lt')
    user_gte = sgqlc.types.Field(String, graphql_name='user_gte')
    user_lte = sgqlc.types.Field(String, graphql_name='user_lte')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_not_in')
    user_contains = sgqlc.types.Field(String, graphql_name='user_contains')
    user_contains_nocase = sgqlc.types.Field(String, graphql_name='user_contains_nocase')
    user_not_contains = sgqlc.types.Field(String, graphql_name='user_not_contains')
    user_not_contains_nocase = sgqlc.types.Field(String, graphql_name='user_not_contains_nocase')
    user_starts_with = sgqlc.types.Field(String, graphql_name='user_starts_with')
    user_starts_with_nocase = sgqlc.types.Field(String, graphql_name='user_starts_with_nocase')
    user_not_starts_with = sgqlc.types.Field(String, graphql_name='user_not_starts_with')
    user_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='user_not_starts_with_nocase')
    user_ends_with = sgqlc.types.Field(String, graphql_name='user_ends_with')
    user_ends_with_nocase = sgqlc.types.Field(String, graphql_name='user_ends_with_nocase')
    user_not_ends_with = sgqlc.types.Field(String, graphql_name='user_not_ends_with')
    user_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='user_not_ends_with_nocase')
    user_ = sgqlc.types.Field(Account_filter, graphql_name='user_')
    gauge = sgqlc.types.Field(String, graphql_name='gauge')
    gauge_not = sgqlc.types.Field(String, graphql_name='gauge_not')
    gauge_gt = sgqlc.types.Field(String, graphql_name='gauge_gt')
    gauge_lt = sgqlc.types.Field(String, graphql_name='gauge_lt')
    gauge_gte = sgqlc.types.Field(String, graphql_name='gauge_gte')
    gauge_lte = sgqlc.types.Field(String, graphql_name='gauge_lte')
    gauge_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_in')
    gauge_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_not_in')
    gauge_contains = sgqlc.types.Field(String, graphql_name='gauge_contains')
    gauge_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_contains_nocase')
    gauge_not_contains = sgqlc.types.Field(String, graphql_name='gauge_not_contains')
    gauge_not_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_contains_nocase')
    gauge_starts_with = sgqlc.types.Field(String, graphql_name='gauge_starts_with')
    gauge_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_starts_with_nocase')
    gauge_not_starts_with = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with')
    gauge_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with_nocase')
    gauge_ends_with = sgqlc.types.Field(String, graphql_name='gauge_ends_with')
    gauge_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_ends_with_nocase')
    gauge_not_ends_with = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with')
    gauge_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with_nocase')
    gauge_ = sgqlc.types.Field('Gauge_filter', graphql_name='gauge_')
    original_balance = sgqlc.types.Field(BigInt, graphql_name='originalBalance')
    original_balance_not = sgqlc.types.Field(BigInt, graphql_name='originalBalance_not')
    original_balance_gt = sgqlc.types.Field(BigInt, graphql_name='originalBalance_gt')
    original_balance_lt = sgqlc.types.Field(BigInt, graphql_name='originalBalance_lt')
    original_balance_gte = sgqlc.types.Field(BigInt, graphql_name='originalBalance_gte')
    original_balance_lte = sgqlc.types.Field(BigInt, graphql_name='originalBalance_lte')
    original_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='originalBalance_in')
    original_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='originalBalance_not_in')
    original_supply = sgqlc.types.Field(BigInt, graphql_name='originalSupply')
    original_supply_not = sgqlc.types.Field(BigInt, graphql_name='originalSupply_not')
    original_supply_gt = sgqlc.types.Field(BigInt, graphql_name='originalSupply_gt')
    original_supply_lt = sgqlc.types.Field(BigInt, graphql_name='originalSupply_lt')
    original_supply_gte = sgqlc.types.Field(BigInt, graphql_name='originalSupply_gte')
    original_supply_lte = sgqlc.types.Field(BigInt, graphql_name='originalSupply_lte')
    original_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='originalSupply_in')
    original_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='originalSupply_not_in')
    working_balance = sgqlc.types.Field(BigInt, graphql_name='workingBalance')
    working_balance_not = sgqlc.types.Field(BigInt, graphql_name='workingBalance_not')
    working_balance_gt = sgqlc.types.Field(BigInt, graphql_name='workingBalance_gt')
    working_balance_lt = sgqlc.types.Field(BigInt, graphql_name='workingBalance_lt')
    working_balance_gte = sgqlc.types.Field(BigInt, graphql_name='workingBalance_gte')
    working_balance_lte = sgqlc.types.Field(BigInt, graphql_name='workingBalance_lte')
    working_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='workingBalance_in')
    working_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='workingBalance_not_in')
    working_supply = sgqlc.types.Field(BigInt, graphql_name='workingSupply')
    working_supply_not = sgqlc.types.Field(BigInt, graphql_name='workingSupply_not')
    working_supply_gt = sgqlc.types.Field(BigInt, graphql_name='workingSupply_gt')
    working_supply_lt = sgqlc.types.Field(BigInt, graphql_name='workingSupply_lt')
    working_supply_gte = sgqlc.types.Field(BigInt, graphql_name='workingSupply_gte')
    working_supply_lte = sgqlc.types.Field(BigInt, graphql_name='workingSupply_lte')
    working_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='workingSupply_in')
    working_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='workingSupply_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeTotalWeight_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'time', 'time_not', 'time_gt', 'time_lt', 'time_gte', 'time_lte', 'time_in', 'time_not_in', 'weight', 'weight_not', 'weight_gt', 'weight_lt', 'weight_gte', 'weight_lte', 'weight_in', 'weight_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    time = sgqlc.types.Field(BigInt, graphql_name='time')
    time_not = sgqlc.types.Field(BigInt, graphql_name='time_not')
    time_gt = sgqlc.types.Field(BigInt, graphql_name='time_gt')
    time_lt = sgqlc.types.Field(BigInt, graphql_name='time_lt')
    time_gte = sgqlc.types.Field(BigInt, graphql_name='time_gte')
    time_lte = sgqlc.types.Field(BigInt, graphql_name='time_lte')
    time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_in')
    time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_not_in')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')
    weight_not = sgqlc.types.Field(BigDecimal, graphql_name='weight_not')
    weight_gt = sgqlc.types.Field(BigDecimal, graphql_name='weight_gt')
    weight_lt = sgqlc.types.Field(BigDecimal, graphql_name='weight_lt')
    weight_gte = sgqlc.types.Field(BigDecimal, graphql_name='weight_gte')
    weight_lte = sgqlc.types.Field(BigDecimal, graphql_name='weight_lte')
    weight_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_in')
    weight_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeTypeWeight_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'type', 'type_not', 'type_gt', 'type_lt', 'type_gte', 'type_lte', 'type_in', 'type_not_in', 'type_contains', 'type_contains_nocase', 'type_not_contains', 'type_not_contains_nocase', 'type_starts_with', 'type_starts_with_nocase', 'type_not_starts_with', 'type_not_starts_with_nocase', 'type_ends_with', 'type_ends_with_nocase', 'type_not_ends_with', 'type_not_ends_with_nocase', 'type_', 'time', 'time_not', 'time_gt', 'time_lt', 'time_gte', 'time_lte', 'time_in', 'time_not_in', 'weight', 'weight_not', 'weight_gt', 'weight_lt', 'weight_gte', 'weight_lte', 'weight_in', 'weight_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    type = sgqlc.types.Field(String, graphql_name='type')
    type_not = sgqlc.types.Field(String, graphql_name='type_not')
    type_gt = sgqlc.types.Field(String, graphql_name='type_gt')
    type_lt = sgqlc.types.Field(String, graphql_name='type_lt')
    type_gte = sgqlc.types.Field(String, graphql_name='type_gte')
    type_lte = sgqlc.types.Field(String, graphql_name='type_lte')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='type_not_in')
    type_contains = sgqlc.types.Field(String, graphql_name='type_contains')
    type_contains_nocase = sgqlc.types.Field(String, graphql_name='type_contains_nocase')
    type_not_contains = sgqlc.types.Field(String, graphql_name='type_not_contains')
    type_not_contains_nocase = sgqlc.types.Field(String, graphql_name='type_not_contains_nocase')
    type_starts_with = sgqlc.types.Field(String, graphql_name='type_starts_with')
    type_starts_with_nocase = sgqlc.types.Field(String, graphql_name='type_starts_with_nocase')
    type_not_starts_with = sgqlc.types.Field(String, graphql_name='type_not_starts_with')
    type_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='type_not_starts_with_nocase')
    type_ends_with = sgqlc.types.Field(String, graphql_name='type_ends_with')
    type_ends_with_nocase = sgqlc.types.Field(String, graphql_name='type_ends_with_nocase')
    type_not_ends_with = sgqlc.types.Field(String, graphql_name='type_not_ends_with')
    type_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='type_not_ends_with_nocase')
    type_ = sgqlc.types.Field('GaugeType_filter', graphql_name='type_')
    time = sgqlc.types.Field(BigInt, graphql_name='time')
    time_not = sgqlc.types.Field(BigInt, graphql_name='time_not')
    time_gt = sgqlc.types.Field(BigInt, graphql_name='time_gt')
    time_lt = sgqlc.types.Field(BigInt, graphql_name='time_lt')
    time_gte = sgqlc.types.Field(BigInt, graphql_name='time_gte')
    time_lte = sgqlc.types.Field(BigInt, graphql_name='time_lte')
    time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_in')
    time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_not_in')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')
    weight_not = sgqlc.types.Field(BigDecimal, graphql_name='weight_not')
    weight_gt = sgqlc.types.Field(BigDecimal, graphql_name='weight_gt')
    weight_lt = sgqlc.types.Field(BigDecimal, graphql_name='weight_lt')
    weight_gte = sgqlc.types.Field(BigDecimal, graphql_name='weight_gte')
    weight_lte = sgqlc.types.Field(BigDecimal, graphql_name='weight_lte')
    weight_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_in')
    weight_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeType_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'gauge_count', 'gauge_count_not', 'gauge_count_gt', 'gauge_count_lt', 'gauge_count_gte', 'gauge_count_lte', 'gauge_count_in', 'gauge_count_not_in', 'gauges_', 'weights_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    gauge_count = sgqlc.types.Field(BigInt, graphql_name='gaugeCount')
    gauge_count_not = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_not')
    gauge_count_gt = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_gt')
    gauge_count_lt = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_lt')
    gauge_count_gte = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_gte')
    gauge_count_lte = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_lte')
    gauge_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeCount_in')
    gauge_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeCount_not_in')
    gauges_ = sgqlc.types.Field('Gauge_filter', graphql_name='gauges_')
    weights_ = sgqlc.types.Field(GaugeTypeWeight_filter, graphql_name='weights_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeWeightVote_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'gauge', 'gauge_not', 'gauge_gt', 'gauge_lt', 'gauge_gte', 'gauge_lte', 'gauge_in', 'gauge_not_in', 'gauge_contains', 'gauge_contains_nocase', 'gauge_not_contains', 'gauge_not_contains_nocase', 'gauge_starts_with', 'gauge_starts_with_nocase', 'gauge_not_starts_with', 'gauge_not_starts_with_nocase', 'gauge_ends_with', 'gauge_ends_with_nocase', 'gauge_not_ends_with', 'gauge_not_ends_with_nocase', 'gauge_', 'user', 'user_not', 'user_gt', 'user_lt', 'user_gte', 'user_lte', 'user_in', 'user_not_in', 'user_contains', 'user_contains_nocase', 'user_not_contains', 'user_not_contains_nocase', 'user_starts_with', 'user_starts_with_nocase', 'user_not_starts_with', 'user_not_starts_with_nocase', 'user_ends_with', 'user_ends_with_nocase', 'user_not_ends_with', 'user_not_ends_with_nocase', 'user_', 'time', 'time_not', 'time_gt', 'time_lt', 'time_gte', 'time_lte', 'time_in', 'time_not_in', 'weight', 'weight_not', 'weight_gt', 'weight_lt', 'weight_gte', 'weight_lte', 'weight_in', 'weight_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    gauge = sgqlc.types.Field(String, graphql_name='gauge')
    gauge_not = sgqlc.types.Field(String, graphql_name='gauge_not')
    gauge_gt = sgqlc.types.Field(String, graphql_name='gauge_gt')
    gauge_lt = sgqlc.types.Field(String, graphql_name='gauge_lt')
    gauge_gte = sgqlc.types.Field(String, graphql_name='gauge_gte')
    gauge_lte = sgqlc.types.Field(String, graphql_name='gauge_lte')
    gauge_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_in')
    gauge_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_not_in')
    gauge_contains = sgqlc.types.Field(String, graphql_name='gauge_contains')
    gauge_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_contains_nocase')
    gauge_not_contains = sgqlc.types.Field(String, graphql_name='gauge_not_contains')
    gauge_not_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_contains_nocase')
    gauge_starts_with = sgqlc.types.Field(String, graphql_name='gauge_starts_with')
    gauge_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_starts_with_nocase')
    gauge_not_starts_with = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with')
    gauge_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with_nocase')
    gauge_ends_with = sgqlc.types.Field(String, graphql_name='gauge_ends_with')
    gauge_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_ends_with_nocase')
    gauge_not_ends_with = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with')
    gauge_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with_nocase')
    gauge_ = sgqlc.types.Field('Gauge_filter', graphql_name='gauge_')
    user = sgqlc.types.Field(String, graphql_name='user')
    user_not = sgqlc.types.Field(String, graphql_name='user_not')
    user_gt = sgqlc.types.Field(String, graphql_name='user_gt')
    user_lt = sgqlc.types.Field(String, graphql_name='user_lt')
    user_gte = sgqlc.types.Field(String, graphql_name='user_gte')
    user_lte = sgqlc.types.Field(String, graphql_name='user_lte')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_not_in')
    user_contains = sgqlc.types.Field(String, graphql_name='user_contains')
    user_contains_nocase = sgqlc.types.Field(String, graphql_name='user_contains_nocase')
    user_not_contains = sgqlc.types.Field(String, graphql_name='user_not_contains')
    user_not_contains_nocase = sgqlc.types.Field(String, graphql_name='user_not_contains_nocase')
    user_starts_with = sgqlc.types.Field(String, graphql_name='user_starts_with')
    user_starts_with_nocase = sgqlc.types.Field(String, graphql_name='user_starts_with_nocase')
    user_not_starts_with = sgqlc.types.Field(String, graphql_name='user_not_starts_with')
    user_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='user_not_starts_with_nocase')
    user_ends_with = sgqlc.types.Field(String, graphql_name='user_ends_with')
    user_ends_with_nocase = sgqlc.types.Field(String, graphql_name='user_ends_with_nocase')
    user_not_ends_with = sgqlc.types.Field(String, graphql_name='user_not_ends_with')
    user_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='user_not_ends_with_nocase')
    user_ = sgqlc.types.Field(Account_filter, graphql_name='user_')
    time = sgqlc.types.Field(BigInt, graphql_name='time')
    time_not = sgqlc.types.Field(BigInt, graphql_name='time_not')
    time_gt = sgqlc.types.Field(BigInt, graphql_name='time_gt')
    time_lt = sgqlc.types.Field(BigInt, graphql_name='time_lt')
    time_gte = sgqlc.types.Field(BigInt, graphql_name='time_gte')
    time_lte = sgqlc.types.Field(BigInt, graphql_name='time_lte')
    time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_in')
    time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_not_in')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')
    weight_not = sgqlc.types.Field(BigDecimal, graphql_name='weight_not')
    weight_gt = sgqlc.types.Field(BigDecimal, graphql_name='weight_gt')
    weight_lt = sgqlc.types.Field(BigDecimal, graphql_name='weight_lt')
    weight_gte = sgqlc.types.Field(BigDecimal, graphql_name='weight_gte')
    weight_lte = sgqlc.types.Field(BigDecimal, graphql_name='weight_lte')
    weight_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_in')
    weight_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeWeight_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'gauge', 'gauge_not', 'gauge_gt', 'gauge_lt', 'gauge_gte', 'gauge_lte', 'gauge_in', 'gauge_not_in', 'gauge_contains', 'gauge_contains_nocase', 'gauge_not_contains', 'gauge_not_contains_nocase', 'gauge_starts_with', 'gauge_starts_with_nocase', 'gauge_not_starts_with', 'gauge_not_starts_with_nocase', 'gauge_ends_with', 'gauge_ends_with_nocase', 'gauge_not_ends_with', 'gauge_not_ends_with_nocase', 'gauge_', 'time', 'time_not', 'time_gt', 'time_lt', 'time_gte', 'time_lte', 'time_in', 'time_not_in', 'weight', 'weight_not', 'weight_gt', 'weight_lt', 'weight_gte', 'weight_lte', 'weight_in', 'weight_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    gauge = sgqlc.types.Field(String, graphql_name='gauge')
    gauge_not = sgqlc.types.Field(String, graphql_name='gauge_not')
    gauge_gt = sgqlc.types.Field(String, graphql_name='gauge_gt')
    gauge_lt = sgqlc.types.Field(String, graphql_name='gauge_lt')
    gauge_gte = sgqlc.types.Field(String, graphql_name='gauge_gte')
    gauge_lte = sgqlc.types.Field(String, graphql_name='gauge_lte')
    gauge_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_in')
    gauge_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_not_in')
    gauge_contains = sgqlc.types.Field(String, graphql_name='gauge_contains')
    gauge_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_contains_nocase')
    gauge_not_contains = sgqlc.types.Field(String, graphql_name='gauge_not_contains')
    gauge_not_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_contains_nocase')
    gauge_starts_with = sgqlc.types.Field(String, graphql_name='gauge_starts_with')
    gauge_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_starts_with_nocase')
    gauge_not_starts_with = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with')
    gauge_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with_nocase')
    gauge_ends_with = sgqlc.types.Field(String, graphql_name='gauge_ends_with')
    gauge_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_ends_with_nocase')
    gauge_not_ends_with = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with')
    gauge_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with_nocase')
    gauge_ = sgqlc.types.Field('Gauge_filter', graphql_name='gauge_')
    time = sgqlc.types.Field(BigInt, graphql_name='time')
    time_not = sgqlc.types.Field(BigInt, graphql_name='time_not')
    time_gt = sgqlc.types.Field(BigInt, graphql_name='time_gt')
    time_lt = sgqlc.types.Field(BigInt, graphql_name='time_lt')
    time_gte = sgqlc.types.Field(BigInt, graphql_name='time_gte')
    time_lte = sgqlc.types.Field(BigInt, graphql_name='time_lte')
    time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_in')
    time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='time_not_in')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')
    weight_not = sgqlc.types.Field(BigDecimal, graphql_name='weight_not')
    weight_gt = sgqlc.types.Field(BigDecimal, graphql_name='weight_gt')
    weight_lt = sgqlc.types.Field(BigDecimal, graphql_name='weight_lt')
    weight_gte = sgqlc.types.Field(BigDecimal, graphql_name='weight_gte')
    weight_lte = sgqlc.types.Field(BigDecimal, graphql_name='weight_lte')
    weight_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_in')
    weight_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class GaugeWithdraw_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'gauge', 'gauge_not', 'gauge_gt', 'gauge_lt', 'gauge_gte', 'gauge_lte', 'gauge_in', 'gauge_not_in', 'gauge_contains', 'gauge_contains_nocase', 'gauge_not_contains', 'gauge_not_contains_nocase', 'gauge_starts_with', 'gauge_starts_with_nocase', 'gauge_not_starts_with', 'gauge_not_starts_with_nocase', 'gauge_ends_with', 'gauge_ends_with_nocase', 'gauge_not_ends_with', 'gauge_not_ends_with_nocase', 'gauge_', 'provider', 'provider_not', 'provider_gt', 'provider_lt', 'provider_gte', 'provider_lte', 'provider_in', 'provider_not_in', 'provider_contains', 'provider_contains_nocase', 'provider_not_contains', 'provider_not_contains_nocase', 'provider_starts_with', 'provider_starts_with_nocase', 'provider_not_starts_with', 'provider_not_starts_with_nocase', 'provider_ends_with', 'provider_ends_with_nocase', 'provider_not_ends_with', 'provider_not_ends_with_nocase', 'provider_', 'value', 'value_not', 'value_gt', 'value_lt', 'value_gte', 'value_lte', 'value_in', 'value_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    gauge = sgqlc.types.Field(String, graphql_name='gauge')
    gauge_not = sgqlc.types.Field(String, graphql_name='gauge_not')
    gauge_gt = sgqlc.types.Field(String, graphql_name='gauge_gt')
    gauge_lt = sgqlc.types.Field(String, graphql_name='gauge_lt')
    gauge_gte = sgqlc.types.Field(String, graphql_name='gauge_gte')
    gauge_lte = sgqlc.types.Field(String, graphql_name='gauge_lte')
    gauge_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_in')
    gauge_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_not_in')
    gauge_contains = sgqlc.types.Field(String, graphql_name='gauge_contains')
    gauge_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_contains_nocase')
    gauge_not_contains = sgqlc.types.Field(String, graphql_name='gauge_not_contains')
    gauge_not_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_contains_nocase')
    gauge_starts_with = sgqlc.types.Field(String, graphql_name='gauge_starts_with')
    gauge_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_starts_with_nocase')
    gauge_not_starts_with = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with')
    gauge_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with_nocase')
    gauge_ends_with = sgqlc.types.Field(String, graphql_name='gauge_ends_with')
    gauge_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_ends_with_nocase')
    gauge_not_ends_with = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with')
    gauge_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with_nocase')
    gauge_ = sgqlc.types.Field('Gauge_filter', graphql_name='gauge_')
    provider = sgqlc.types.Field(String, graphql_name='provider')
    provider_not = sgqlc.types.Field(String, graphql_name='provider_not')
    provider_gt = sgqlc.types.Field(String, graphql_name='provider_gt')
    provider_lt = sgqlc.types.Field(String, graphql_name='provider_lt')
    provider_gte = sgqlc.types.Field(String, graphql_name='provider_gte')
    provider_lte = sgqlc.types.Field(String, graphql_name='provider_lte')
    provider_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_in')
    provider_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_not_in')
    provider_contains = sgqlc.types.Field(String, graphql_name='provider_contains')
    provider_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_contains_nocase')
    provider_not_contains = sgqlc.types.Field(String, graphql_name='provider_not_contains')
    provider_not_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_not_contains_nocase')
    provider_starts_with = sgqlc.types.Field(String, graphql_name='provider_starts_with')
    provider_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_starts_with_nocase')
    provider_not_starts_with = sgqlc.types.Field(String, graphql_name='provider_not_starts_with')
    provider_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_starts_with_nocase')
    provider_ends_with = sgqlc.types.Field(String, graphql_name='provider_ends_with')
    provider_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_ends_with_nocase')
    provider_not_ends_with = sgqlc.types.Field(String, graphql_name='provider_not_ends_with')
    provider_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_ends_with_nocase')
    provider_ = sgqlc.types.Field(Account_filter, graphql_name='provider_')
    value = sgqlc.types.Field(BigDecimal, graphql_name='value')
    value_not = sgqlc.types.Field(BigDecimal, graphql_name='value_not')
    value_gt = sgqlc.types.Field(BigDecimal, graphql_name='value_gt')
    value_lt = sgqlc.types.Field(BigDecimal, graphql_name='value_lt')
    value_gte = sgqlc.types.Field(BigDecimal, graphql_name='value_gte')
    value_lte = sgqlc.types.Field(BigDecimal, graphql_name='value_lte')
    value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_in')
    value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='value_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Gauge_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'type', 'type_not', 'type_gt', 'type_lt', 'type_gte', 'type_lte', 'type_in', 'type_not_in', 'type_contains', 'type_contains_nocase', 'type_not_contains', 'type_not_contains_nocase', 'type_starts_with', 'type_starts_with_nocase', 'type_not_starts_with', 'type_not_starts_with_nocase', 'type_ends_with', 'type_ends_with_nocase', 'type_not_ends_with', 'type_not_ends_with_nocase', 'type_', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'created', 'created_not', 'created_gt', 'created_lt', 'created_gte', 'created_lte', 'created_in', 'created_not_in', 'created_at_block', 'created_at_block_not', 'created_at_block_gt', 'created_at_block_lt', 'created_at_block_gte', 'created_at_block_lte', 'created_at_block_in', 'created_at_block_not_in', 'created_at_transaction', 'created_at_transaction_not', 'created_at_transaction_in', 'created_at_transaction_not_in', 'created_at_transaction_contains', 'created_at_transaction_not_contains', 'weights_', 'weight_votes_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    type = sgqlc.types.Field(String, graphql_name='type')
    type_not = sgqlc.types.Field(String, graphql_name='type_not')
    type_gt = sgqlc.types.Field(String, graphql_name='type_gt')
    type_lt = sgqlc.types.Field(String, graphql_name='type_lt')
    type_gte = sgqlc.types.Field(String, graphql_name='type_gte')
    type_lte = sgqlc.types.Field(String, graphql_name='type_lte')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='type_not_in')
    type_contains = sgqlc.types.Field(String, graphql_name='type_contains')
    type_contains_nocase = sgqlc.types.Field(String, graphql_name='type_contains_nocase')
    type_not_contains = sgqlc.types.Field(String, graphql_name='type_not_contains')
    type_not_contains_nocase = sgqlc.types.Field(String, graphql_name='type_not_contains_nocase')
    type_starts_with = sgqlc.types.Field(String, graphql_name='type_starts_with')
    type_starts_with_nocase = sgqlc.types.Field(String, graphql_name='type_starts_with_nocase')
    type_not_starts_with = sgqlc.types.Field(String, graphql_name='type_not_starts_with')
    type_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='type_not_starts_with_nocase')
    type_ends_with = sgqlc.types.Field(String, graphql_name='type_ends_with')
    type_ends_with_nocase = sgqlc.types.Field(String, graphql_name='type_ends_with_nocase')
    type_not_ends_with = sgqlc.types.Field(String, graphql_name='type_not_ends_with')
    type_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='type_not_ends_with_nocase')
    type_ = sgqlc.types.Field(GaugeType_filter, graphql_name='type_')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    created = sgqlc.types.Field(BigInt, graphql_name='created')
    created_not = sgqlc.types.Field(BigInt, graphql_name='created_not')
    created_gt = sgqlc.types.Field(BigInt, graphql_name='created_gt')
    created_lt = sgqlc.types.Field(BigInt, graphql_name='created_lt')
    created_gte = sgqlc.types.Field(BigInt, graphql_name='created_gte')
    created_lte = sgqlc.types.Field(BigInt, graphql_name='created_lte')
    created_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='created_in')
    created_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='created_not_in')
    created_at_block = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock')
    created_at_block_not = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_not')
    created_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_gt')
    created_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_lt')
    created_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_gte')
    created_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_lte')
    created_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlock_in')
    created_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlock_not_in')
    created_at_transaction = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction')
    created_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_not')
    created_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='createdAtTransaction_in')
    created_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='createdAtTransaction_not_in')
    created_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_contains')
    created_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_not_contains')
    weights_ = sgqlc.types.Field(GaugeWeight_filter, graphql_name='weights_')
    weight_votes_ = sgqlc.types.Field(GaugeWeightVote_filter, graphql_name='weightVotes_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class HourlyVolume_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class LpToken_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'gauge', 'gauge_not', 'gauge_gt', 'gauge_lt', 'gauge_gte', 'gauge_lte', 'gauge_in', 'gauge_not_in', 'gauge_contains', 'gauge_contains_nocase', 'gauge_not_contains', 'gauge_not_contains_nocase', 'gauge_starts_with', 'gauge_starts_with_nocase', 'gauge_not_starts_with', 'gauge_not_starts_with_nocase', 'gauge_ends_with', 'gauge_ends_with_nocase', 'gauge_not_ends_with', 'gauge_not_ends_with_nocase', 'gauge_', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    decimals = sgqlc.types.Field(BigInt, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(BigInt, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(BigInt, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(BigInt, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(BigInt, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(BigInt, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    symbol_not = sgqlc.types.Field(String, graphql_name='symbol_not')
    symbol_gt = sgqlc.types.Field(String, graphql_name='symbol_gt')
    symbol_lt = sgqlc.types.Field(String, graphql_name='symbol_lt')
    symbol_gte = sgqlc.types.Field(String, graphql_name='symbol_gte')
    symbol_lte = sgqlc.types.Field(String, graphql_name='symbol_lte')
    symbol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_in')
    symbol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_not_in')
    symbol_contains = sgqlc.types.Field(String, graphql_name='symbol_contains')
    symbol_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_contains_nocase')
    symbol_not_contains = sgqlc.types.Field(String, graphql_name='symbol_not_contains')
    symbol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_contains_nocase')
    symbol_starts_with = sgqlc.types.Field(String, graphql_name='symbol_starts_with')
    symbol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_starts_with_nocase')
    symbol_not_starts_with = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with')
    symbol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with_nocase')
    symbol_ends_with = sgqlc.types.Field(String, graphql_name='symbol_ends_with')
    symbol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_ends_with_nocase')
    symbol_not_ends_with = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with')
    symbol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with_nocase')
    gauge = sgqlc.types.Field(String, graphql_name='gauge')
    gauge_not = sgqlc.types.Field(String, graphql_name='gauge_not')
    gauge_gt = sgqlc.types.Field(String, graphql_name='gauge_gt')
    gauge_lt = sgqlc.types.Field(String, graphql_name='gauge_lt')
    gauge_gte = sgqlc.types.Field(String, graphql_name='gauge_gte')
    gauge_lte = sgqlc.types.Field(String, graphql_name='gauge_lte')
    gauge_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_in')
    gauge_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gauge_not_in')
    gauge_contains = sgqlc.types.Field(String, graphql_name='gauge_contains')
    gauge_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_contains_nocase')
    gauge_not_contains = sgqlc.types.Field(String, graphql_name='gauge_not_contains')
    gauge_not_contains_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_contains_nocase')
    gauge_starts_with = sgqlc.types.Field(String, graphql_name='gauge_starts_with')
    gauge_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_starts_with_nocase')
    gauge_not_starts_with = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with')
    gauge_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_starts_with_nocase')
    gauge_ends_with = sgqlc.types.Field(String, graphql_name='gauge_ends_with')
    gauge_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_ends_with_nocase')
    gauge_not_ends_with = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with')
    gauge_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='gauge_not_ends_with_nocase')
    gauge_ = sgqlc.types.Field(Gauge_filter, graphql_name='gauge_')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class PoolEvent_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Pool_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'asset_type', 'asset_type_not', 'asset_type_in', 'asset_type_not_in', 'is_meta', 'is_meta_not', 'is_meta_in', 'is_meta_not_in', 'registry_address', 'registry_address_not', 'registry_address_in', 'registry_address_not_in', 'registry_address_contains', 'registry_address_not_contains', 'swap_address', 'swap_address_not', 'swap_address_in', 'swap_address_not_in', 'swap_address_contains', 'swap_address_not_contains', 'lp_token', 'lp_token_not', 'lp_token_gt', 'lp_token_lt', 'lp_token_gte', 'lp_token_lte', 'lp_token_in', 'lp_token_not_in', 'lp_token_contains', 'lp_token_contains_nocase', 'lp_token_not_contains', 'lp_token_not_contains_nocase', 'lp_token_starts_with', 'lp_token_starts_with_nocase', 'lp_token_not_starts_with', 'lp_token_not_starts_with_nocase', 'lp_token_ends_with', 'lp_token_ends_with_nocase', 'lp_token_not_ends_with', 'lp_token_not_ends_with_nocase', 'lp_token_', 'coin_count', 'coin_count_not', 'coin_count_gt', 'coin_count_lt', 'coin_count_gte', 'coin_count_lte', 'coin_count_in', 'coin_count_not_in', 'coins_', 'underlying_count', 'underlying_count_not', 'underlying_count_gt', 'underlying_count_lt', 'underlying_count_gte', 'underlying_count_lte', 'underlying_count_in', 'underlying_count_not_in', 'underlying_coins_', 'a', 'a_not', 'a_gt', 'a_lt', 'a_gte', 'a_lte', 'a_in', 'a_not_in', 'fee', 'fee_not', 'fee_gt', 'fee_lt', 'fee_gte', 'fee_lte', 'fee_in', 'fee_not_in', 'admin_fee', 'admin_fee_not', 'admin_fee_gt', 'admin_fee_lt', 'admin_fee_gte', 'admin_fee_lte', 'admin_fee_in', 'admin_fee_not_in', 'owner', 'owner_not', 'owner_in', 'owner_not_in', 'owner_contains', 'owner_not_contains', 'virtual_price', 'virtual_price_not', 'virtual_price_gt', 'virtual_price_lt', 'virtual_price_gte', 'virtual_price_lte', 'virtual_price_in', 'virtual_price_not_in', 'locked', 'locked_not', 'locked_gt', 'locked_lt', 'locked_gte', 'locked_lte', 'locked_in', 'locked_not_in', 'added_at', 'added_at_not', 'added_at_gt', 'added_at_lt', 'added_at_gte', 'added_at_lte', 'added_at_in', 'added_at_not_in', 'added_at_block', 'added_at_block_not', 'added_at_block_gt', 'added_at_block_lt', 'added_at_block_gte', 'added_at_block_lte', 'added_at_block_in', 'added_at_block_not_in', 'added_at_transaction', 'added_at_transaction_not', 'added_at_transaction_in', 'added_at_transaction_not_in', 'added_at_transaction_contains', 'added_at_transaction_not_contains', 'removed_at', 'removed_at_not', 'removed_at_gt', 'removed_at_lt', 'removed_at_gte', 'removed_at_lte', 'removed_at_in', 'removed_at_not_in', 'removed_at_block', 'removed_at_block_not', 'removed_at_block_gt', 'removed_at_block_lt', 'removed_at_block_gte', 'removed_at_block_lte', 'removed_at_block_in', 'removed_at_block_not_in', 'removed_at_transaction', 'removed_at_transaction_not', 'removed_at_transaction_in', 'removed_at_transaction_not_in', 'removed_at_transaction_contains', 'removed_at_transaction_not_contains', 'exchange_count', 'exchange_count_not', 'exchange_count_gt', 'exchange_count_lt', 'exchange_count_gte', 'exchange_count_lte', 'exchange_count_in', 'exchange_count_not_in', 'exchanges_', 'gauge_count', 'gauge_count_not', 'gauge_count_gt', 'gauge_count_lt', 'gauge_count_gte', 'gauge_count_lte', 'gauge_count_in', 'gauge_count_not_in', 'gauges_', 'hourly_volumes_', 'daily_volumes_', 'weekly_volumes_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    asset_type = sgqlc.types.Field(AssetType, graphql_name='assetType')
    asset_type_not = sgqlc.types.Field(AssetType, graphql_name='assetType_not')
    asset_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AssetType)), graphql_name='assetType_in')
    asset_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AssetType)), graphql_name='assetType_not_in')
    is_meta = sgqlc.types.Field(Boolean, graphql_name='isMeta')
    is_meta_not = sgqlc.types.Field(Boolean, graphql_name='isMeta_not')
    is_meta_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isMeta_in')
    is_meta_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isMeta_not_in')
    registry_address = sgqlc.types.Field(Bytes, graphql_name='registryAddress')
    registry_address_not = sgqlc.types.Field(Bytes, graphql_name='registryAddress_not')
    registry_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='registryAddress_in')
    registry_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='registryAddress_not_in')
    registry_address_contains = sgqlc.types.Field(Bytes, graphql_name='registryAddress_contains')
    registry_address_not_contains = sgqlc.types.Field(Bytes, graphql_name='registryAddress_not_contains')
    swap_address = sgqlc.types.Field(Bytes, graphql_name='swapAddress')
    swap_address_not = sgqlc.types.Field(Bytes, graphql_name='swapAddress_not')
    swap_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='swapAddress_in')
    swap_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='swapAddress_not_in')
    swap_address_contains = sgqlc.types.Field(Bytes, graphql_name='swapAddress_contains')
    swap_address_not_contains = sgqlc.types.Field(Bytes, graphql_name='swapAddress_not_contains')
    lp_token = sgqlc.types.Field(String, graphql_name='lpToken')
    lp_token_not = sgqlc.types.Field(String, graphql_name='lpToken_not')
    lp_token_gt = sgqlc.types.Field(String, graphql_name='lpToken_gt')
    lp_token_lt = sgqlc.types.Field(String, graphql_name='lpToken_lt')
    lp_token_gte = sgqlc.types.Field(String, graphql_name='lpToken_gte')
    lp_token_lte = sgqlc.types.Field(String, graphql_name='lpToken_lte')
    lp_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lpToken_in')
    lp_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lpToken_not_in')
    lp_token_contains = sgqlc.types.Field(String, graphql_name='lpToken_contains')
    lp_token_contains_nocase = sgqlc.types.Field(String, graphql_name='lpToken_contains_nocase')
    lp_token_not_contains = sgqlc.types.Field(String, graphql_name='lpToken_not_contains')
    lp_token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='lpToken_not_contains_nocase')
    lp_token_starts_with = sgqlc.types.Field(String, graphql_name='lpToken_starts_with')
    lp_token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='lpToken_starts_with_nocase')
    lp_token_not_starts_with = sgqlc.types.Field(String, graphql_name='lpToken_not_starts_with')
    lp_token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='lpToken_not_starts_with_nocase')
    lp_token_ends_with = sgqlc.types.Field(String, graphql_name='lpToken_ends_with')
    lp_token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='lpToken_ends_with_nocase')
    lp_token_not_ends_with = sgqlc.types.Field(String, graphql_name='lpToken_not_ends_with')
    lp_token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='lpToken_not_ends_with_nocase')
    lp_token_ = sgqlc.types.Field(LpToken_filter, graphql_name='lpToken_')
    coin_count = sgqlc.types.Field(BigInt, graphql_name='coinCount')
    coin_count_not = sgqlc.types.Field(BigInt, graphql_name='coinCount_not')
    coin_count_gt = sgqlc.types.Field(BigInt, graphql_name='coinCount_gt')
    coin_count_lt = sgqlc.types.Field(BigInt, graphql_name='coinCount_lt')
    coin_count_gte = sgqlc.types.Field(BigInt, graphql_name='coinCount_gte')
    coin_count_lte = sgqlc.types.Field(BigInt, graphql_name='coinCount_lte')
    coin_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='coinCount_in')
    coin_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='coinCount_not_in')
    coins_ = sgqlc.types.Field(Coin_filter, graphql_name='coins_')
    underlying_count = sgqlc.types.Field(BigInt, graphql_name='underlyingCount')
    underlying_count_not = sgqlc.types.Field(BigInt, graphql_name='underlyingCount_not')
    underlying_count_gt = sgqlc.types.Field(BigInt, graphql_name='underlyingCount_gt')
    underlying_count_lt = sgqlc.types.Field(BigInt, graphql_name='underlyingCount_lt')
    underlying_count_gte = sgqlc.types.Field(BigInt, graphql_name='underlyingCount_gte')
    underlying_count_lte = sgqlc.types.Field(BigInt, graphql_name='underlyingCount_lte')
    underlying_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='underlyingCount_in')
    underlying_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='underlyingCount_not_in')
    underlying_coins_ = sgqlc.types.Field('UnderlyingCoin_filter', graphql_name='underlyingCoins_')
    a = sgqlc.types.Field(BigInt, graphql_name='A')
    a_not = sgqlc.types.Field(BigInt, graphql_name='A_not')
    a_gt = sgqlc.types.Field(BigInt, graphql_name='A_gt')
    a_lt = sgqlc.types.Field(BigInt, graphql_name='A_lt')
    a_gte = sgqlc.types.Field(BigInt, graphql_name='A_gte')
    a_lte = sgqlc.types.Field(BigInt, graphql_name='A_lte')
    a_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='A_in')
    a_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='A_not_in')
    fee = sgqlc.types.Field(BigDecimal, graphql_name='fee')
    fee_not = sgqlc.types.Field(BigDecimal, graphql_name='fee_not')
    fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='fee_gt')
    fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='fee_gte')
    fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='fee_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='fee_in')
    fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='fee_not_in')
    admin_fee = sgqlc.types.Field(BigDecimal, graphql_name='adminFee')
    admin_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='adminFee_not')
    admin_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='adminFee_gt')
    admin_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='adminFee_lt')
    admin_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='adminFee_gte')
    admin_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='adminFee_lte')
    admin_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='adminFee_in')
    admin_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='adminFee_not_in')
    owner = sgqlc.types.Field(Bytes, graphql_name='owner')
    owner_not = sgqlc.types.Field(Bytes, graphql_name='owner_not')
    owner_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='owner_in')
    owner_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='owner_not_in')
    owner_contains = sgqlc.types.Field(Bytes, graphql_name='owner_contains')
    owner_not_contains = sgqlc.types.Field(Bytes, graphql_name='owner_not_contains')
    virtual_price = sgqlc.types.Field(BigDecimal, graphql_name='virtualPrice')
    virtual_price_not = sgqlc.types.Field(BigDecimal, graphql_name='virtualPrice_not')
    virtual_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='virtualPrice_gt')
    virtual_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='virtualPrice_lt')
    virtual_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='virtualPrice_gte')
    virtual_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='virtualPrice_lte')
    virtual_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='virtualPrice_in')
    virtual_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='virtualPrice_not_in')
    locked = sgqlc.types.Field(BigDecimal, graphql_name='locked')
    locked_not = sgqlc.types.Field(BigDecimal, graphql_name='locked_not')
    locked_gt = sgqlc.types.Field(BigDecimal, graphql_name='locked_gt')
    locked_lt = sgqlc.types.Field(BigDecimal, graphql_name='locked_lt')
    locked_gte = sgqlc.types.Field(BigDecimal, graphql_name='locked_gte')
    locked_lte = sgqlc.types.Field(BigDecimal, graphql_name='locked_lte')
    locked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='locked_in')
    locked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='locked_not_in')
    added_at = sgqlc.types.Field(BigInt, graphql_name='addedAt')
    added_at_not = sgqlc.types.Field(BigInt, graphql_name='addedAt_not')
    added_at_gt = sgqlc.types.Field(BigInt, graphql_name='addedAt_gt')
    added_at_lt = sgqlc.types.Field(BigInt, graphql_name='addedAt_lt')
    added_at_gte = sgqlc.types.Field(BigInt, graphql_name='addedAt_gte')
    added_at_lte = sgqlc.types.Field(BigInt, graphql_name='addedAt_lte')
    added_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAt_in')
    added_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAt_not_in')
    added_at_block = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock')
    added_at_block_not = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_not')
    added_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_gt')
    added_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_lt')
    added_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_gte')
    added_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='addedAtBlock_lte')
    added_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAtBlock_in')
    added_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='addedAtBlock_not_in')
    added_at_transaction = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction')
    added_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_not')
    added_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='addedAtTransaction_in')
    added_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='addedAtTransaction_not_in')
    added_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_contains')
    added_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='addedAtTransaction_not_contains')
    removed_at = sgqlc.types.Field(BigInt, graphql_name='removedAt')
    removed_at_not = sgqlc.types.Field(BigInt, graphql_name='removedAt_not')
    removed_at_gt = sgqlc.types.Field(BigInt, graphql_name='removedAt_gt')
    removed_at_lt = sgqlc.types.Field(BigInt, graphql_name='removedAt_lt')
    removed_at_gte = sgqlc.types.Field(BigInt, graphql_name='removedAt_gte')
    removed_at_lte = sgqlc.types.Field(BigInt, graphql_name='removedAt_lte')
    removed_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='removedAt_in')
    removed_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='removedAt_not_in')
    removed_at_block = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock')
    removed_at_block_not = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock_not')
    removed_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock_gt')
    removed_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock_lt')
    removed_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock_gte')
    removed_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock_lte')
    removed_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='removedAtBlock_in')
    removed_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='removedAtBlock_not_in')
    removed_at_transaction = sgqlc.types.Field(Bytes, graphql_name='removedAtTransaction')
    removed_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='removedAtTransaction_not')
    removed_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='removedAtTransaction_in')
    removed_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='removedAtTransaction_not_in')
    removed_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='removedAtTransaction_contains')
    removed_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='removedAtTransaction_not_contains')
    exchange_count = sgqlc.types.Field(BigInt, graphql_name='exchangeCount')
    exchange_count_not = sgqlc.types.Field(BigInt, graphql_name='exchangeCount_not')
    exchange_count_gt = sgqlc.types.Field(BigInt, graphql_name='exchangeCount_gt')
    exchange_count_lt = sgqlc.types.Field(BigInt, graphql_name='exchangeCount_lt')
    exchange_count_gte = sgqlc.types.Field(BigInt, graphql_name='exchangeCount_gte')
    exchange_count_lte = sgqlc.types.Field(BigInt, graphql_name='exchangeCount_lte')
    exchange_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='exchangeCount_in')
    exchange_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='exchangeCount_not_in')
    exchanges_ = sgqlc.types.Field(Exchange_filter, graphql_name='exchanges_')
    gauge_count = sgqlc.types.Field(BigInt, graphql_name='gaugeCount')
    gauge_count_not = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_not')
    gauge_count_gt = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_gt')
    gauge_count_lt = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_lt')
    gauge_count_gte = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_gte')
    gauge_count_lte = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_lte')
    gauge_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeCount_in')
    gauge_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeCount_not_in')
    gauges_ = sgqlc.types.Field(Gauge_filter, graphql_name='gauges_')
    hourly_volumes_ = sgqlc.types.Field(HourlyVolume_filter, graphql_name='hourlyVolumes_')
    daily_volumes_ = sgqlc.types.Field(DailyVolume_filter, graphql_name='dailyVolumes_')
    weekly_volumes_ = sgqlc.types.Field('WeeklyVolume_filter', graphql_name='weeklyVolumes_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class ProposalVote_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'proposal', 'proposal_not', 'proposal_gt', 'proposal_lt', 'proposal_gte', 'proposal_lte', 'proposal_in', 'proposal_not_in', 'proposal_contains', 'proposal_contains_nocase', 'proposal_not_contains', 'proposal_not_contains_nocase', 'proposal_starts_with', 'proposal_starts_with_nocase', 'proposal_not_starts_with', 'proposal_not_starts_with_nocase', 'proposal_ends_with', 'proposal_ends_with_nocase', 'proposal_not_ends_with', 'proposal_not_ends_with_nocase', 'proposal_', 'supports', 'supports_not', 'supports_in', 'supports_not_in', 'stake', 'stake_not', 'stake_gt', 'stake_lt', 'stake_gte', 'stake_lte', 'stake_in', 'stake_not_in', 'voter', 'voter_not', 'voter_gt', 'voter_lt', 'voter_gte', 'voter_lte', 'voter_in', 'voter_not_in', 'voter_contains', 'voter_contains_nocase', 'voter_not_contains', 'voter_not_contains_nocase', 'voter_starts_with', 'voter_starts_with_nocase', 'voter_not_starts_with', 'voter_not_starts_with_nocase', 'voter_ends_with', 'voter_ends_with_nocase', 'voter_not_ends_with', 'voter_not_ends_with_nocase', 'voter_', 'created', 'created_not', 'created_gt', 'created_lt', 'created_gte', 'created_lte', 'created_in', 'created_not_in', 'created_at_block', 'created_at_block_not', 'created_at_block_gt', 'created_at_block_lt', 'created_at_block_gte', 'created_at_block_lte', 'created_at_block_in', 'created_at_block_not_in', 'created_at_transaction', 'created_at_transaction_not', 'created_at_transaction_in', 'created_at_transaction_not_in', 'created_at_transaction_contains', 'created_at_transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    proposal = sgqlc.types.Field(String, graphql_name='proposal')
    proposal_not = sgqlc.types.Field(String, graphql_name='proposal_not')
    proposal_gt = sgqlc.types.Field(String, graphql_name='proposal_gt')
    proposal_lt = sgqlc.types.Field(String, graphql_name='proposal_lt')
    proposal_gte = sgqlc.types.Field(String, graphql_name='proposal_gte')
    proposal_lte = sgqlc.types.Field(String, graphql_name='proposal_lte')
    proposal_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='proposal_in')
    proposal_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='proposal_not_in')
    proposal_contains = sgqlc.types.Field(String, graphql_name='proposal_contains')
    proposal_contains_nocase = sgqlc.types.Field(String, graphql_name='proposal_contains_nocase')
    proposal_not_contains = sgqlc.types.Field(String, graphql_name='proposal_not_contains')
    proposal_not_contains_nocase = sgqlc.types.Field(String, graphql_name='proposal_not_contains_nocase')
    proposal_starts_with = sgqlc.types.Field(String, graphql_name='proposal_starts_with')
    proposal_starts_with_nocase = sgqlc.types.Field(String, graphql_name='proposal_starts_with_nocase')
    proposal_not_starts_with = sgqlc.types.Field(String, graphql_name='proposal_not_starts_with')
    proposal_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='proposal_not_starts_with_nocase')
    proposal_ends_with = sgqlc.types.Field(String, graphql_name='proposal_ends_with')
    proposal_ends_with_nocase = sgqlc.types.Field(String, graphql_name='proposal_ends_with_nocase')
    proposal_not_ends_with = sgqlc.types.Field(String, graphql_name='proposal_not_ends_with')
    proposal_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='proposal_not_ends_with_nocase')
    proposal_ = sgqlc.types.Field('Proposal_filter', graphql_name='proposal_')
    supports = sgqlc.types.Field(Boolean, graphql_name='supports')
    supports_not = sgqlc.types.Field(Boolean, graphql_name='supports_not')
    supports_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='supports_in')
    supports_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='supports_not_in')
    stake = sgqlc.types.Field(BigDecimal, graphql_name='stake')
    stake_not = sgqlc.types.Field(BigDecimal, graphql_name='stake_not')
    stake_gt = sgqlc.types.Field(BigDecimal, graphql_name='stake_gt')
    stake_lt = sgqlc.types.Field(BigDecimal, graphql_name='stake_lt')
    stake_gte = sgqlc.types.Field(BigDecimal, graphql_name='stake_gte')
    stake_lte = sgqlc.types.Field(BigDecimal, graphql_name='stake_lte')
    stake_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='stake_in')
    stake_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='stake_not_in')
    voter = sgqlc.types.Field(String, graphql_name='voter')
    voter_not = sgqlc.types.Field(String, graphql_name='voter_not')
    voter_gt = sgqlc.types.Field(String, graphql_name='voter_gt')
    voter_lt = sgqlc.types.Field(String, graphql_name='voter_lt')
    voter_gte = sgqlc.types.Field(String, graphql_name='voter_gte')
    voter_lte = sgqlc.types.Field(String, graphql_name='voter_lte')
    voter_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='voter_in')
    voter_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='voter_not_in')
    voter_contains = sgqlc.types.Field(String, graphql_name='voter_contains')
    voter_contains_nocase = sgqlc.types.Field(String, graphql_name='voter_contains_nocase')
    voter_not_contains = sgqlc.types.Field(String, graphql_name='voter_not_contains')
    voter_not_contains_nocase = sgqlc.types.Field(String, graphql_name='voter_not_contains_nocase')
    voter_starts_with = sgqlc.types.Field(String, graphql_name='voter_starts_with')
    voter_starts_with_nocase = sgqlc.types.Field(String, graphql_name='voter_starts_with_nocase')
    voter_not_starts_with = sgqlc.types.Field(String, graphql_name='voter_not_starts_with')
    voter_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='voter_not_starts_with_nocase')
    voter_ends_with = sgqlc.types.Field(String, graphql_name='voter_ends_with')
    voter_ends_with_nocase = sgqlc.types.Field(String, graphql_name='voter_ends_with_nocase')
    voter_not_ends_with = sgqlc.types.Field(String, graphql_name='voter_not_ends_with')
    voter_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='voter_not_ends_with_nocase')
    voter_ = sgqlc.types.Field(Account_filter, graphql_name='voter_')
    created = sgqlc.types.Field(BigInt, graphql_name='created')
    created_not = sgqlc.types.Field(BigInt, graphql_name='created_not')
    created_gt = sgqlc.types.Field(BigInt, graphql_name='created_gt')
    created_lt = sgqlc.types.Field(BigInt, graphql_name='created_lt')
    created_gte = sgqlc.types.Field(BigInt, graphql_name='created_gte')
    created_lte = sgqlc.types.Field(BigInt, graphql_name='created_lte')
    created_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='created_in')
    created_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='created_not_in')
    created_at_block = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock')
    created_at_block_not = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_not')
    created_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_gt')
    created_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_lt')
    created_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_gte')
    created_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_lte')
    created_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlock_in')
    created_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlock_not_in')
    created_at_transaction = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction')
    created_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_not')
    created_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='createdAtTransaction_in')
    created_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='createdAtTransaction_not_in')
    created_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_contains')
    created_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Proposal_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'number', 'number_not', 'number_gt', 'number_lt', 'number_gte', 'number_lte', 'number_in', 'number_not_in', 'app', 'app_not', 'app_gt', 'app_lt', 'app_gte', 'app_lte', 'app_in', 'app_not_in', 'app_contains', 'app_contains_nocase', 'app_not_contains', 'app_not_contains_nocase', 'app_starts_with', 'app_starts_with_nocase', 'app_not_starts_with', 'app_not_starts_with_nocase', 'app_ends_with', 'app_ends_with_nocase', 'app_not_ends_with', 'app_not_ends_with_nocase', 'app_', 'creator', 'creator_not', 'creator_gt', 'creator_lt', 'creator_gte', 'creator_lte', 'creator_in', 'creator_not_in', 'creator_contains', 'creator_contains_nocase', 'creator_not_contains', 'creator_not_contains_nocase', 'creator_starts_with', 'creator_starts_with_nocase', 'creator_not_starts_with', 'creator_not_starts_with_nocase', 'creator_ends_with', 'creator_ends_with_nocase', 'creator_not_ends_with', 'creator_not_ends_with_nocase', 'creator_', 'execution_script', 'execution_script_not', 'execution_script_in', 'execution_script_not_in', 'execution_script_contains', 'execution_script_not_contains', 'expire_date', 'expire_date_not', 'expire_date_gt', 'expire_date_lt', 'expire_date_gte', 'expire_date_lte', 'expire_date_in', 'expire_date_not_in', 'minimum_quorum', 'minimum_quorum_not', 'minimum_quorum_gt', 'minimum_quorum_lt', 'minimum_quorum_gte', 'minimum_quorum_lte', 'minimum_quorum_in', 'minimum_quorum_not_in', 'required_support', 'required_support_not', 'required_support_gt', 'required_support_lt', 'required_support_gte', 'required_support_lte', 'required_support_in', 'required_support_not_in', 'snapshot_block', 'snapshot_block_not', 'snapshot_block_gt', 'snapshot_block_lt', 'snapshot_block_gte', 'snapshot_block_lte', 'snapshot_block_in', 'snapshot_block_not_in', 'voting_power', 'voting_power_not', 'voting_power_gt', 'voting_power_lt', 'voting_power_gte', 'voting_power_lte', 'voting_power_in', 'voting_power_not_in', 'metadata', 'metadata_not', 'metadata_gt', 'metadata_lt', 'metadata_gte', 'metadata_lte', 'metadata_in', 'metadata_not_in', 'metadata_contains', 'metadata_contains_nocase', 'metadata_not_contains', 'metadata_not_contains_nocase', 'metadata_starts_with', 'metadata_starts_with_nocase', 'metadata_not_starts_with', 'metadata_not_starts_with_nocase', 'metadata_ends_with', 'metadata_ends_with_nocase', 'metadata_not_ends_with', 'metadata_not_ends_with_nocase', 'text', 'text_not', 'text_gt', 'text_lt', 'text_gte', 'text_lte', 'text_in', 'text_not_in', 'text_contains', 'text_contains_nocase', 'text_not_contains', 'text_not_contains_nocase', 'text_starts_with', 'text_starts_with_nocase', 'text_not_starts_with', 'text_not_starts_with_nocase', 'text_ends_with', 'text_ends_with_nocase', 'text_not_ends_with', 'text_not_ends_with_nocase', 'vote_count', 'vote_count_not', 'vote_count_gt', 'vote_count_lt', 'vote_count_gte', 'vote_count_lte', 'vote_count_in', 'vote_count_not_in', 'positive_vote_count', 'positive_vote_count_not', 'positive_vote_count_gt', 'positive_vote_count_lt', 'positive_vote_count_gte', 'positive_vote_count_lte', 'positive_vote_count_in', 'positive_vote_count_not_in', 'negative_vote_count', 'negative_vote_count_not', 'negative_vote_count_gt', 'negative_vote_count_lt', 'negative_vote_count_gte', 'negative_vote_count_lte', 'negative_vote_count_in', 'negative_vote_count_not_in', 'current_quorum', 'current_quorum_not', 'current_quorum_gt', 'current_quorum_lt', 'current_quorum_gte', 'current_quorum_lte', 'current_quorum_in', 'current_quorum_not_in', 'current_support', 'current_support_not', 'current_support_gt', 'current_support_lt', 'current_support_gte', 'current_support_lte', 'current_support_in', 'current_support_not_in', 'staked_support', 'staked_support_not', 'staked_support_gt', 'staked_support_lt', 'staked_support_gte', 'staked_support_lte', 'staked_support_in', 'staked_support_not_in', 'total_staked', 'total_staked_not', 'total_staked_gt', 'total_staked_lt', 'total_staked_gte', 'total_staked_lte', 'total_staked_in', 'total_staked_not_in', 'created', 'created_not', 'created_gt', 'created_lt', 'created_gte', 'created_lte', 'created_in', 'created_not_in', 'created_at_block', 'created_at_block_not', 'created_at_block_gt', 'created_at_block_lt', 'created_at_block_gte', 'created_at_block_lte', 'created_at_block_in', 'created_at_block_not_in', 'created_at_transaction', 'created_at_transaction_not', 'created_at_transaction_in', 'created_at_transaction_not_in', 'created_at_transaction_contains', 'created_at_transaction_not_contains', 'updated', 'updated_not', 'updated_gt', 'updated_lt', 'updated_gte', 'updated_lte', 'updated_in', 'updated_not_in', 'updated_at_block', 'updated_at_block_not', 'updated_at_block_gt', 'updated_at_block_lt', 'updated_at_block_gte', 'updated_at_block_lte', 'updated_at_block_in', 'updated_at_block_not_in', 'updated_at_transaction', 'updated_at_transaction_not', 'updated_at_transaction_in', 'updated_at_transaction_not_in', 'updated_at_transaction_contains', 'updated_at_transaction_not_contains', 'executed', 'executed_not', 'executed_gt', 'executed_lt', 'executed_gte', 'executed_lte', 'executed_in', 'executed_not_in', 'executed_at_block', 'executed_at_block_not', 'executed_at_block_gt', 'executed_at_block_lt', 'executed_at_block_gte', 'executed_at_block_lte', 'executed_at_block_in', 'executed_at_block_not_in', 'executed_at_transaction', 'executed_at_transaction_not', 'executed_at_transaction_in', 'executed_at_transaction_not_in', 'executed_at_transaction_contains', 'executed_at_transaction_not_contains', 'votes_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    number = sgqlc.types.Field(BigInt, graphql_name='number')
    number_not = sgqlc.types.Field(BigInt, graphql_name='number_not')
    number_gt = sgqlc.types.Field(BigInt, graphql_name='number_gt')
    number_lt = sgqlc.types.Field(BigInt, graphql_name='number_lt')
    number_gte = sgqlc.types.Field(BigInt, graphql_name='number_gte')
    number_lte = sgqlc.types.Field(BigInt, graphql_name='number_lte')
    number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='number_in')
    number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='number_not_in')
    app = sgqlc.types.Field(String, graphql_name='app')
    app_not = sgqlc.types.Field(String, graphql_name='app_not')
    app_gt = sgqlc.types.Field(String, graphql_name='app_gt')
    app_lt = sgqlc.types.Field(String, graphql_name='app_lt')
    app_gte = sgqlc.types.Field(String, graphql_name='app_gte')
    app_lte = sgqlc.types.Field(String, graphql_name='app_lte')
    app_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='app_in')
    app_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='app_not_in')
    app_contains = sgqlc.types.Field(String, graphql_name='app_contains')
    app_contains_nocase = sgqlc.types.Field(String, graphql_name='app_contains_nocase')
    app_not_contains = sgqlc.types.Field(String, graphql_name='app_not_contains')
    app_not_contains_nocase = sgqlc.types.Field(String, graphql_name='app_not_contains_nocase')
    app_starts_with = sgqlc.types.Field(String, graphql_name='app_starts_with')
    app_starts_with_nocase = sgqlc.types.Field(String, graphql_name='app_starts_with_nocase')
    app_not_starts_with = sgqlc.types.Field(String, graphql_name='app_not_starts_with')
    app_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='app_not_starts_with_nocase')
    app_ends_with = sgqlc.types.Field(String, graphql_name='app_ends_with')
    app_ends_with_nocase = sgqlc.types.Field(String, graphql_name='app_ends_with_nocase')
    app_not_ends_with = sgqlc.types.Field(String, graphql_name='app_not_ends_with')
    app_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='app_not_ends_with_nocase')
    app_ = sgqlc.types.Field('VotingApp_filter', graphql_name='app_')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    creator_not = sgqlc.types.Field(String, graphql_name='creator_not')
    creator_gt = sgqlc.types.Field(String, graphql_name='creator_gt')
    creator_lt = sgqlc.types.Field(String, graphql_name='creator_lt')
    creator_gte = sgqlc.types.Field(String, graphql_name='creator_gte')
    creator_lte = sgqlc.types.Field(String, graphql_name='creator_lte')
    creator_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='creator_in')
    creator_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='creator_not_in')
    creator_contains = sgqlc.types.Field(String, graphql_name='creator_contains')
    creator_contains_nocase = sgqlc.types.Field(String, graphql_name='creator_contains_nocase')
    creator_not_contains = sgqlc.types.Field(String, graphql_name='creator_not_contains')
    creator_not_contains_nocase = sgqlc.types.Field(String, graphql_name='creator_not_contains_nocase')
    creator_starts_with = sgqlc.types.Field(String, graphql_name='creator_starts_with')
    creator_starts_with_nocase = sgqlc.types.Field(String, graphql_name='creator_starts_with_nocase')
    creator_not_starts_with = sgqlc.types.Field(String, graphql_name='creator_not_starts_with')
    creator_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='creator_not_starts_with_nocase')
    creator_ends_with = sgqlc.types.Field(String, graphql_name='creator_ends_with')
    creator_ends_with_nocase = sgqlc.types.Field(String, graphql_name='creator_ends_with_nocase')
    creator_not_ends_with = sgqlc.types.Field(String, graphql_name='creator_not_ends_with')
    creator_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='creator_not_ends_with_nocase')
    creator_ = sgqlc.types.Field(Account_filter, graphql_name='creator_')
    execution_script = sgqlc.types.Field(Bytes, graphql_name='executionScript')
    execution_script_not = sgqlc.types.Field(Bytes, graphql_name='executionScript_not')
    execution_script_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='executionScript_in')
    execution_script_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='executionScript_not_in')
    execution_script_contains = sgqlc.types.Field(Bytes, graphql_name='executionScript_contains')
    execution_script_not_contains = sgqlc.types.Field(Bytes, graphql_name='executionScript_not_contains')
    expire_date = sgqlc.types.Field(BigInt, graphql_name='expireDate')
    expire_date_not = sgqlc.types.Field(BigInt, graphql_name='expireDate_not')
    expire_date_gt = sgqlc.types.Field(BigInt, graphql_name='expireDate_gt')
    expire_date_lt = sgqlc.types.Field(BigInt, graphql_name='expireDate_lt')
    expire_date_gte = sgqlc.types.Field(BigInt, graphql_name='expireDate_gte')
    expire_date_lte = sgqlc.types.Field(BigInt, graphql_name='expireDate_lte')
    expire_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='expireDate_in')
    expire_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='expireDate_not_in')
    minimum_quorum = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum')
    minimum_quorum_not = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_not')
    minimum_quorum_gt = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_gt')
    minimum_quorum_lt = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_lt')
    minimum_quorum_gte = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_gte')
    minimum_quorum_lte = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_lte')
    minimum_quorum_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='minimumQuorum_in')
    minimum_quorum_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='minimumQuorum_not_in')
    required_support = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport')
    required_support_not = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_not')
    required_support_gt = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_gt')
    required_support_lt = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_lt')
    required_support_gte = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_gte')
    required_support_lte = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_lte')
    required_support_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='requiredSupport_in')
    required_support_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='requiredSupport_not_in')
    snapshot_block = sgqlc.types.Field(BigInt, graphql_name='snapshotBlock')
    snapshot_block_not = sgqlc.types.Field(BigInt, graphql_name='snapshotBlock_not')
    snapshot_block_gt = sgqlc.types.Field(BigInt, graphql_name='snapshotBlock_gt')
    snapshot_block_lt = sgqlc.types.Field(BigInt, graphql_name='snapshotBlock_lt')
    snapshot_block_gte = sgqlc.types.Field(BigInt, graphql_name='snapshotBlock_gte')
    snapshot_block_lte = sgqlc.types.Field(BigInt, graphql_name='snapshotBlock_lte')
    snapshot_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='snapshotBlock_in')
    snapshot_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='snapshotBlock_not_in')
    voting_power = sgqlc.types.Field(BigDecimal, graphql_name='votingPower')
    voting_power_not = sgqlc.types.Field(BigDecimal, graphql_name='votingPower_not')
    voting_power_gt = sgqlc.types.Field(BigDecimal, graphql_name='votingPower_gt')
    voting_power_lt = sgqlc.types.Field(BigDecimal, graphql_name='votingPower_lt')
    voting_power_gte = sgqlc.types.Field(BigDecimal, graphql_name='votingPower_gte')
    voting_power_lte = sgqlc.types.Field(BigDecimal, graphql_name='votingPower_lte')
    voting_power_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='votingPower_in')
    voting_power_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='votingPower_not_in')
    metadata = sgqlc.types.Field(String, graphql_name='metadata')
    metadata_not = sgqlc.types.Field(String, graphql_name='metadata_not')
    metadata_gt = sgqlc.types.Field(String, graphql_name='metadata_gt')
    metadata_lt = sgqlc.types.Field(String, graphql_name='metadata_lt')
    metadata_gte = sgqlc.types.Field(String, graphql_name='metadata_gte')
    metadata_lte = sgqlc.types.Field(String, graphql_name='metadata_lte')
    metadata_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metadata_in')
    metadata_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metadata_not_in')
    metadata_contains = sgqlc.types.Field(String, graphql_name='metadata_contains')
    metadata_contains_nocase = sgqlc.types.Field(String, graphql_name='metadata_contains_nocase')
    metadata_not_contains = sgqlc.types.Field(String, graphql_name='metadata_not_contains')
    metadata_not_contains_nocase = sgqlc.types.Field(String, graphql_name='metadata_not_contains_nocase')
    metadata_starts_with = sgqlc.types.Field(String, graphql_name='metadata_starts_with')
    metadata_starts_with_nocase = sgqlc.types.Field(String, graphql_name='metadata_starts_with_nocase')
    metadata_not_starts_with = sgqlc.types.Field(String, graphql_name='metadata_not_starts_with')
    metadata_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='metadata_not_starts_with_nocase')
    metadata_ends_with = sgqlc.types.Field(String, graphql_name='metadata_ends_with')
    metadata_ends_with_nocase = sgqlc.types.Field(String, graphql_name='metadata_ends_with_nocase')
    metadata_not_ends_with = sgqlc.types.Field(String, graphql_name='metadata_not_ends_with')
    metadata_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='metadata_not_ends_with_nocase')
    text = sgqlc.types.Field(String, graphql_name='text')
    text_not = sgqlc.types.Field(String, graphql_name='text_not')
    text_gt = sgqlc.types.Field(String, graphql_name='text_gt')
    text_lt = sgqlc.types.Field(String, graphql_name='text_lt')
    text_gte = sgqlc.types.Field(String, graphql_name='text_gte')
    text_lte = sgqlc.types.Field(String, graphql_name='text_lte')
    text_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='text_in')
    text_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='text_not_in')
    text_contains = sgqlc.types.Field(String, graphql_name='text_contains')
    text_contains_nocase = sgqlc.types.Field(String, graphql_name='text_contains_nocase')
    text_not_contains = sgqlc.types.Field(String, graphql_name='text_not_contains')
    text_not_contains_nocase = sgqlc.types.Field(String, graphql_name='text_not_contains_nocase')
    text_starts_with = sgqlc.types.Field(String, graphql_name='text_starts_with')
    text_starts_with_nocase = sgqlc.types.Field(String, graphql_name='text_starts_with_nocase')
    text_not_starts_with = sgqlc.types.Field(String, graphql_name='text_not_starts_with')
    text_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='text_not_starts_with_nocase')
    text_ends_with = sgqlc.types.Field(String, graphql_name='text_ends_with')
    text_ends_with_nocase = sgqlc.types.Field(String, graphql_name='text_ends_with_nocase')
    text_not_ends_with = sgqlc.types.Field(String, graphql_name='text_not_ends_with')
    text_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='text_not_ends_with_nocase')
    vote_count = sgqlc.types.Field(BigInt, graphql_name='voteCount')
    vote_count_not = sgqlc.types.Field(BigInt, graphql_name='voteCount_not')
    vote_count_gt = sgqlc.types.Field(BigInt, graphql_name='voteCount_gt')
    vote_count_lt = sgqlc.types.Field(BigInt, graphql_name='voteCount_lt')
    vote_count_gte = sgqlc.types.Field(BigInt, graphql_name='voteCount_gte')
    vote_count_lte = sgqlc.types.Field(BigInt, graphql_name='voteCount_lte')
    vote_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='voteCount_in')
    vote_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='voteCount_not_in')
    positive_vote_count = sgqlc.types.Field(BigInt, graphql_name='positiveVoteCount')
    positive_vote_count_not = sgqlc.types.Field(BigInt, graphql_name='positiveVoteCount_not')
    positive_vote_count_gt = sgqlc.types.Field(BigInt, graphql_name='positiveVoteCount_gt')
    positive_vote_count_lt = sgqlc.types.Field(BigInt, graphql_name='positiveVoteCount_lt')
    positive_vote_count_gte = sgqlc.types.Field(BigInt, graphql_name='positiveVoteCount_gte')
    positive_vote_count_lte = sgqlc.types.Field(BigInt, graphql_name='positiveVoteCount_lte')
    positive_vote_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='positiveVoteCount_in')
    positive_vote_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='positiveVoteCount_not_in')
    negative_vote_count = sgqlc.types.Field(BigInt, graphql_name='negativeVoteCount')
    negative_vote_count_not = sgqlc.types.Field(BigInt, graphql_name='negativeVoteCount_not')
    negative_vote_count_gt = sgqlc.types.Field(BigInt, graphql_name='negativeVoteCount_gt')
    negative_vote_count_lt = sgqlc.types.Field(BigInt, graphql_name='negativeVoteCount_lt')
    negative_vote_count_gte = sgqlc.types.Field(BigInt, graphql_name='negativeVoteCount_gte')
    negative_vote_count_lte = sgqlc.types.Field(BigInt, graphql_name='negativeVoteCount_lte')
    negative_vote_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='negativeVoteCount_in')
    negative_vote_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='negativeVoteCount_not_in')
    current_quorum = sgqlc.types.Field(BigDecimal, graphql_name='currentQuorum')
    current_quorum_not = sgqlc.types.Field(BigDecimal, graphql_name='currentQuorum_not')
    current_quorum_gt = sgqlc.types.Field(BigDecimal, graphql_name='currentQuorum_gt')
    current_quorum_lt = sgqlc.types.Field(BigDecimal, graphql_name='currentQuorum_lt')
    current_quorum_gte = sgqlc.types.Field(BigDecimal, graphql_name='currentQuorum_gte')
    current_quorum_lte = sgqlc.types.Field(BigDecimal, graphql_name='currentQuorum_lte')
    current_quorum_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='currentQuorum_in')
    current_quorum_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='currentQuorum_not_in')
    current_support = sgqlc.types.Field(BigDecimal, graphql_name='currentSupport')
    current_support_not = sgqlc.types.Field(BigDecimal, graphql_name='currentSupport_not')
    current_support_gt = sgqlc.types.Field(BigDecimal, graphql_name='currentSupport_gt')
    current_support_lt = sgqlc.types.Field(BigDecimal, graphql_name='currentSupport_lt')
    current_support_gte = sgqlc.types.Field(BigDecimal, graphql_name='currentSupport_gte')
    current_support_lte = sgqlc.types.Field(BigDecimal, graphql_name='currentSupport_lte')
    current_support_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='currentSupport_in')
    current_support_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='currentSupport_not_in')
    staked_support = sgqlc.types.Field(BigDecimal, graphql_name='stakedSupport')
    staked_support_not = sgqlc.types.Field(BigDecimal, graphql_name='stakedSupport_not')
    staked_support_gt = sgqlc.types.Field(BigDecimal, graphql_name='stakedSupport_gt')
    staked_support_lt = sgqlc.types.Field(BigDecimal, graphql_name='stakedSupport_lt')
    staked_support_gte = sgqlc.types.Field(BigDecimal, graphql_name='stakedSupport_gte')
    staked_support_lte = sgqlc.types.Field(BigDecimal, graphql_name='stakedSupport_lte')
    staked_support_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='stakedSupport_in')
    staked_support_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='stakedSupport_not_in')
    total_staked = sgqlc.types.Field(BigDecimal, graphql_name='totalStaked')
    total_staked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalStaked_not')
    total_staked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalStaked_gt')
    total_staked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalStaked_lt')
    total_staked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalStaked_gte')
    total_staked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalStaked_lte')
    total_staked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalStaked_in')
    total_staked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalStaked_not_in')
    created = sgqlc.types.Field(BigInt, graphql_name='created')
    created_not = sgqlc.types.Field(BigInt, graphql_name='created_not')
    created_gt = sgqlc.types.Field(BigInt, graphql_name='created_gt')
    created_lt = sgqlc.types.Field(BigInt, graphql_name='created_lt')
    created_gte = sgqlc.types.Field(BigInt, graphql_name='created_gte')
    created_lte = sgqlc.types.Field(BigInt, graphql_name='created_lte')
    created_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='created_in')
    created_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='created_not_in')
    created_at_block = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock')
    created_at_block_not = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_not')
    created_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_gt')
    created_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_lt')
    created_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_gte')
    created_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlock_lte')
    created_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlock_in')
    created_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlock_not_in')
    created_at_transaction = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction')
    created_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_not')
    created_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='createdAtTransaction_in')
    created_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='createdAtTransaction_not_in')
    created_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_contains')
    created_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='createdAtTransaction_not_contains')
    updated = sgqlc.types.Field(BigInt, graphql_name='updated')
    updated_not = sgqlc.types.Field(BigInt, graphql_name='updated_not')
    updated_gt = sgqlc.types.Field(BigInt, graphql_name='updated_gt')
    updated_lt = sgqlc.types.Field(BigInt, graphql_name='updated_lt')
    updated_gte = sgqlc.types.Field(BigInt, graphql_name='updated_gte')
    updated_lte = sgqlc.types.Field(BigInt, graphql_name='updated_lte')
    updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_in')
    updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_not_in')
    updated_at_block = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock')
    updated_at_block_not = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_not')
    updated_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gt')
    updated_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lt')
    updated_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gte')
    updated_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lte')
    updated_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_in')
    updated_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_not_in')
    updated_at_transaction = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction')
    updated_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not')
    updated_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_in')
    updated_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_not_in')
    updated_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_contains')
    updated_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not_contains')
    executed = sgqlc.types.Field(BigInt, graphql_name='executed')
    executed_not = sgqlc.types.Field(BigInt, graphql_name='executed_not')
    executed_gt = sgqlc.types.Field(BigInt, graphql_name='executed_gt')
    executed_lt = sgqlc.types.Field(BigInt, graphql_name='executed_lt')
    executed_gte = sgqlc.types.Field(BigInt, graphql_name='executed_gte')
    executed_lte = sgqlc.types.Field(BigInt, graphql_name='executed_lte')
    executed_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='executed_in')
    executed_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='executed_not_in')
    executed_at_block = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock')
    executed_at_block_not = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock_not')
    executed_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock_gt')
    executed_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock_lt')
    executed_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock_gte')
    executed_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock_lte')
    executed_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='executedAtBlock_in')
    executed_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='executedAtBlock_not_in')
    executed_at_transaction = sgqlc.types.Field(Bytes, graphql_name='executedAtTransaction')
    executed_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='executedAtTransaction_not')
    executed_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='executedAtTransaction_in')
    executed_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='executedAtTransaction_not_in')
    executed_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='executedAtTransaction_contains')
    executed_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='executedAtTransaction_not_contains')
    votes_ = sgqlc.types.Field(ProposalVote_filter, graphql_name='votes_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class RemoveLiquidityEvent_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'provider', 'provider_not', 'provider_gt', 'provider_lt', 'provider_gte', 'provider_lte', 'provider_in', 'provider_not_in', 'provider_contains', 'provider_contains_nocase', 'provider_not_contains', 'provider_not_contains_nocase', 'provider_starts_with', 'provider_starts_with_nocase', 'provider_not_starts_with', 'provider_not_starts_with_nocase', 'provider_ends_with', 'provider_ends_with_nocase', 'provider_not_ends_with', 'provider_not_ends_with_nocase', 'provider_', 'token_amounts', 'token_amounts_not', 'token_amounts_contains', 'token_amounts_contains_nocase', 'token_amounts_not_contains', 'token_amounts_not_contains_nocase', 'fees', 'fees_not', 'fees_contains', 'fees_contains_nocase', 'fees_not_contains', 'fees_not_contains_nocase', 'token_supply', 'token_supply_not', 'token_supply_gt', 'token_supply_lt', 'token_supply_gte', 'token_supply_lte', 'token_supply_in', 'token_supply_not_in', 'invariant', 'invariant_not', 'invariant_gt', 'invariant_lt', 'invariant_gte', 'invariant_lte', 'invariant_in', 'invariant_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    provider = sgqlc.types.Field(String, graphql_name='provider')
    provider_not = sgqlc.types.Field(String, graphql_name='provider_not')
    provider_gt = sgqlc.types.Field(String, graphql_name='provider_gt')
    provider_lt = sgqlc.types.Field(String, graphql_name='provider_lt')
    provider_gte = sgqlc.types.Field(String, graphql_name='provider_gte')
    provider_lte = sgqlc.types.Field(String, graphql_name='provider_lte')
    provider_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_in')
    provider_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_not_in')
    provider_contains = sgqlc.types.Field(String, graphql_name='provider_contains')
    provider_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_contains_nocase')
    provider_not_contains = sgqlc.types.Field(String, graphql_name='provider_not_contains')
    provider_not_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_not_contains_nocase')
    provider_starts_with = sgqlc.types.Field(String, graphql_name='provider_starts_with')
    provider_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_starts_with_nocase')
    provider_not_starts_with = sgqlc.types.Field(String, graphql_name='provider_not_starts_with')
    provider_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_starts_with_nocase')
    provider_ends_with = sgqlc.types.Field(String, graphql_name='provider_ends_with')
    provider_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_ends_with_nocase')
    provider_not_ends_with = sgqlc.types.Field(String, graphql_name='provider_not_ends_with')
    provider_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_ends_with_nocase')
    provider_ = sgqlc.types.Field(Account_filter, graphql_name='provider_')
    token_amounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts')
    token_amounts_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_not')
    token_amounts_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_contains')
    token_amounts_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_contains_nocase')
    token_amounts_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_not_contains')
    token_amounts_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmounts_not_contains_nocase')
    fees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees')
    fees_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_not')
    fees_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_contains')
    fees_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_contains_nocase')
    fees_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_not_contains')
    fees_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees_not_contains_nocase')
    token_supply = sgqlc.types.Field(BigInt, graphql_name='tokenSupply')
    token_supply_not = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_not')
    token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_gt')
    token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_lt')
    token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_gte')
    token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='tokenSupply_lte')
    token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenSupply_in')
    token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenSupply_not_in')
    invariant = sgqlc.types.Field(BigInt, graphql_name='invariant')
    invariant_not = sgqlc.types.Field(BigInt, graphql_name='invariant_not')
    invariant_gt = sgqlc.types.Field(BigInt, graphql_name='invariant_gt')
    invariant_lt = sgqlc.types.Field(BigInt, graphql_name='invariant_lt')
    invariant_gte = sgqlc.types.Field(BigInt, graphql_name='invariant_gte')
    invariant_lte = sgqlc.types.Field(BigInt, graphql_name='invariant_lte')
    invariant_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='invariant_in')
    invariant_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='invariant_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class RemoveLiquidityOneEvent_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'provider', 'provider_not', 'provider_gt', 'provider_lt', 'provider_gte', 'provider_lte', 'provider_in', 'provider_not_in', 'provider_contains', 'provider_contains_nocase', 'provider_not_contains', 'provider_not_contains_nocase', 'provider_starts_with', 'provider_starts_with_nocase', 'provider_not_starts_with', 'provider_not_starts_with_nocase', 'provider_ends_with', 'provider_ends_with_nocase', 'provider_not_ends_with', 'provider_not_ends_with_nocase', 'provider_', 'token_amount', 'token_amount_not', 'token_amount_gt', 'token_amount_lt', 'token_amount_gte', 'token_amount_lte', 'token_amount_in', 'token_amount_not_in', 'coin_amount', 'coin_amount_not', 'coin_amount_gt', 'coin_amount_lt', 'coin_amount_gte', 'coin_amount_lte', 'coin_amount_in', 'coin_amount_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    provider = sgqlc.types.Field(String, graphql_name='provider')
    provider_not = sgqlc.types.Field(String, graphql_name='provider_not')
    provider_gt = sgqlc.types.Field(String, graphql_name='provider_gt')
    provider_lt = sgqlc.types.Field(String, graphql_name='provider_lt')
    provider_gte = sgqlc.types.Field(String, graphql_name='provider_gte')
    provider_lte = sgqlc.types.Field(String, graphql_name='provider_lte')
    provider_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_in')
    provider_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provider_not_in')
    provider_contains = sgqlc.types.Field(String, graphql_name='provider_contains')
    provider_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_contains_nocase')
    provider_not_contains = sgqlc.types.Field(String, graphql_name='provider_not_contains')
    provider_not_contains_nocase = sgqlc.types.Field(String, graphql_name='provider_not_contains_nocase')
    provider_starts_with = sgqlc.types.Field(String, graphql_name='provider_starts_with')
    provider_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_starts_with_nocase')
    provider_not_starts_with = sgqlc.types.Field(String, graphql_name='provider_not_starts_with')
    provider_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_starts_with_nocase')
    provider_ends_with = sgqlc.types.Field(String, graphql_name='provider_ends_with')
    provider_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_ends_with_nocase')
    provider_not_ends_with = sgqlc.types.Field(String, graphql_name='provider_not_ends_with')
    provider_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='provider_not_ends_with_nocase')
    provider_ = sgqlc.types.Field(Account_filter, graphql_name='provider_')
    token_amount = sgqlc.types.Field(BigInt, graphql_name='tokenAmount')
    token_amount_not = sgqlc.types.Field(BigInt, graphql_name='tokenAmount_not')
    token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='tokenAmount_gt')
    token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='tokenAmount_lt')
    token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='tokenAmount_gte')
    token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='tokenAmount_lte')
    token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmount_in')
    token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenAmount_not_in')
    coin_amount = sgqlc.types.Field(BigInt, graphql_name='coinAmount')
    coin_amount_not = sgqlc.types.Field(BigInt, graphql_name='coinAmount_not')
    coin_amount_gt = sgqlc.types.Field(BigInt, graphql_name='coinAmount_gt')
    coin_amount_lt = sgqlc.types.Field(BigInt, graphql_name='coinAmount_lt')
    coin_amount_gte = sgqlc.types.Field(BigInt, graphql_name='coinAmount_gte')
    coin_amount_lte = sgqlc.types.Field(BigInt, graphql_name='coinAmount_lte')
    coin_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='coinAmount_in')
    coin_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='coinAmount_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class SystemState_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'registry_contract', 'registry_contract_not', 'registry_contract_in', 'registry_contract_not_in', 'registry_contract_contains', 'registry_contract_not_contains', 'contract_count', 'contract_count_not', 'contract_count_gt', 'contract_count_lt', 'contract_count_gte', 'contract_count_lte', 'contract_count_in', 'contract_count_not_in', 'gauge_count', 'gauge_count_not', 'gauge_count_gt', 'gauge_count_lt', 'gauge_count_gte', 'gauge_count_lte', 'gauge_count_in', 'gauge_count_not_in', 'gauge_type_count', 'gauge_type_count_not', 'gauge_type_count_gt', 'gauge_type_count_lt', 'gauge_type_count_gte', 'gauge_type_count_lte', 'gauge_type_count_in', 'gauge_type_count_not_in', 'pool_count', 'pool_count_not', 'pool_count_gt', 'pool_count_lt', 'pool_count_gte', 'pool_count_lte', 'pool_count_in', 'pool_count_not_in', 'token_count', 'token_count_not', 'token_count_gt', 'token_count_lt', 'token_count_gte', 'token_count_lte', 'token_count_in', 'token_count_not_in', 'total_pool_count', 'total_pool_count_not', 'total_pool_count_gt', 'total_pool_count_lt', 'total_pool_count_gte', 'total_pool_count_lte', 'total_pool_count_in', 'total_pool_count_not_in', 'updated', 'updated_not', 'updated_gt', 'updated_lt', 'updated_gte', 'updated_lte', 'updated_in', 'updated_not_in', 'updated_at_block', 'updated_at_block_not', 'updated_at_block_gt', 'updated_at_block_lt', 'updated_at_block_gte', 'updated_at_block_lte', 'updated_at_block_in', 'updated_at_block_not_in', 'updated_at_transaction', 'updated_at_transaction_not', 'updated_at_transaction_in', 'updated_at_transaction_not_in', 'updated_at_transaction_contains', 'updated_at_transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    registry_contract = sgqlc.types.Field(Bytes, graphql_name='registryContract')
    registry_contract_not = sgqlc.types.Field(Bytes, graphql_name='registryContract_not')
    registry_contract_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='registryContract_in')
    registry_contract_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='registryContract_not_in')
    registry_contract_contains = sgqlc.types.Field(Bytes, graphql_name='registryContract_contains')
    registry_contract_not_contains = sgqlc.types.Field(Bytes, graphql_name='registryContract_not_contains')
    contract_count = sgqlc.types.Field(BigInt, graphql_name='contractCount')
    contract_count_not = sgqlc.types.Field(BigInt, graphql_name='contractCount_not')
    contract_count_gt = sgqlc.types.Field(BigInt, graphql_name='contractCount_gt')
    contract_count_lt = sgqlc.types.Field(BigInt, graphql_name='contractCount_lt')
    contract_count_gte = sgqlc.types.Field(BigInt, graphql_name='contractCount_gte')
    contract_count_lte = sgqlc.types.Field(BigInt, graphql_name='contractCount_lte')
    contract_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='contractCount_in')
    contract_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='contractCount_not_in')
    gauge_count = sgqlc.types.Field(BigInt, graphql_name='gaugeCount')
    gauge_count_not = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_not')
    gauge_count_gt = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_gt')
    gauge_count_lt = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_lt')
    gauge_count_gte = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_gte')
    gauge_count_lte = sgqlc.types.Field(BigInt, graphql_name='gaugeCount_lte')
    gauge_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeCount_in')
    gauge_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeCount_not_in')
    gauge_type_count = sgqlc.types.Field(BigInt, graphql_name='gaugeTypeCount')
    gauge_type_count_not = sgqlc.types.Field(BigInt, graphql_name='gaugeTypeCount_not')
    gauge_type_count_gt = sgqlc.types.Field(BigInt, graphql_name='gaugeTypeCount_gt')
    gauge_type_count_lt = sgqlc.types.Field(BigInt, graphql_name='gaugeTypeCount_lt')
    gauge_type_count_gte = sgqlc.types.Field(BigInt, graphql_name='gaugeTypeCount_gte')
    gauge_type_count_lte = sgqlc.types.Field(BigInt, graphql_name='gaugeTypeCount_lte')
    gauge_type_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeTypeCount_in')
    gauge_type_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gaugeTypeCount_not_in')
    pool_count = sgqlc.types.Field(BigInt, graphql_name='poolCount')
    pool_count_not = sgqlc.types.Field(BigInt, graphql_name='poolCount_not')
    pool_count_gt = sgqlc.types.Field(BigInt, graphql_name='poolCount_gt')
    pool_count_lt = sgqlc.types.Field(BigInt, graphql_name='poolCount_lt')
    pool_count_gte = sgqlc.types.Field(BigInt, graphql_name='poolCount_gte')
    pool_count_lte = sgqlc.types.Field(BigInt, graphql_name='poolCount_lte')
    pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='poolCount_in')
    pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='poolCount_not_in')
    token_count = sgqlc.types.Field(BigInt, graphql_name='tokenCount')
    token_count_not = sgqlc.types.Field(BigInt, graphql_name='tokenCount_not')
    token_count_gt = sgqlc.types.Field(BigInt, graphql_name='tokenCount_gt')
    token_count_lt = sgqlc.types.Field(BigInt, graphql_name='tokenCount_lt')
    token_count_gte = sgqlc.types.Field(BigInt, graphql_name='tokenCount_gte')
    token_count_lte = sgqlc.types.Field(BigInt, graphql_name='tokenCount_lte')
    token_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenCount_in')
    token_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenCount_not_in')
    total_pool_count = sgqlc.types.Field(BigInt, graphql_name='totalPoolCount')
    total_pool_count_not = sgqlc.types.Field(BigInt, graphql_name='totalPoolCount_not')
    total_pool_count_gt = sgqlc.types.Field(BigInt, graphql_name='totalPoolCount_gt')
    total_pool_count_lt = sgqlc.types.Field(BigInt, graphql_name='totalPoolCount_lt')
    total_pool_count_gte = sgqlc.types.Field(BigInt, graphql_name='totalPoolCount_gte')
    total_pool_count_lte = sgqlc.types.Field(BigInt, graphql_name='totalPoolCount_lte')
    total_pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalPoolCount_in')
    total_pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalPoolCount_not_in')
    updated = sgqlc.types.Field(BigInt, graphql_name='updated')
    updated_not = sgqlc.types.Field(BigInt, graphql_name='updated_not')
    updated_gt = sgqlc.types.Field(BigInt, graphql_name='updated_gt')
    updated_lt = sgqlc.types.Field(BigInt, graphql_name='updated_lt')
    updated_gte = sgqlc.types.Field(BigInt, graphql_name='updated_gte')
    updated_lte = sgqlc.types.Field(BigInt, graphql_name='updated_lte')
    updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_in')
    updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_not_in')
    updated_at_block = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock')
    updated_at_block_not = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_not')
    updated_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gt')
    updated_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lt')
    updated_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gte')
    updated_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lte')
    updated_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_in')
    updated_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_not_in')
    updated_at_transaction = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction')
    updated_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not')
    updated_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_in')
    updated_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_not_in')
    updated_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_contains')
    updated_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Token_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'pools', 'pools_not', 'pools_contains', 'pools_contains_nocase', 'pools_not_contains', 'pools_not_contains_nocase', 'pools_', 'coins_', 'underlying_coins_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    decimals = sgqlc.types.Field(BigInt, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(BigInt, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(BigInt, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(BigInt, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(BigInt, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(BigInt, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    symbol_not = sgqlc.types.Field(String, graphql_name='symbol_not')
    symbol_gt = sgqlc.types.Field(String, graphql_name='symbol_gt')
    symbol_lt = sgqlc.types.Field(String, graphql_name='symbol_lt')
    symbol_gte = sgqlc.types.Field(String, graphql_name='symbol_gte')
    symbol_lte = sgqlc.types.Field(String, graphql_name='symbol_lte')
    symbol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_in')
    symbol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_not_in')
    symbol_contains = sgqlc.types.Field(String, graphql_name='symbol_contains')
    symbol_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_contains_nocase')
    symbol_not_contains = sgqlc.types.Field(String, graphql_name='symbol_not_contains')
    symbol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_contains_nocase')
    symbol_starts_with = sgqlc.types.Field(String, graphql_name='symbol_starts_with')
    symbol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_starts_with_nocase')
    symbol_not_starts_with = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with')
    symbol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with_nocase')
    symbol_ends_with = sgqlc.types.Field(String, graphql_name='symbol_ends_with')
    symbol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_ends_with_nocase')
    symbol_not_ends_with = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with')
    symbol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with_nocase')
    pools = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pools')
    pools_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pools_not')
    pools_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pools_contains')
    pools_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pools_contains_nocase')
    pools_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pools_not_contains')
    pools_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pools_not_contains_nocase')
    pools_ = sgqlc.types.Field(Pool_filter, graphql_name='pools_')
    coins_ = sgqlc.types.Field(Coin_filter, graphql_name='coins_')
    underlying_coins_ = sgqlc.types.Field('UnderlyingCoin_filter', graphql_name='underlyingCoins_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class TradeVolume_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', '_change_block')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class TransferOwnershipEvent_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'new_admin', 'new_admin_not', 'new_admin_in', 'new_admin_not_in', 'new_admin_contains', 'new_admin_not_contains', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'transaction', 'transaction_not', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    new_admin = sgqlc.types.Field(Bytes, graphql_name='newAdmin')
    new_admin_not = sgqlc.types.Field(Bytes, graphql_name='newAdmin_not')
    new_admin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='newAdmin_in')
    new_admin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='newAdmin_not_in')
    new_admin_contains = sgqlc.types.Field(Bytes, graphql_name='newAdmin_contains')
    new_admin_not_contains = sgqlc.types.Field(Bytes, graphql_name='newAdmin_not_contains')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    transaction = sgqlc.types.Field(Bytes, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(Bytes, graphql_name='transaction_not')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_contains')
    transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='transaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class UnderlyingCoin_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'index', 'index_not', 'index_gt', 'index_lt', 'index_gte', 'index_lte', 'index_in', 'index_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'coin', 'coin_not', 'coin_gt', 'coin_lt', 'coin_gte', 'coin_lte', 'coin_in', 'coin_not_in', 'coin_contains', 'coin_contains_nocase', 'coin_not_contains', 'coin_not_contains_nocase', 'coin_starts_with', 'coin_starts_with_nocase', 'coin_not_starts_with', 'coin_not_starts_with_nocase', 'coin_ends_with', 'coin_ends_with_nocase', 'coin_not_ends_with', 'coin_not_ends_with_nocase', 'coin_', 'balance', 'balance_not', 'balance_gt', 'balance_lt', 'balance_gte', 'balance_lte', 'balance_in', 'balance_not_in', 'updated', 'updated_not', 'updated_gt', 'updated_lt', 'updated_gte', 'updated_lte', 'updated_in', 'updated_not_in', 'updated_at_block', 'updated_at_block_not', 'updated_at_block_gt', 'updated_at_block_lt', 'updated_at_block_gte', 'updated_at_block_lte', 'updated_at_block_in', 'updated_at_block_not_in', 'updated_at_transaction', 'updated_at_transaction_not', 'updated_at_transaction_in', 'updated_at_transaction_not_in', 'updated_at_transaction_contains', 'updated_at_transaction_not_contains', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    index = sgqlc.types.Field(Int, graphql_name='index')
    index_not = sgqlc.types.Field(Int, graphql_name='index_not')
    index_gt = sgqlc.types.Field(Int, graphql_name='index_gt')
    index_lt = sgqlc.types.Field(Int, graphql_name='index_lt')
    index_gte = sgqlc.types.Field(Int, graphql_name='index_gte')
    index_lte = sgqlc.types.Field(Int, graphql_name='index_lte')
    index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='index_in')
    index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='index_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    token = sgqlc.types.Field(String, graphql_name='token')
    token_not = sgqlc.types.Field(String, graphql_name='token_not')
    token_gt = sgqlc.types.Field(String, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(String, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(String, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(String, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(String, graphql_name='token_contains')
    token_contains_nocase = sgqlc.types.Field(String, graphql_name='token_contains_nocase')
    token_not_contains = sgqlc.types.Field(String, graphql_name='token_not_contains')
    token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token_not_contains_nocase')
    token_starts_with = sgqlc.types.Field(String, graphql_name='token_starts_with')
    token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_starts_with_nocase')
    token_not_starts_with = sgqlc.types.Field(String, graphql_name='token_not_starts_with')
    token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_starts_with_nocase')
    token_ends_with = sgqlc.types.Field(String, graphql_name='token_ends_with')
    token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_ends_with_nocase')
    token_not_ends_with = sgqlc.types.Field(String, graphql_name='token_not_ends_with')
    token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_ends_with_nocase')
    token_ = sgqlc.types.Field(Token_filter, graphql_name='token_')
    coin = sgqlc.types.Field(String, graphql_name='coin')
    coin_not = sgqlc.types.Field(String, graphql_name='coin_not')
    coin_gt = sgqlc.types.Field(String, graphql_name='coin_gt')
    coin_lt = sgqlc.types.Field(String, graphql_name='coin_lt')
    coin_gte = sgqlc.types.Field(String, graphql_name='coin_gte')
    coin_lte = sgqlc.types.Field(String, graphql_name='coin_lte')
    coin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='coin_in')
    coin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='coin_not_in')
    coin_contains = sgqlc.types.Field(String, graphql_name='coin_contains')
    coin_contains_nocase = sgqlc.types.Field(String, graphql_name='coin_contains_nocase')
    coin_not_contains = sgqlc.types.Field(String, graphql_name='coin_not_contains')
    coin_not_contains_nocase = sgqlc.types.Field(String, graphql_name='coin_not_contains_nocase')
    coin_starts_with = sgqlc.types.Field(String, graphql_name='coin_starts_with')
    coin_starts_with_nocase = sgqlc.types.Field(String, graphql_name='coin_starts_with_nocase')
    coin_not_starts_with = sgqlc.types.Field(String, graphql_name='coin_not_starts_with')
    coin_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='coin_not_starts_with_nocase')
    coin_ends_with = sgqlc.types.Field(String, graphql_name='coin_ends_with')
    coin_ends_with_nocase = sgqlc.types.Field(String, graphql_name='coin_ends_with_nocase')
    coin_not_ends_with = sgqlc.types.Field(String, graphql_name='coin_not_ends_with')
    coin_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='coin_not_ends_with_nocase')
    coin_ = sgqlc.types.Field(Coin_filter, graphql_name='coin_')
    balance = sgqlc.types.Field(BigDecimal, graphql_name='balance')
    balance_not = sgqlc.types.Field(BigDecimal, graphql_name='balance_not')
    balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='balance_gt')
    balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='balance_lt')
    balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='balance_gte')
    balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='balance_lte')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_in')
    balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_not_in')
    updated = sgqlc.types.Field(BigInt, graphql_name='updated')
    updated_not = sgqlc.types.Field(BigInt, graphql_name='updated_not')
    updated_gt = sgqlc.types.Field(BigInt, graphql_name='updated_gt')
    updated_lt = sgqlc.types.Field(BigInt, graphql_name='updated_lt')
    updated_gte = sgqlc.types.Field(BigInt, graphql_name='updated_gte')
    updated_lte = sgqlc.types.Field(BigInt, graphql_name='updated_lte')
    updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_in')
    updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updated_not_in')
    updated_at_block = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock')
    updated_at_block_not = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_not')
    updated_at_block_gt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gt')
    updated_at_block_lt = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lt')
    updated_at_block_gte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_gte')
    updated_at_block_lte = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock_lte')
    updated_at_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_in')
    updated_at_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='updatedAtBlock_not_in')
    updated_at_transaction = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction')
    updated_at_transaction_not = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not')
    updated_at_transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_in')
    updated_at_transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='updatedAtTransaction_not_in')
    updated_at_transaction_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_contains')
    updated_at_transaction_not_contains = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class VotingApp_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'codename', 'codename_not', 'codename_gt', 'codename_lt', 'codename_gte', 'codename_lte', 'codename_in', 'codename_not_in', 'codename_contains', 'codename_contains_nocase', 'codename_not_contains', 'codename_not_contains_nocase', 'codename_starts_with', 'codename_starts_with_nocase', 'codename_not_starts_with', 'codename_not_starts_with_nocase', 'codename_ends_with', 'codename_ends_with_nocase', 'codename_not_ends_with', 'codename_not_ends_with_nocase', 'minimum_balance', 'minimum_balance_not', 'minimum_balance_gt', 'minimum_balance_lt', 'minimum_balance_gte', 'minimum_balance_lte', 'minimum_balance_in', 'minimum_balance_not_in', 'minimum_quorum', 'minimum_quorum_not', 'minimum_quorum_gt', 'minimum_quorum_lt', 'minimum_quorum_gte', 'minimum_quorum_lte', 'minimum_quorum_in', 'minimum_quorum_not_in', 'minimum_time', 'minimum_time_not', 'minimum_time_gt', 'minimum_time_lt', 'minimum_time_gte', 'minimum_time_lte', 'minimum_time_in', 'minimum_time_not_in', 'required_support', 'required_support_not', 'required_support_gt', 'required_support_lt', 'required_support_gte', 'required_support_lte', 'required_support_in', 'required_support_not_in', 'vote_time', 'vote_time_not', 'vote_time_gt', 'vote_time_lt', 'vote_time_gte', 'vote_time_lte', 'vote_time_in', 'vote_time_not_in', 'proposal_count', 'proposal_count_not', 'proposal_count_gt', 'proposal_count_lt', 'proposal_count_gte', 'proposal_count_lte', 'proposal_count_in', 'proposal_count_not_in', 'vote_count', 'vote_count_not', 'vote_count_gt', 'vote_count_lt', 'vote_count_gte', 'vote_count_lte', 'vote_count_in', 'vote_count_not_in', 'token', 'token_not', 'token_in', 'token_not_in', 'token_contains', 'token_not_contains', 'proposals_', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    codename = sgqlc.types.Field(String, graphql_name='codename')
    codename_not = sgqlc.types.Field(String, graphql_name='codename_not')
    codename_gt = sgqlc.types.Field(String, graphql_name='codename_gt')
    codename_lt = sgqlc.types.Field(String, graphql_name='codename_lt')
    codename_gte = sgqlc.types.Field(String, graphql_name='codename_gte')
    codename_lte = sgqlc.types.Field(String, graphql_name='codename_lte')
    codename_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='codename_in')
    codename_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='codename_not_in')
    codename_contains = sgqlc.types.Field(String, graphql_name='codename_contains')
    codename_contains_nocase = sgqlc.types.Field(String, graphql_name='codename_contains_nocase')
    codename_not_contains = sgqlc.types.Field(String, graphql_name='codename_not_contains')
    codename_not_contains_nocase = sgqlc.types.Field(String, graphql_name='codename_not_contains_nocase')
    codename_starts_with = sgqlc.types.Field(String, graphql_name='codename_starts_with')
    codename_starts_with_nocase = sgqlc.types.Field(String, graphql_name='codename_starts_with_nocase')
    codename_not_starts_with = sgqlc.types.Field(String, graphql_name='codename_not_starts_with')
    codename_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='codename_not_starts_with_nocase')
    codename_ends_with = sgqlc.types.Field(String, graphql_name='codename_ends_with')
    codename_ends_with_nocase = sgqlc.types.Field(String, graphql_name='codename_ends_with_nocase')
    codename_not_ends_with = sgqlc.types.Field(String, graphql_name='codename_not_ends_with')
    codename_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='codename_not_ends_with_nocase')
    minimum_balance = sgqlc.types.Field(BigDecimal, graphql_name='minimumBalance')
    minimum_balance_not = sgqlc.types.Field(BigDecimal, graphql_name='minimumBalance_not')
    minimum_balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='minimumBalance_gt')
    minimum_balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='minimumBalance_lt')
    minimum_balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='minimumBalance_gte')
    minimum_balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='minimumBalance_lte')
    minimum_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='minimumBalance_in')
    minimum_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='minimumBalance_not_in')
    minimum_quorum = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum')
    minimum_quorum_not = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_not')
    minimum_quorum_gt = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_gt')
    minimum_quorum_lt = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_lt')
    minimum_quorum_gte = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_gte')
    minimum_quorum_lte = sgqlc.types.Field(BigDecimal, graphql_name='minimumQuorum_lte')
    minimum_quorum_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='minimumQuorum_in')
    minimum_quorum_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='minimumQuorum_not_in')
    minimum_time = sgqlc.types.Field(BigInt, graphql_name='minimumTime')
    minimum_time_not = sgqlc.types.Field(BigInt, graphql_name='minimumTime_not')
    minimum_time_gt = sgqlc.types.Field(BigInt, graphql_name='minimumTime_gt')
    minimum_time_lt = sgqlc.types.Field(BigInt, graphql_name='minimumTime_lt')
    minimum_time_gte = sgqlc.types.Field(BigInt, graphql_name='minimumTime_gte')
    minimum_time_lte = sgqlc.types.Field(BigInt, graphql_name='minimumTime_lte')
    minimum_time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='minimumTime_in')
    minimum_time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='minimumTime_not_in')
    required_support = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport')
    required_support_not = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_not')
    required_support_gt = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_gt')
    required_support_lt = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_lt')
    required_support_gte = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_gte')
    required_support_lte = sgqlc.types.Field(BigDecimal, graphql_name='requiredSupport_lte')
    required_support_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='requiredSupport_in')
    required_support_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='requiredSupport_not_in')
    vote_time = sgqlc.types.Field(BigInt, graphql_name='voteTime')
    vote_time_not = sgqlc.types.Field(BigInt, graphql_name='voteTime_not')
    vote_time_gt = sgqlc.types.Field(BigInt, graphql_name='voteTime_gt')
    vote_time_lt = sgqlc.types.Field(BigInt, graphql_name='voteTime_lt')
    vote_time_gte = sgqlc.types.Field(BigInt, graphql_name='voteTime_gte')
    vote_time_lte = sgqlc.types.Field(BigInt, graphql_name='voteTime_lte')
    vote_time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='voteTime_in')
    vote_time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='voteTime_not_in')
    proposal_count = sgqlc.types.Field(BigInt, graphql_name='proposalCount')
    proposal_count_not = sgqlc.types.Field(BigInt, graphql_name='proposalCount_not')
    proposal_count_gt = sgqlc.types.Field(BigInt, graphql_name='proposalCount_gt')
    proposal_count_lt = sgqlc.types.Field(BigInt, graphql_name='proposalCount_lt')
    proposal_count_gte = sgqlc.types.Field(BigInt, graphql_name='proposalCount_gte')
    proposal_count_lte = sgqlc.types.Field(BigInt, graphql_name='proposalCount_lte')
    proposal_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='proposalCount_in')
    proposal_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='proposalCount_not_in')
    vote_count = sgqlc.types.Field(BigInt, graphql_name='voteCount')
    vote_count_not = sgqlc.types.Field(BigInt, graphql_name='voteCount_not')
    vote_count_gt = sgqlc.types.Field(BigInt, graphql_name='voteCount_gt')
    vote_count_lt = sgqlc.types.Field(BigInt, graphql_name='voteCount_lt')
    vote_count_gte = sgqlc.types.Field(BigInt, graphql_name='voteCount_gte')
    vote_count_lte = sgqlc.types.Field(BigInt, graphql_name='voteCount_lte')
    vote_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='voteCount_in')
    vote_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='voteCount_not_in')
    token = sgqlc.types.Field(Bytes, graphql_name='token')
    token_not = sgqlc.types.Field(Bytes, graphql_name='token_not')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(Bytes, graphql_name='token_contains')
    token_not_contains = sgqlc.types.Field(Bytes, graphql_name='token_not_contains')
    proposals_ = sgqlc.types.Field(Proposal_filter, graphql_name='proposals_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class WeeklyVolume_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')



########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'gauges', 'gauge_weight_votes', 'proposals', 'proposal_votes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    gauges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GaugeLiquidity')), graphql_name='gauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeLiquidity_filter, graphql_name='where', default=None)),
))
    )
    gauge_weight_votes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GaugeWeightVote')), graphql_name='gaugeWeightVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeightVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeightVote_filter, graphql_name='where', default=None)),
))
    )
    proposals = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Proposal')), graphql_name='proposals', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Proposal_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Proposal_filter, graphql_name='where', default=None)),
))
    )
    proposal_votes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProposalVote')), graphql_name='proposalVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ProposalVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ProposalVote_filter, graphql_name='where', default=None)),
))
    )


class Coin(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'index', 'pool', 'token', 'underlying', 'balance', 'rate', 'updated', 'updated_at_block', 'updated_at_transaction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    pool = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='pool')
    token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token')
    underlying = sgqlc.types.Field(sgqlc.types.non_null('UnderlyingCoin'), graphql_name='underlying')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')
    rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='rate')
    updated = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='updated')
    updated_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='updatedAtBlock')
    updated_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='updatedAtTransaction')


class Contract(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'description', 'added', 'added_at_block', 'added_at_transaction', 'modified', 'modified_at_block', 'modified_at_transaction', 'versions')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(String, graphql_name='description')
    added = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='added')
    added_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='addedAtBlock')
    added_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='addedAtTransaction')
    modified = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='modified')
    modified_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='modifiedAtBlock')
    modified_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='modifiedAtTransaction')
    versions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ContractVersion')), graphql_name='versions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ContractVersion_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ContractVersion_filter, graphql_name='where', default=None)),
))
    )


class ContractVersion(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'contract', 'address', 'version', 'added', 'added_at_block', 'added_at_transaction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    contract = sgqlc.types.Field(sgqlc.types.non_null(Contract), graphql_name='contract')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    version = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='version')
    added = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='added')
    added_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='addedAtBlock')
    added_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='addedAtTransaction')


class Gauge(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'type', 'pool', 'created', 'created_at_block', 'created_at_transaction', 'weights', 'weight_votes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    type = sgqlc.types.Field(sgqlc.types.non_null('GaugeType'), graphql_name='type')
    pool = sgqlc.types.Field('Pool', graphql_name='pool')
    created = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='created')
    created_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtBlock')
    created_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='createdAtTransaction')
    weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GaugeWeight')), graphql_name='weights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeight_filter, graphql_name='where', default=None)),
))
    )
    weight_votes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GaugeWeightVote')), graphql_name='weightVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeightVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeightVote_filter, graphql_name='where', default=None)),
))
    )


class GaugeDeposit(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'gauge', 'provider', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    gauge = sgqlc.types.Field(sgqlc.types.non_null(Gauge), graphql_name='gauge')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='provider')
    value = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='value')


class GaugeLiquidity(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'user', 'gauge', 'original_balance', 'original_supply', 'working_balance', 'working_supply', 'timestamp', 'block', 'transaction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='user')
    gauge = sgqlc.types.Field(sgqlc.types.non_null(Gauge), graphql_name='gauge')
    original_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='originalBalance')
    original_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='originalSupply')
    working_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='workingBalance')
    working_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='workingSupply')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='block')
    transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='transaction')


class GaugeTotalWeight(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'time', 'weight')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    time = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='time')
    weight = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='weight')


class GaugeType(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'name', 'gauge_count', 'gauges', 'weights')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gauge_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='gaugeCount')
    gauges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Gauge)), graphql_name='gauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Gauge_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Gauge_filter, graphql_name='where', default=None)),
))
    )
    weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GaugeTypeWeight')), graphql_name='weights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeTypeWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeTypeWeight_filter, graphql_name='where', default=None)),
))
    )


class GaugeTypeWeight(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'type', 'time', 'weight')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(GaugeType), graphql_name='type')
    time = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='time')
    weight = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='weight')


class GaugeWeight(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'gauge', 'time', 'weight')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    gauge = sgqlc.types.Field(sgqlc.types.non_null(Gauge), graphql_name='gauge')
    time = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='time')
    weight = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='weight')


class GaugeWeightVote(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'gauge', 'user', 'time', 'weight')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    gauge = sgqlc.types.Field(sgqlc.types.non_null(Gauge), graphql_name='gauge')
    user = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='user')
    time = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='time')
    weight = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='weight')


class GaugeWithdraw(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'gauge', 'provider', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    gauge = sgqlc.types.Field(sgqlc.types.non_null(Gauge), graphql_name='gauge')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='provider')
    value = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='value')


class LpToken(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'decimals', 'name', 'symbol', 'gauge', 'pool')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='decimals')
    name = sgqlc.types.Field(String, graphql_name='name')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    gauge = sgqlc.types.Field(Gauge, graphql_name='gauge')
    pool = sgqlc.types.Field('Pool', graphql_name='pool')


class Pool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'name', 'asset_type', 'is_meta', 'registry_address', 'swap_address', 'lp_token', 'coin_count', 'coins', 'underlying_count', 'underlying_coins', 'a', 'fee', 'admin_fee', 'owner', 'virtual_price', 'locked', 'added_at', 'added_at_block', 'added_at_transaction', 'removed_at', 'removed_at_block', 'removed_at_transaction', 'events', 'exchange_count', 'exchanges', 'gauge_count', 'gauges', 'hourly_volumes', 'daily_volumes', 'weekly_volumes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    asset_type = sgqlc.types.Field(AssetType, graphql_name='assetType')
    is_meta = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMeta')
    registry_address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='registryAddress')
    swap_address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='swapAddress')
    lp_token = sgqlc.types.Field(sgqlc.types.non_null(LpToken), graphql_name='lpToken')
    coin_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='coinCount')
    coins = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Coin)), graphql_name='coins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Coin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Coin_filter, graphql_name='where', default=None)),
))
    )
    underlying_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='underlyingCount')
    underlying_coins = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UnderlyingCoin')), graphql_name='underlyingCoins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UnderlyingCoin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UnderlyingCoin_filter, graphql_name='where', default=None)),
))
    )
    a = sgqlc.types.Field(BigInt, graphql_name='A')
    fee = sgqlc.types.Field(BigDecimal, graphql_name='fee')
    admin_fee = sgqlc.types.Field(BigDecimal, graphql_name='adminFee')
    owner = sgqlc.types.Field(Bytes, graphql_name='owner')
    virtual_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='virtualPrice')
    locked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='locked')
    added_at = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='addedAt')
    added_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='addedAtBlock')
    added_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='addedAtTransaction')
    removed_at = sgqlc.types.Field(BigInt, graphql_name='removedAt')
    removed_at_block = sgqlc.types.Field(BigInt, graphql_name='removedAtBlock')
    removed_at_transaction = sgqlc.types.Field(Bytes, graphql_name='removedAtTransaction')
    events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PoolEvent')), graphql_name='events', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolEvent_filter, graphql_name='where', default=None)),
))
    )
    exchange_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='exchangeCount')
    exchanges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Exchange')), graphql_name='exchanges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Exchange_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Exchange_filter, graphql_name='where', default=None)),
))
    )
    gauge_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='gaugeCount')
    gauges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Gauge)), graphql_name='gauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Gauge_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Gauge_filter, graphql_name='where', default=None)),
))
    )
    hourly_volumes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('HourlyVolume')), graphql_name='hourlyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(HourlyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(HourlyVolume_filter, graphql_name='where', default=None)),
))
    )
    daily_volumes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DailyVolume')), graphql_name='dailyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DailyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DailyVolume_filter, graphql_name='where', default=None)),
))
    )
    weekly_volumes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WeeklyVolume')), graphql_name='weeklyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WeeklyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WeeklyVolume_filter, graphql_name='where', default=None)),
))
    )


class PoolEvent(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('pool', 'block', 'timestamp', 'transaction')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='block')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='transaction')


class Proposal(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'number', 'app', 'creator', 'execution_script', 'expire_date', 'minimum_quorum', 'required_support', 'snapshot_block', 'voting_power', 'metadata', 'text', 'vote_count', 'positive_vote_count', 'negative_vote_count', 'current_quorum', 'current_support', 'staked_support', 'total_staked', 'created', 'created_at_block', 'created_at_transaction', 'updated', 'updated_at_block', 'updated_at_transaction', 'executed', 'executed_at_block', 'executed_at_transaction', 'votes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='number')
    app = sgqlc.types.Field(sgqlc.types.non_null('VotingApp'), graphql_name='app')
    creator = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='creator')
    execution_script = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='executionScript')
    expire_date = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='expireDate')
    minimum_quorum = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='minimumQuorum')
    required_support = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='requiredSupport')
    snapshot_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='snapshotBlock')
    voting_power = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='votingPower')
    metadata = sgqlc.types.Field(String, graphql_name='metadata')
    text = sgqlc.types.Field(String, graphql_name='text')
    vote_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='voteCount')
    positive_vote_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='positiveVoteCount')
    negative_vote_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='negativeVoteCount')
    current_quorum = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='currentQuorum')
    current_support = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='currentSupport')
    staked_support = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='stakedSupport')
    total_staked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalStaked')
    created = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='created')
    created_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtBlock')
    created_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='createdAtTransaction')
    updated = sgqlc.types.Field(BigInt, graphql_name='updated')
    updated_at_block = sgqlc.types.Field(BigInt, graphql_name='updatedAtBlock')
    updated_at_transaction = sgqlc.types.Field(Bytes, graphql_name='updatedAtTransaction')
    executed = sgqlc.types.Field(BigInt, graphql_name='executed')
    executed_at_block = sgqlc.types.Field(BigInt, graphql_name='executedAtBlock')
    executed_at_transaction = sgqlc.types.Field(Bytes, graphql_name='executedAtTransaction')
    votes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProposalVote')), graphql_name='votes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ProposalVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ProposalVote_filter, graphql_name='where', default=None)),
))
    )


class ProposalVote(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'proposal', 'supports', 'stake', 'voter', 'created', 'created_at_block', 'created_at_transaction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    proposal = sgqlc.types.Field(sgqlc.types.non_null(Proposal), graphql_name='proposal')
    supports = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='supports')
    stake = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='stake')
    voter = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='voter')
    created = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='created')
    created_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtBlock')
    created_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='createdAtTransaction')


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('system_state', 'system_states', 'account', 'accounts', 'contract', 'contracts', 'contract_version', 'contract_versions', 'gauge', 'gauges', 'gauge_weight', 'gauge_weights', 'gauge_weight_vote', 'gauge_weight_votes', 'gauge_type', 'gauge_types', 'gauge_type_weight', 'gauge_type_weights', 'gauge_total_weight', 'gauge_total_weights', 'gauge_liquidity', 'gauge_liquidities', 'gauge_deposit', 'gauge_deposits', 'gauge_withdraw', 'gauge_withdraws', 'lp_token', 'lp_tokens', 'pool', 'pools', 'coin', 'coins', 'underlying_coin', 'underlying_coins', 'token', 'tokens', 'daily_volume', 'daily_volumes', 'hourly_volume', 'hourly_volumes', 'weekly_volume', 'weekly_volumes', 'admin_fee_changelog', 'admin_fee_changelogs', 'amplification_coeff_changelog', 'amplification_coeff_changelogs', 'fee_changelog', 'fee_changelogs', 'transfer_ownership_event', 'transfer_ownership_events', 'add_liquidity_event', 'add_liquidity_events', 'remove_liquidity_event', 'remove_liquidity_events', 'remove_liquidity_one_event', 'remove_liquidity_one_events', 'exchange', 'exchanges', 'voting_app', 'voting_apps', 'proposal', 'proposals', 'proposal_vote', 'proposal_votes', 'trade_volume', 'trade_volumes', 'pool_event', 'pool_events', '_meta')
    system_state = sgqlc.types.Field('SystemState', graphql_name='systemState', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    system_states = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SystemState'))), graphql_name='systemStates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(SystemState_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(SystemState_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Account_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Account_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contract = sgqlc.types.Field(Contract, graphql_name='contract', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contracts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Contract))), graphql_name='contracts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Contract_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Contract_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contract_version = sgqlc.types.Field(ContractVersion, graphql_name='contractVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contract_versions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContractVersion))), graphql_name='contractVersions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ContractVersion_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ContractVersion_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge = sgqlc.types.Field(Gauge, graphql_name='gauge', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Gauge))), graphql_name='gauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Gauge_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Gauge_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weight = sgqlc.types.Field(GaugeWeight, graphql_name='gaugeWeight', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeWeight))), graphql_name='gaugeWeights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeight_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weight_vote = sgqlc.types.Field(GaugeWeightVote, graphql_name='gaugeWeightVote', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weight_votes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeWeightVote))), graphql_name='gaugeWeightVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeightVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeightVote_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_type = sgqlc.types.Field(GaugeType, graphql_name='gaugeType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeType))), graphql_name='gaugeTypes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeType_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeType_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_type_weight = sgqlc.types.Field(GaugeTypeWeight, graphql_name='gaugeTypeWeight', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_type_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeTypeWeight))), graphql_name='gaugeTypeWeights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeTypeWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeTypeWeight_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_total_weight = sgqlc.types.Field(GaugeTotalWeight, graphql_name='gaugeTotalWeight', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_total_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeTotalWeight))), graphql_name='gaugeTotalWeights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeTotalWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeTotalWeight_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_liquidity = sgqlc.types.Field(GaugeLiquidity, graphql_name='gaugeLiquidity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_liquidities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeLiquidity))), graphql_name='gaugeLiquidities', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeLiquidity_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_deposit = sgqlc.types.Field(GaugeDeposit, graphql_name='gaugeDeposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeDeposit))), graphql_name='gaugeDeposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeDeposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeDeposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_withdraw = sgqlc.types.Field(GaugeWithdraw, graphql_name='gaugeWithdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeWithdraw))), graphql_name='gaugeWithdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWithdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWithdraw_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_token = sgqlc.types.Field(LpToken, graphql_name='lpToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LpToken))), graphql_name='lpTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LpToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LpToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool = sgqlc.types.Field(Pool, graphql_name='pool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pool))), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    coin = sgqlc.types.Field(Coin, graphql_name='coin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    coins = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Coin))), graphql_name='coins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Coin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Coin_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    underlying_coin = sgqlc.types.Field('UnderlyingCoin', graphql_name='underlyingCoin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    underlying_coins = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UnderlyingCoin'))), graphql_name='underlyingCoins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UnderlyingCoin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UnderlyingCoin_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    daily_volume = sgqlc.types.Field('DailyVolume', graphql_name='dailyVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    daily_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DailyVolume'))), graphql_name='dailyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DailyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DailyVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    hourly_volume = sgqlc.types.Field('HourlyVolume', graphql_name='hourlyVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    hourly_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('HourlyVolume'))), graphql_name='hourlyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(HourlyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(HourlyVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    weekly_volume = sgqlc.types.Field('WeeklyVolume', graphql_name='weeklyVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    weekly_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WeeklyVolume'))), graphql_name='weeklyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WeeklyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WeeklyVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    admin_fee_changelog = sgqlc.types.Field('AdminFeeChangelog', graphql_name='adminFeeChangelog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    admin_fee_changelogs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AdminFeeChangelog'))), graphql_name='adminFeeChangelogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AdminFeeChangelog_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AdminFeeChangelog_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amplification_coeff_changelog = sgqlc.types.Field('AmplificationCoeffChangelog', graphql_name='amplificationCoeffChangelog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amplification_coeff_changelogs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AmplificationCoeffChangelog'))), graphql_name='amplificationCoeffChangelogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AmplificationCoeffChangelog_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AmplificationCoeffChangelog_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fee_changelog = sgqlc.types.Field('FeeChangelog', graphql_name='feeChangelog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fee_changelogs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FeeChangelog'))), graphql_name='feeChangelogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FeeChangelog_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FeeChangelog_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_ownership_event = sgqlc.types.Field('TransferOwnershipEvent', graphql_name='transferOwnershipEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_ownership_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TransferOwnershipEvent'))), graphql_name='transferOwnershipEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TransferOwnershipEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TransferOwnershipEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    add_liquidity_event = sgqlc.types.Field('AddLiquidityEvent', graphql_name='addLiquidityEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    add_liquidity_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AddLiquidityEvent'))), graphql_name='addLiquidityEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AddLiquidityEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AddLiquidityEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_event = sgqlc.types.Field('RemoveLiquidityEvent', graphql_name='removeLiquidityEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RemoveLiquidityEvent'))), graphql_name='removeLiquidityEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RemoveLiquidityEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RemoveLiquidityEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_one_event = sgqlc.types.Field('RemoveLiquidityOneEvent', graphql_name='removeLiquidityOneEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_one_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RemoveLiquidityOneEvent'))), graphql_name='removeLiquidityOneEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RemoveLiquidityOneEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RemoveLiquidityOneEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    exchange = sgqlc.types.Field('Exchange', graphql_name='exchange', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    exchanges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Exchange'))), graphql_name='exchanges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Exchange_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Exchange_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    voting_app = sgqlc.types.Field('VotingApp', graphql_name='votingApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    voting_apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VotingApp'))), graphql_name='votingApps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(VotingApp_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(VotingApp_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposal = sgqlc.types.Field(Proposal, graphql_name='proposal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposals = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Proposal))), graphql_name='proposals', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Proposal_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Proposal_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposal_vote = sgqlc.types.Field(ProposalVote, graphql_name='proposalVote', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposal_votes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProposalVote))), graphql_name='proposalVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ProposalVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ProposalVote_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_volume = sgqlc.types.Field('TradeVolume', graphql_name='tradeVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TradeVolume'))), graphql_name='tradeVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TradeVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TradeVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_event = sgqlc.types.Field(PoolEvent, graphql_name='poolEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolEvent))), graphql_name='poolEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Subscription(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('system_state', 'system_states', 'account', 'accounts', 'contract', 'contracts', 'contract_version', 'contract_versions', 'gauge', 'gauges', 'gauge_weight', 'gauge_weights', 'gauge_weight_vote', 'gauge_weight_votes', 'gauge_type', 'gauge_types', 'gauge_type_weight', 'gauge_type_weights', 'gauge_total_weight', 'gauge_total_weights', 'gauge_liquidity', 'gauge_liquidities', 'gauge_deposit', 'gauge_deposits', 'gauge_withdraw', 'gauge_withdraws', 'lp_token', 'lp_tokens', 'pool', 'pools', 'coin', 'coins', 'underlying_coin', 'underlying_coins', 'token', 'tokens', 'daily_volume', 'daily_volumes', 'hourly_volume', 'hourly_volumes', 'weekly_volume', 'weekly_volumes', 'admin_fee_changelog', 'admin_fee_changelogs', 'amplification_coeff_changelog', 'amplification_coeff_changelogs', 'fee_changelog', 'fee_changelogs', 'transfer_ownership_event', 'transfer_ownership_events', 'add_liquidity_event', 'add_liquidity_events', 'remove_liquidity_event', 'remove_liquidity_events', 'remove_liquidity_one_event', 'remove_liquidity_one_events', 'exchange', 'exchanges', 'voting_app', 'voting_apps', 'proposal', 'proposals', 'proposal_vote', 'proposal_votes', 'trade_volume', 'trade_volumes', 'pool_event', 'pool_events', '_meta')
    system_state = sgqlc.types.Field('SystemState', graphql_name='systemState', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    system_states = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SystemState'))), graphql_name='systemStates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(SystemState_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(SystemState_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Account_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Account_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contract = sgqlc.types.Field(Contract, graphql_name='contract', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contracts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Contract))), graphql_name='contracts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Contract_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Contract_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contract_version = sgqlc.types.Field(ContractVersion, graphql_name='contractVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    contract_versions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContractVersion))), graphql_name='contractVersions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ContractVersion_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ContractVersion_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge = sgqlc.types.Field(Gauge, graphql_name='gauge', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Gauge))), graphql_name='gauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Gauge_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Gauge_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weight = sgqlc.types.Field(GaugeWeight, graphql_name='gaugeWeight', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeWeight))), graphql_name='gaugeWeights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeight_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weight_vote = sgqlc.types.Field(GaugeWeightVote, graphql_name='gaugeWeightVote', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_weight_votes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeWeightVote))), graphql_name='gaugeWeightVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWeightVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWeightVote_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_type = sgqlc.types.Field(GaugeType, graphql_name='gaugeType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeType))), graphql_name='gaugeTypes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeType_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeType_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_type_weight = sgqlc.types.Field(GaugeTypeWeight, graphql_name='gaugeTypeWeight', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_type_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeTypeWeight))), graphql_name='gaugeTypeWeights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeTypeWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeTypeWeight_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_total_weight = sgqlc.types.Field(GaugeTotalWeight, graphql_name='gaugeTotalWeight', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_total_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeTotalWeight))), graphql_name='gaugeTotalWeights', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeTotalWeight_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeTotalWeight_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_liquidity = sgqlc.types.Field(GaugeLiquidity, graphql_name='gaugeLiquidity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_liquidities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeLiquidity))), graphql_name='gaugeLiquidities', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeLiquidity_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_deposit = sgqlc.types.Field(GaugeDeposit, graphql_name='gaugeDeposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeDeposit))), graphql_name='gaugeDeposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeDeposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeDeposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_withdraw = sgqlc.types.Field(GaugeWithdraw, graphql_name='gaugeWithdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gauge_withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GaugeWithdraw))), graphql_name='gaugeWithdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GaugeWithdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GaugeWithdraw_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_token = sgqlc.types.Field(LpToken, graphql_name='lpToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LpToken))), graphql_name='lpTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LpToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LpToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool = sgqlc.types.Field(Pool, graphql_name='pool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pool))), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    coin = sgqlc.types.Field(Coin, graphql_name='coin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    coins = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Coin))), graphql_name='coins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Coin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Coin_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    underlying_coin = sgqlc.types.Field('UnderlyingCoin', graphql_name='underlyingCoin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    underlying_coins = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UnderlyingCoin'))), graphql_name='underlyingCoins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UnderlyingCoin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UnderlyingCoin_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    daily_volume = sgqlc.types.Field('DailyVolume', graphql_name='dailyVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    daily_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DailyVolume'))), graphql_name='dailyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DailyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DailyVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    hourly_volume = sgqlc.types.Field('HourlyVolume', graphql_name='hourlyVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    hourly_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('HourlyVolume'))), graphql_name='hourlyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(HourlyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(HourlyVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    weekly_volume = sgqlc.types.Field('WeeklyVolume', graphql_name='weeklyVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    weekly_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WeeklyVolume'))), graphql_name='weeklyVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WeeklyVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WeeklyVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    admin_fee_changelog = sgqlc.types.Field('AdminFeeChangelog', graphql_name='adminFeeChangelog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    admin_fee_changelogs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AdminFeeChangelog'))), graphql_name='adminFeeChangelogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AdminFeeChangelog_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AdminFeeChangelog_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amplification_coeff_changelog = sgqlc.types.Field('AmplificationCoeffChangelog', graphql_name='amplificationCoeffChangelog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amplification_coeff_changelogs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AmplificationCoeffChangelog'))), graphql_name='amplificationCoeffChangelogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AmplificationCoeffChangelog_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AmplificationCoeffChangelog_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fee_changelog = sgqlc.types.Field('FeeChangelog', graphql_name='feeChangelog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fee_changelogs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FeeChangelog'))), graphql_name='feeChangelogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FeeChangelog_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FeeChangelog_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_ownership_event = sgqlc.types.Field('TransferOwnershipEvent', graphql_name='transferOwnershipEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_ownership_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TransferOwnershipEvent'))), graphql_name='transferOwnershipEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TransferOwnershipEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TransferOwnershipEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    add_liquidity_event = sgqlc.types.Field('AddLiquidityEvent', graphql_name='addLiquidityEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    add_liquidity_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AddLiquidityEvent'))), graphql_name='addLiquidityEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AddLiquidityEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AddLiquidityEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_event = sgqlc.types.Field('RemoveLiquidityEvent', graphql_name='removeLiquidityEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RemoveLiquidityEvent'))), graphql_name='removeLiquidityEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RemoveLiquidityEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RemoveLiquidityEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_one_event = sgqlc.types.Field('RemoveLiquidityOneEvent', graphql_name='removeLiquidityOneEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    remove_liquidity_one_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RemoveLiquidityOneEvent'))), graphql_name='removeLiquidityOneEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RemoveLiquidityOneEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RemoveLiquidityOneEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    exchange = sgqlc.types.Field('Exchange', graphql_name='exchange', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    exchanges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Exchange'))), graphql_name='exchanges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Exchange_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Exchange_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    voting_app = sgqlc.types.Field('VotingApp', graphql_name='votingApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    voting_apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VotingApp'))), graphql_name='votingApps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(VotingApp_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(VotingApp_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposal = sgqlc.types.Field(Proposal, graphql_name='proposal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposals = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Proposal))), graphql_name='proposals', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Proposal_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Proposal_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposal_vote = sgqlc.types.Field(ProposalVote, graphql_name='proposalVote', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    proposal_votes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProposalVote))), graphql_name='proposalVotes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ProposalVote_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ProposalVote_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_volume = sgqlc.types.Field('TradeVolume', graphql_name='tradeVolume', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_volumes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TradeVolume'))), graphql_name='tradeVolumes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TradeVolume_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TradeVolume_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_event = sgqlc.types.Field(PoolEvent, graphql_name='poolEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolEvent))), graphql_name='poolEvents', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolEvent_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolEvent_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class SystemState(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'registry_contract', 'contract_count', 'gauge_count', 'gauge_type_count', 'pool_count', 'token_count', 'total_pool_count', 'updated', 'updated_at_block', 'updated_at_transaction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    registry_contract = sgqlc.types.Field(Bytes, graphql_name='registryContract')
    contract_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='contractCount')
    gauge_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='gaugeCount')
    gauge_type_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='gaugeTypeCount')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='poolCount')
    token_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenCount')
    total_pool_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='totalPoolCount')
    updated = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='updated')
    updated_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='updatedAtBlock')
    updated_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='updatedAtTransaction')


class Token(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'decimals', 'name', 'symbol', 'pools', 'coins', 'underlying_coins')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='decimals')
    name = sgqlc.types.Field(String, graphql_name='name')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    pools = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Pool)), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
))
    )
    coins = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Coin)), graphql_name='coins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Coin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Coin_filter, graphql_name='where', default=None)),
))
    )
    underlying_coins = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UnderlyingCoin')), graphql_name='underlyingCoins', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UnderlyingCoin_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UnderlyingCoin_filter, graphql_name='where', default=None)),
))
    )


class TradeVolume(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('pool', 'timestamp', 'volume')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume')


class UnderlyingCoin(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'index', 'pool', 'token', 'coin', 'balance', 'updated', 'updated_at_block', 'updated_at_transaction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='token')
    coin = sgqlc.types.Field(sgqlc.types.non_null(Coin), graphql_name='coin')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')
    updated = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='updated')
    updated_at_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='updatedAtBlock')
    updated_at_transaction = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='updatedAtTransaction')


class VotingApp(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'codename', 'minimum_balance', 'minimum_quorum', 'minimum_time', 'required_support', 'vote_time', 'proposal_count', 'vote_count', 'token', 'proposals')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    codename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='codename')
    minimum_balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='minimumBalance')
    minimum_quorum = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='minimumQuorum')
    minimum_time = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='minimumTime')
    required_support = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='requiredSupport')
    vote_time = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='voteTime')
    proposal_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='proposalCount')
    vote_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='voteCount')
    token = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='token')
    proposals = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Proposal)), graphql_name='proposals', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Proposal_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Proposal_filter, graphql_name='where', default=None)),
))
    )


class _Block_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class _Meta_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('block', 'deployment', 'has_indexing_errors')
    block = sgqlc.types.Field(sgqlc.types.non_null(_Block_), graphql_name='block')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deployment')
    has_indexing_errors = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIndexingErrors')


class AddLiquidityEvent(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'provider', 'token_amounts', 'fees', 'invariant', 'token_supply')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='provider')
    token_amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='tokenAmounts')
    fees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='fees')
    invariant = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='invariant')
    token_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenSupply')


class AdminFeeChangelog(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='value')


class AmplificationCoeffChangelog(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='value')


class DailyVolume(sgqlc.types.Type, TradeVolume):
    __schema__ = graphql_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Exchange(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'buyer', 'receiver', 'token_sold', 'token_bought', 'amount_sold', 'amount_bought')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    buyer = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='buyer')
    receiver = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='receiver')
    token_sold = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='tokenSold')
    token_bought = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='tokenBought')
    amount_sold = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountSold')
    amount_bought = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountBought')


class FeeChangelog(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='value')


class HourlyVolume(sgqlc.types.Type, TradeVolume):
    __schema__ = graphql_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RemoveLiquidityEvent(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'provider', 'token_amounts', 'fees', 'token_supply', 'invariant')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='provider')
    token_amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='tokenAmounts')
    fees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fees')
    token_supply = sgqlc.types.Field(BigInt, graphql_name='tokenSupply')
    invariant = sgqlc.types.Field(BigInt, graphql_name='invariant')


class RemoveLiquidityOneEvent(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'provider', 'token_amount', 'coin_amount')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='provider')
    token_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenAmount')
    coin_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='coinAmount')


class TransferOwnershipEvent(sgqlc.types.Type, PoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'new_admin')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    new_admin = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='newAdmin')


class WeeklyVolume(sgqlc.types.Type, TradeVolume):
    __schema__ = graphql_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = None
graphql_schema.subscription_type = Subscription


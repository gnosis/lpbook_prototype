all: update-uniswap-v3-graphql-schema update-curve-graphql-schema fetch-curve-contract_abis update-uniswap-v2-graphql-schema

update-uniswap-v3-graphql-schema:
	python -m sgqlc.introspection --exclude-deprecated --exclude-description https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3 uniswap_v3_graphql_schema.json
	sgqlc-codegen schema uniswap_v3_graphql_schema.json lpbook/lps/uniswap_v3/artifacts/graphql_schema.py
	rm uniswap_v3_graphql_schema.json

update-curve-graphql-schema:
	python -m sgqlc.introspection --exclude-deprecated --exclude-description https://api.thegraph.com/subgraphs/name/curvefi/curve curve_graphql_schema.json
	sgqlc-codegen schema curve_graphql_schema.json lpbook/lps/curve/artifacts/graphql_schema.py
	rm curve_graphql_schema.json

fetch-curve-contract_abis:
	# fetches all "non meta" pools
	python -m lpbook.web3.fetch_abi lpbook/lps/curve/artifacts \
		0x06364f10b501e868329afbc005b3492902d6c763 `# pax` 			\
		0x0ce6a5ff5217e38315f87032cf90686c96627caa `# eurs` 		\
		0x2dded6da1bf5dbdf597c45fcfaa3194e53ecfeaf `# ib` 			\
		0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51 `# y` 			\
		0x4ca9b3063ec5866a4b82e437059d2c43d1be596f `# hbtc` 		\
		0x52ea46506b9cc5ef470c5bf89f17dc28bb35d85c `# usdt` 		\
		0x79a8c46dea5ada233abaffd40f3a0a2b1e5a4f27 `# busd` 		\
		0x7fc77b5c7614e1533320ea6ddc2eb61fa00a9714 `# sbtc` 		\
		0x80466c64868e1ab14a1ddf27a676c3fcbe638fe5 `# tricrypto`	\
		0x93054188d876f558f4a66b2ef1d97d16edf0895b `# ren` 			\
		0x98a7f18d4e56cfe84e3d081b40001b3d5bd3eb8b `# eurs` 		\
		0xa2b47e3d5c44877cca798226b7b8118f9bfb7a56 `# compound` 	\
		0xa5407eae9ba41422680e2e00537571bcc53efbfd `# susd` 		\
		0xa96a65c051bf88b4095ee1f2451c2a9d43f53ae2 `# aeth` 		\
		0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7 `# 3pool` 		\
		0xc5424b857f758e906013f3555dad202e4bdb4567 `# seth` 		\
		0xd51a44d3fae010294c616388b506acda1bfaae46 `# tricrypto2` 	\
		0xdc24316b9ae028f1497c275eb9192a3ea0f67022 `# steth` 		\
		0xdebf20617708857ebe4f679508e7b7863a8a8eee `# aave` 		\
		0xeb16ae0052ed37f479f7fe63849198df1765a733 `# saave` 		\
		0xf178c0b5bb7e7abf4e12a4838c7b7c5ba2c623c0 `# link` 		\
		0xf9440930043eb3997fc70e1339dbb11f341de7a8 `# reth` 		\
		0xfd5db7463a3ab53fd211b4af195c5bccc1a03890 `# eurt`

update-uniswap-v2-graphql-schema:
	python -m sgqlc.introspection --exclude-deprecated --exclude-description https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2 uniswap_v2_graphql_schema.json
	sgqlc-codegen schema uniswap_v2_graphql_schema.json lpbook/lps/uniswap_v2/artifacts/graphql_schema.py
	rm uniswap_v2_graphql_schema.json

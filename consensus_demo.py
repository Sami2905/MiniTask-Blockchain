"""
Consensus Demo
Simulates PoW, PoS, and DPoS consensus selection.
"""

import random

# Mock validators
pow_validators = [{'id': 'Miner1', 'power': random.randint(1, 100)} for _ in range(3)]
pos_validators = [{'id': 'Staker1', 'stake': random.randint(1, 100)} for _ in range(3)]
dpos_votes = ['Delegate1', 'Delegate2', 'Delegate1']

# PoW
pow_winner = max(pow_validators, key=lambda x: x['power'])
print(f"PoW Winner: {pow_winner['id']} (Power: {pow_winner['power']})")

# PoS
pos_winner = max(pos_validators, key=lambda x: x['stake'])
print(f"PoS Winner: {pos_winner['id']} (Stake: {pos_winner['stake']})")

# DPoS
from collections import Counter
vote_result = Counter(dpos_votes).most_common(1)[0][0]
print(f"DPoS Winner: {vote_result}")

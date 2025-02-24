use near_sdk::{near_bindgen, AccountId, collections::LookupMap};
use borsh::{BorshDeserialize, BorshSerialize}; // 

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct TrustScoreContract {
    contract_scores: LookupMap<AccountId, u8>,
    user_scores: LookupMap<AccountId, u8>,
}


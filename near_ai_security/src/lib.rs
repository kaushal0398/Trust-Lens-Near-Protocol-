use near_sdk::{near_bindgen, AccountId, BorshStorageKey, collections::LookupMap};
use borsh::{BorshDeserialize, BorshSerialize};

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct TrustScoreContract {
    contract_scores: LookupMap<AccountId, u8>,
    user_scores: LookupMap<AccountId, u8>,
}

#[near_bindgen]
impl TrustScoreContract {
    pub fn submit_audit(&mut self, contract_id: AccountId, risk_score: u8) {
        self.contract_scores.insert(&contract_id, &risk_score);
    }

    pub fn get_trust_score(&self, entity_id: AccountId) -> Option<u8> {
        self.contract_scores.get(&entity_id).or(self.user_scores.get(&entity_id))
    }
}


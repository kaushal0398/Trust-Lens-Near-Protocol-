use near_sdk::{near_bindgen, AccountId, collections::LookupMap};
use borsh::{BorshDeserialize, BorshSerialize}; // 

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct TrustScoreContract {
    contract_scores: LookupMap<AccountId, u8>,
    user_scores: LookupMap<AccountId, u8>,
}

impl Default for TrustScoreContract {
    fn default() -> Self {
        Self {
            contract_scores: LookupMap::new(b"c".to_vec()),  // ✅ Fixed Storage Key
            user_scores: LookupMap::new(b"u".to_vec()),      // ✅ Fixed Storage Key
        }
    }
}

#[near_bindgen]
impl TrustScoreContract {
    pub fn submit_audit(&mut self, contract_id: AccountId, risk_score: u8) {
        self.contract_scores.insert(&contract_id, &risk_score);
    }

    pub fn update_reputation(&mut self, user_id: AccountId, new_score: u8) {
        self.user_scores.insert(&user_id, &new_score);
    }


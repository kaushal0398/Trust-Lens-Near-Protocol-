use near_sdk::{near_bindgen, AccountId, collections::LookupMap, BorshDeserialize, BorshSerialize};

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct TrustScoreContract {
    contract_scores: LookupMap<AccountId, u8>,
}

impl Default for TrustScoreContract {
    fn default() -> Self {
        panic!("Contract must be initialized with new()");
    }
}

#[near_bindgen]
impl TrustScoreContract {
    #[init]
    pub fn new() -> Self {
        Self {
            contract_scores: LookupMap::new(b"c"),
        }
    }

    pub fn submit_audit(&mut self, contract_id: AccountId, risk_score: u8) {
        self.contract_scores.insert(&contract_id, &risk_score);
    }

    pub fn get_trust_score(&self, entity_id: AccountId) -> Option<u8> {
        self.contract_scores.get(&entity_id)
    }
}


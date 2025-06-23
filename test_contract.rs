#[near_bindgen]
impl Contract {
    pub fn vulnerable_function(&mut self) {
        self.balance += 100; // potential overflow
    }
}

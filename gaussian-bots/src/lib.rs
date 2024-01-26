pub mod wrappers;

use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn refill_resources() {
    wrappers::use_skill_targetless(wrappers::Skill::UseHp);
}

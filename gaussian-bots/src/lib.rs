pub mod wrappers;

use wasm_bindgen::prelude::*;
use web_sys;

#[wasm_bindgen]
pub fn run() -> Result<(), JsValue> {
    // todo: set up setInterval call
    let window = web_sys::window().expect("Error: window not found");
    let tick_fn = Closure::<dyn Fn()>::new(move || tick());
    window.set_interval_with_callback_and_timeout_and_arguments_0(
        tick_fn.as_ref().unchecked_ref(),
        5000,
    )?;

    tick_fn.forget(); // memory leak, but we can't drop the reference and still call periodically.
    Ok(())
}

pub fn tick() {
    wrappers::al_log("Hi");
}

#[wasm_bindgen]
pub fn refill_resources() {
    wrappers::use_skill_targetless(wrappers::Skill::UseHp);
}

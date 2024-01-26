use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_name=use_skill)]
    fn juse_skill(name: &str, target: JsValue, extra_arg: JsValue) -> JsValue;

    #[wasm_bindgen(js_name=log)]
    fn jlog(to_log: &str);
}

pub enum Skill {
    UseMp,
    UseHp,
}

fn skill_to_str(skill: Skill) -> &'static str {
    match skill {
        Skill::UseMp => "use_mp",
        Skill::UseHp => "use_hp",
    }
}

pub fn use_skill_targetless(skill: Skill) {
    juse_skill(skill_to_str(skill), JsValue::NULL, JsValue::NULL);
    jlog("Used an hp or mp pot... FROM RUST! 🦀");
}

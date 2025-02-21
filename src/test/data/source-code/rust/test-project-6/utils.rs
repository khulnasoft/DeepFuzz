// Copyright 2025 Fuzz Introspector Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

pub fn call_with<F>(input: &str, f: F) -> usize
where
    F: Fn(&str) -> usize,
{
    f(input)
}

pub fn process_str(input: &str) -> String {
    if input.is_empty() {
        "Input is empty".to_string()
    } else {
        format!("Processed: {}", input)
    }
}

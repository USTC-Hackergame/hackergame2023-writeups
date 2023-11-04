## 为什么要打开 /flag 😡
### Stage 1: LD_PRELOAD, love! 非预期解

不使用C库函数，直接用Rust写

``` rs
use std::io::prelude::*;

fn main() {
    let mut file = std::fs::File::open("/flag").unwrap();
    let mut buf = String::new();
    file.read_to_string(&mut buf).unwrap();
    println!("{}", buf);
}
```

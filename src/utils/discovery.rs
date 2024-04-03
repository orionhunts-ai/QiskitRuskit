// 

use etcd_rs::{Client, ClientConfig, PutRequest};
use tokio::runtime::Runtime;

pub fn register_service(service_name: &str, addr: &str) {
    let client = Runtime::new().unwrap().block_on(async {
        Client::connect(ClientConfig {
            endpoints: vec!["http://etcd:2379".into()],
            auth: None,
            tls: None,
        })
        .await.unwrap()
    });

    let req = PutRequest::new(service_name, addr);
    Runtime::new().unwrap().block_on(async {
        client.kv().put(req).await.unwrap();
    });

    println!("Service {} registered with address {}", service_name, addr);
}

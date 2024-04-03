// Networking for the Rust environment and within Docker containers

use tokio::net::{TcpListener, TcpStream};
use tokio::io::{self, AsyncReadExt, AsyncWriteExt};
use serde::{Serialize, Deserialize};
use serde_json;

#[derive(Serialize, Deserialize)]
struct Message {
    content: String,
}

pub async fn send_message(addr: &str, message: &Message) -> io::Result<()> {
    let mut stream = TcpStream::connect(addr).await?;
    let msg = serde_json::to_string(message)?;
    stream.write_all(msg.as_bytes()).await?;
    Ok(())
}

pub async fn listen_for_messages(addr: &str) -> io::Result<()> {
    let listener = TcpListener::bind(addr).await?;
    loop {
        let (mut socket, _) = listener.accept().await?;
        tokio::spawn(async move {
            let mut buf = vec![0; 1024];
            match socket.read(&mut buf).await {
                Ok(_) => {
                    let msg: Message = serde_json::from_slice(&buf).unwrap();
                    println!("Received: {}", msg.content);
                }
                Err(e) => println!("Failed to receive message: {:?}", e),
            }
        });
    }
}

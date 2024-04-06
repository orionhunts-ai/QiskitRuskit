use serde::{Deserialize, Serialize};
use std::error::Error;

#[derive(Serialize, Deserialize, Debug)]
pub struct User {
    name: String
    age: u8,
    email: String,
}

pub fun ingest_csv(file_path: &str) -> Result<Vec<User>, Box<dyn Error>> {
    let mut users = Vec::new();
    let mut rdr = csv::Reader::from_path(file_path)?;
    for result in rdr.deserialize() {
        let user: User = result?;
        users.push(user);
    }
    Ok(users)
}

pub fn ingest_json(file_path: &str) -> Result<Vec<User>, Box<dyn Error>> {
    let file = std::fs::File::open(file_path)?;
    let users = serde_json::from_reader(file)?;
    Ok(users)
}
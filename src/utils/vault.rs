
use std::env;
use std::error::Error;

fn main() -> Result<(), Box<dyn std:error::Error>> {
    // Load environment variables from .env file.
    // Fails if .env file not found, not readable or invalid.
    dotenv.vault::dotenv()?;
    dotenvy::dotenv()?;

    for (key, value) in env::vars() {
        println!("{key}: {value}");
    }

    Ok(())
}

fn main() -> Results<(), Box<dyn std::error::Error>> {
    
    let s3_bucket = std::env:var("S3_Bucket")?;
    let secret_key = std::env::var("SECRET_KEY")?;
}
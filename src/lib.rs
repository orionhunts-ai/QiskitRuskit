mod utils;

use warp::Filter;
use std::sync::Arc;
use tokio::sync::Mutex;
use data_ingestion_service::ingest::{ingest_csv, ingest_json};

#[tokio::main]
async fn main() {
    // Path for uploaded files (adjust as needed)
    let upload_dir = Arc::new(Mutex::new("uploads/".to_string()));

    // POST /upload
    let upload_route = warp::post()
        .and(warp::path("upload"))
        .and(warp::body::bytes())
        .and(warp::header::<String>("content-type"))
        .and(with_upload_dir(upload_dir.clone()))
        .and_then(handle_upload);

    warp::serve(upload_route).run(([127, 0, 0, 1], 3030)).await;
}

fn with_upload_dir(
    upload_dir: Arc<Mutex<String>>,
) -> impl Filter<Extract = (Arc<Mutex<String>>,), Error = std::convert::Infallible> + Clone {
    warp::any().map(move || upload_dir.clone())
}

async fn handle_upload(
    body: bytes::Bytes,
    content_type: String,
    upload_dir: Arc<Mutex<String>>,
) -> Result<impl warp::Reply, warp::Rejection> {
    // Simplified handling logic
    // Here, you'd save the file to `upload_dir` and call `ingest_csv` or `ingest_json` based on `content_type`
    Ok(warp::reply::with_status("File uploaded successfully.", warp::http::StatusCode::OK))
}
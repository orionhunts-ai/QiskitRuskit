use pyo3::prelude::*;
use pyo3::types::IntoPyDict;

fn call_python_model(data: &serde_json::Value) -> PyResult<()> {
    Python::with_gil(|py| {
        let model_module = PyModule::import(py, "model")?;
        let result = model_module.call1("predict", (data,))?;
        println!("Prediction result: {:?}", result);
        Ok(())
    })
}
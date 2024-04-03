use pyo3::prelude::*;
use pyo3::types::IntoPyDict;

#[pyfunction]
fn create_quantum_circuit(qubits: usize, operation: String) -> PyResult<()> {
    Python::with_gil(|py| {
        let qiskit = PyModule::import(py, "qiskit")?;
        let circuit = qiskit.call_method1("QuantumCircuit", (qubits, qubits))?;

        println!("Quantum Circuit Created with {} qubits.", qubits);

        // Flexible operation application based on input
        for qubit in 0..qubits {
            circuit.call_method1(&operation, (qubit,))?;
        }

        Ok(())
    })
}

#[pymodule]
fn qiskit_bridge(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(create_quantum_circuit, m)?)?;

    // Enhanced user-friendly functionality within Python
    let locals = [("qiskit_bridge", m)].into_py_dict(py);
    py.run(
        "def execute_quantum_circuit(qubits, operation): return qiskit_bridge.create_quantum_circuit(qubits, operation)", 
        None, Some(locals)
    )?;

    Ok(())
}

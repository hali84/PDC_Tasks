# 🧠 Python Multiprocessing – Chapter 3  
Efficient Matrix Computation using Multiple Processes

This chapter demonstrates different **multiprocessing techniques** in Python using a common heavy-load task:

👉 Matrix Multiplication (imported from `matrix_mul.py`)

Each program showcases a unique method to communicate, synchronize, or manage processes.  
Real-world applications: Data processing, scientific computing, automation, parallel workloads ✅

---

## 📌 Base Module: `matrix_mul.py`

All scripts import a single function:

- Generates 20×20 matrices
- Performs matrix multiplication repeatedly based on `count`
- Returns a small computed result

Purpose: Simulate a **CPU-intensive** workload 🔥

---

## ✅ Implemented Multiprocessing Scripts

### 1️⃣ communicating_with_pipe.py  
📡 **Point-to-point communication** (one sender → one receiver)

✔️ Good for structured data transfer between two processes.  

---

### 2️⃣ communicating_with_queue.py  
📬 **Safe multi-producer / multi-consumer** message passing

✔️ Thread- and process-safe  
✔️ Best for multiple tasks and workers  

---

### 3️⃣ killing_processes.py  
⛔ **Force-terminate long running processes**  
Useful for:

✔️ Timeouts  
✔️ Cancel buttons in apps  

---

### 4️⃣ naming_processes.py  
🏷️ **Tracking workers using custom names**

✔️ Helpful in debugging worker identities  

---

### 5️⃣ process_in_subclass.py  
🧩 **Object-Oriented multiprocessing**

✔️ Custom behavior in a subclass of `Process`  

---

### 6️⃣ process_pool.py  
🔥 **Best method to parallelize multiple independent tasks**

✔️ Efficient worker pool  
✔️ Auto task distribution  

---

### 7️⃣ run_background_processes.py  
👻 **Daemon background tasks**

✔️ Stop automatically when main exits  
❌ Not guaranteed full completion  

---

### 8️⃣ run_background_processes_no_daemons.py  
✅ **Background process must finish before exit**

✔️ Safe + controlled shutdown using `.join()`  

---

### 9️⃣ spawning_processes.py  
🍼 **Safe Windows-compatible process creation**

✔️ Uses `spawn()` method ✔️ Avoids deadlocks 


---

## 🎯 Summary Table

| File | Concept | Communication | Notes |
|------|---------|---------------|------|
| communicating_with_pipe.py | Pipe | 🔁 One-to-one | Simple directed messaging |
| communicating_with_queue.py | Queue | 📬 Multi-worker | Most scalable approach |
| killing_processes.py | Termination control | ⛔ Force stop | Timeout handling |
| naming_processes.py | Debugging support | 🏷️ Names | Track workers easily |
| process_in_subclass.py | OOP-based processing | 🎛️ Custom behavior | Reusable workers |
| process_pool.py | Parallel workload | 🚀 Efficient | Best for batch tasks |
| run_background_processes.py | Daemon mode | 👻 Auto-stop | May not finish |
| run_background_processes_no_daemons.py | Safe background | ✅ Full completion | Uses join() |
| spawning_processes.py | Safe initialization | 🔒 Windows-friendly | No shared state issues |

---

## 🏁 Conclusion  
This chapter demonstrates **complete multiprocessing control**:

✅ Data Sharing  
✅ Worker Management  
✅ Communication Strategies  
✅ Performance Improvement  
✅ Safe Process Shutdown

🔥 Perfect foundation for distributed computing & parallel AI workloads!

---




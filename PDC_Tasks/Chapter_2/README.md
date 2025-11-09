# 🧵 Chapter 2 — Python Thread Synchronization (PDC)

This folder demonstrates how different **thread synchronization primitives** work in Python using the **same workload**:  
✅ CPU-bound matrix multiplication implemented in `matrix_mul.py`.

Each `*_test.py` file runs multiple worker threads using a specific synchronization mechanism to manage shared execution.

---

## 📂 Folder Structure


---

## 🧠 Concepts Covered (Simple Summary)

| Sync Concept | File | Purpose |
|-------------|------|---------|
| 🔄 Barrier | `barrier_test.py` | Wait for all threads to reach a point before starting work |
| 🚦 Condition | `condition_test.py` | Coordinator notifies workers when they can proceed |
| ⛔ Semaphore | `semaphore_test.py` | Limits access to shared resources (max N workers at once) |
| 📣 Event | `event_test.py` | Broadcast signal that wakes all waiting threads |
| 🔐 Lock | `lock_test.py` | Prevents multiple threads from entering critical section |
| ♻️ RLock | `rlock_test.py` | Allows the **same thread** to re-enter a locked block |
| 📦 Queue | `queue_test.py` | Thread-safe producer–consumer messaging |

---






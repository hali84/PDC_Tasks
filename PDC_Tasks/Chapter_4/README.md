# 🧠 PDC Chapter-4 – MPI Communication in Python

This chapter demonstrates how Python’s **`mpi4py`** library enables inter-process communication using the **Message Passing Interface (MPI)** standard.  
Each example focuses on a specific MPI communication pattern or topology essential for distributed computing.

---

## ⚙️ alltoall.py  
### **Purpose**  
To demonstrate the **All-to-All communication pattern**, where every process sends data to all other processes.  

### **Observation**  
Each process generated simulated weather data and successfully exchanged values with all other processes.  
Results verified that every process received a complete dataset from all peers, proving effective full communication.

---

## ⚙️ broadcast.py  
### **Purpose**  
To demonstrate how one process can broadcast data to all other processes in the communicator.  

### **Observation**  
The root process successfully transmitted data to every process simultaneously.  
Broadcast operation ensured data consistency across all ranks.

---

## ⚙️ deadlockProblems.py  
### **Purpose**  
To highlight potential deadlocks in point-to-point communication and show how to avoid them using non-blocking or ordered operations.  

### **Observation**  
Deadlocks occurred when send and receive operations were mismatched.  
By introducing `Isend()`/`Irecv()` or changing communication order, all processes completed safely.

---

## ⚙️ gather.py  
### **Purpose**  
To demonstrate data collection from multiple processes into a single root process using `Gather()`.  

### **Observation**  
Each process sent computed data to the root process, which assembled all values correctly.  
The gathered array confirmed accurate and complete data aggregation.

---

## ⚙️ helloworld_MPI.py  
### **Purpose**  
To introduce basic MPI concepts — initialization, communicator usage, and process rank/size identification.  

### **Observation**  
Each process printed its rank and total process count, confirming successful MPI environment setup and parallel execution.

---

## ⚙️ pointToPointCommunication.py  
### **Purpose**  
To demonstrate basic **send** and **receive** operations between two MPI processes.  

### **Observation**  
Message passing worked correctly, with the sender transmitting data and the receiver displaying it.  
Execution order confirmed correct synchronization between processes.

---

## ⚙️ reduction.py  
### **Purpose**  
To perform parallel reduction operations (e.g., sum, max, min) across all processes using `Reduce()`.  

### **Observation**  
The reduction combined data from all ranks, producing an accurate global result on the root process.  
Confirmed the efficiency of distributed computation aggregation.

---

## ⚙️ scatter.py  
### **Purpose**  
To demonstrate how data from one process is distributed evenly among all other processes using `Scatter()`.  

### **Observation**  
The root process divided a dataset into chunks and distributed them correctly.  
Each process received its assigned portion, validating balanced data distribution.

---

## ⚙️ virtualTopology.py  
### **Purpose**  
To illustrate creation of a **virtual process topology** using Cartesian communicators.  

### **Observation**  
Processes were mapped to a logical grid structure.  
Communication within the topology followed structured neighbor patterns, reducing complexity in multidimensional problems.

---

## 🧩 Summary

| Script Name | Purpose Summary | Observation Summary |
| :------------------------------- | :--------------------------------------------- | :---------------------------------------------------------- |
| alltoall.py | Demonstrates all-to-all communication | Each process exchanged data with all others successfully |
| broadcast.py | One-to-all data broadcast | Root process distributed data uniformly |
| deadlockProblems.py | Avoiding MPI deadlocks | Safe communication achieved with non-blocking or ordered sends |
| gather.py | Collecting data on root process | Root assembled complete dataset |
| helloworld_MPI.py | Basic MPI setup and rank info | Parallel environment initialized correctly |
| pointToPointCommunication.py | Direct message exchange | Sender and receiver synchronized successfully |
| reduction.py | Parallel reduction operation | Aggregated result computed correctly |
| scatter.py | Data distribution from root | Data evenly scattered to all processes |
| virtualTopology.py | Logical grid topology mapping | Structured communication achieved via Cartesian layout |

---

## 🧠 Overall Learning

Through these examples, students learn how **MPI** enables efficient communication in distributed systems.  
Each script focuses on a different MPI concept — from basic message passing to complex topologies — forming the foundation for high-performance parallel applications.

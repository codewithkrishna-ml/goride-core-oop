# GoRide Core - Ride Sharing Simulator 🚗🏍️

GoRide Core is a comprehensive ride-sharing backend simulator built in Python using advanced **Object-Oriented Programming (OOP)** architectures. The system models the core dynamics of platforms like Uber or Ola, coordinating interactions between Riders, Drivers, Wallet system validation, and dynamic Fare Calculations based on vehicle archetypes.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dual User Personas:** Distinctly splits workflow behaviors for `Rider` profiles and `Driver` profiles originating from a shared system core.
*   **Secure In-App Wallet:** Implements booking restriction thresholds where riders cannot initiate ride requests if their active balance drops below standard base limits (e.g., ₹50).
*   **Real-time Driver Status Tracker:** State management handling dispatch requests seamlessly (`AVAILABLE` vs `BUSY`) to prevent double-bookings or concurrent passenger overrides.
*   **Dynamic Poly-Fare Engine:** Calculates explicit trip pricing variables on the fly based on specified route distances paired against select vehicle models (Bike, Sedan, SUV).

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This project serves as a showcase of scalable code infrastructure:
*   **Inheritance (Hierarchical):** Cleanly structures `Rider` and `Driver` classes as children inheriting base parameters from a central `User` super-class using `super().__init__()`. Similarly, `Bike`, `Sedan`, and `SUV` inherit from the parent `Vehicle` blueprint.
*   **Polymorphism (Method Overriding):** The `calculate_fare()` function is uniquely overridden across different vehicle subclasses to calculate precise pricing variations dynamically (e.g., Bike at ₹5/km vs SUV at ₹18/km).
*   **Composition:** Maps active references seamlessly by assigning a concrete `Vehicle` object directly as an inner attribute of a `Driver` profile configuration.

---

## 🚀 How to Run and Test

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd goride-core-oop
    ```
3.  **Run the application simulation script:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.

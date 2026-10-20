# Order and Inventory Accounting System

## 1. Overview
This repository contains a terminal-based **Order and Inventory Accounting System** implemented in Python. Designed around Object-Oriented Programming (OOP) principles, the application provides a modular and extensible architecture to manage corporate entities such as clients, products, and sales transactions. The system features an interactive Command-Line Interface (CLI) for real-time data processing and state management.

## 2. Key Features
* **Client Management**: Supports registration, tracking, and deletion of customer profiles using unique identifiers.
* **Inventory Control**: Enables management of product catalogs, including descriptions, real-time pricing, and stock quantities.
* **Order Processing**: Facilitates transaction creation by mapping specific clients to multiple chosen inventory items, with automated total price calculation.
* **Data Aggregation**: Provides a comprehensive overview of the entire system state, compiling lists of active clients, available products, and processed orders.

## 3. Technical Specifications & Architecture
* **Language**: Python 3.x
* **Paradigm**: Object-Oriented Programming (OOP)
* **Project Components**:
  * `Client`: Represents customer entities with contact details and individual IDs.
  * `Product`: Manages product attributes, including cost and warehouse quantity.
  * `Order`: Encapsulates transaction details and automatically computes aggregate purchase costs.
  * `AccountingSystem`: Functions as the centralized database coordinator and controller for system workflows.
  * `main_menu()`: Implements the application lifecycle loop and processes terminal user inputs.

## 4. System Requirements & Installation

### Prerequisites
To run this application, ensure that **Python 3.x** or higher is installed on your local environment.


Cafe Management App
====================

## Project Overview
The Cafe Management App is designed to help administrators and employees manage schedules, tasks, documents, and internal communication in a cafe setting. The app is built for simplicity and usability, without a POS system or order tracking. The backend is developed with Flask, and SQLite is used as the database.

## Features
1. **User Roles**: Admin and Worker roles with specific access permissions.
2. **Authentication**: Secure login system with role-based access control.
3. **Schedule Management**: 
   - Admins can create, update, and manage shift schedules.
   - Workers can view their schedules and request shift changes.
   - Shift marker for workers to log shift start and end times.
4. **Task Assignment and Tracking**:
   - Admins assign weekly or monthly tasks.
   - Workers can mark tasks as complete.
5. **Document Management**:
   - Workers submit and generate documents (e.g., vacation requests, payroll slips) in PDF format.
   - Admins review and approve documents.
6. **Recipe Display**:
   - Workers view kitchen and bar recipes.
   - Admins can add, edit, or remove recipes.
7. **Revenue Tracking**:
   - Track cash balances at shift start and end.
   - Calculate discrepancies between recorded and actual cash.
8. **Internal Chat System**:
   - In-app messaging for communication between Admins and Workers.
   - Notifications for new messages.
9. **Product Ordering (Optional)**:
   - Workers submit orders for stock.
   - Possible API integration for inventory management.
10. **Employee Onboarding**:
   - Document upload feature for new hires.
   - Admins verify and approve onboarding documents.
11. **Company Updates and Knowledge Base (Optional)**:
   - Admins post updates.
   - Centralized reference area for recipes, guides, and links.

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: SQLite

## Setup Instructions
1. Clone the repository to your local machine.
2. Set up a virtual environment and install dependencies with `pip install -r requirements.txt`.
3. Initialize the SQLite database by running the provided migration scripts or database setup file.
4. Run the Flask application using `flask run`.
5. Access the app at `http://localhost:5000`.

## Deliverables
1. Code repository with a clear commit history.
2. Documentation on each feature, both backend and frontend processes.
3. Basic test cases for core functionalities like login, schedule viewing, and document submissions.

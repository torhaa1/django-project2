# Product Context: Django Order Management System

## Why This Project Exists

The Order Management System is being developed to address several key business needs:

1. **Centralized Resource Management**: The company needs a unified system to catalog and manage orders of ROV (Remotely Operated Vehicle) and Survey equipment and personnel resources on projects.

2. **Financial Oversight**: Need to track planned versus actual costs for better budget management and financial reporting.

3. **Multi-tenant Access**: The system needs to serve both internal staff (Nexans) and external subcontractors (REACH and IKM) while maintaining proper data isolation.

## Problems It Solves

### Financial Management Challenges
- **Cost Tracking**: Without a dedicated system, tracking planned vs. actual costs is manual and error-prone
- **Pricing Complexity**: Managing different pricing models (unit, time-based, lump sum) requires a flexible system
- **Budget Oversight**: Lack of real-time financial data hampers decision-making

### Security Challenges
- **Data Isolation**: Need to prevent subcontractors from seeing each other's sensitive information
- **Access Control**: Different user types require different levels of system access

## How It Should Work

### Core Workflow
1. **Resource Management**:
   - Maintain a catalog of available resources (equipment/personnel), projects, etc
   - Categorize resources (ROV/Survey) and their ordering
   - Users will group resources into logical ResourcePackages

2. **Order Processing**:
   - Create orders for resources
   - Associate orders with specific projects/jobs
   - Track order status from creation to completion

3. **Financial Tracking**:
   - Record planned costs during order creation
   - Update with actual costs as resources are utilized (manually done by nexans user based on our invoices)
   - Generate reports for planned and actual order cost

4. **User Access**:
   - Different views and permissions based on user role (subcontractors don't have access to Django Admin)
   - Row-level filtering to ensure data isolation
   - Simple authentication with flexibility for future integration

## User Experience Goals

### For Nexans Staff
- **Comprehensive View**: Access to all system data and functionality
- **Administrative Control**: Ability to manage users, resources, and system settings (leverage Django Admin when possible)
- **Financial Oversight**: Tools for budget management and cost analysis

### For REACH Subcontractors
- **Focused Access**: View and manage only Survey resources and related orders
- **Limited Visibility**: Cannot see IKM's resources, orders, or pricing

### For IKM Subcontractors
- **Focused Access**: View and manage only ROV resources and related orders
- **Limited Visibility**: Cannot see REACH's resources, orders, or pricing

### For All Users
- **Intuitive Interface**: Easy to learn and use, even for occasional users
- **Design**: Simple design; minimal code lines for styling; targeted for pc devices, not tablet or mobiles.
- **Clear Information Architecture**: Logical organization of data and functionality
- **Efficient Workflows**: Minimize clicks and data entry for common tasks

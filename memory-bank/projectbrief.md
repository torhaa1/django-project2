# Project Brief: Django Order Management System

## Overview
A Django web application for order management of equipment and personnel on projects that will help with financial tracking. The system will manage resources (equipment/personnel), orders, projects and provide role-based access control for different user types.

## Core Requirements

### Business Requirements
- **Order Management**: Track and manage orders for equipment and personnel on projects
- **Financial Tracking**: Compare planned vs. actual costs
- **Multiple Pricing Models**: Support unit, time-based, and lump sum pricing
- **Resource Management**: Maintain catalog of equipment/personnel with ROV/Survey categorization
- **Resource Packages**: Group resources into logical packages

### Access Control Requirements
- **Role-Based Access**:
  - **Nexans staff**: Full access to all system functionality
  - **REACH subcontractors**: Limited to Survey resources and related orders
  - **IKM subcontractors**: Limited to ROV resources and related orders
- **Row-Level Security**: Subcontractors cannot see each other's items, orders, or prices

### Technical Requirements
- **Authentication**: Flexible system that can start with Django's built-in auth and potentially migrate to company Azure or SSO
- **Maintainability**: Simple, short DRY code that's easily maintainable by novice developers
- **Performance**: Support for at least 20 concurrent users
- **Security**: Proper implementation of row-level security and data isolation

## Project Phases
The project will be implemented in phases:
1. **Phase 1**: Foundation setup and MVP development
2. **Phase 2**: Completion of core functionality and production readiness
3. **Future phases**: Additional features and enhancements (to be determined)

## Project Goals
- Create a simple, lean, maintainable Django CRUD application
- Enhance financial oversight through cost tracking
- Improve operational efficiency through better resource management
- Ensure proper security and data isolation between different user types
- Provide a system that can be easily taken over by new novice developers

## Constraints
- Must be simple enough for a novice developer to maintain
- Keep codebase short/lean and friendly for LLM context windows
- Authentication system must be flexible for potential future integration

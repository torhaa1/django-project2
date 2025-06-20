# Project Brief: Django Order Management System

## Overview
Django web app for order management of equipment/personnel with financial tracking and role-based access.

## Core Requirements

### Business
- Order management for equipment/personnel
- Financial tracking (planned vs. actual costs)
- Multiple pricing models (unit, time-based, lump sum)
- Resource management with ROV/Survey categorization
- Resource packages

### Access Control
- Nexans staff: Full access
- REACH: Survey resources/orders only
- IKM: ROV resources/orders only
- Row-level security between subcontractors

### Technical
- Flexible authentication (Django auth → potential Azure/SSO)
- Lean, simple, maintainable code for new novice developers
- Support for 20+ concurrent users
- Proper data isolation

## Project Phases
1. **Phase 1**: Foundation setup and MVP
2. **Phase 2**: Core functionality and production readiness

## Constraints
- Simple for novice developers
- Lean/short codebase (LLM context-window friendly)
- Replaceable authentication system

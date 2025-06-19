# Wildfire AIM - Backend

## Overview
Wildfire AIM (AI Mitigation) is a wildfire mitigation and prevention system powered by Microsoft Azure AI Technologies, developed for the AI Innovation Challenge in June 2025.

## Backend Architecture

### Project Structure
```
backend/
├── wildfire_app.py          # Main Flask application
├── data/
│   └── data.json           # Q&A database containing wildfire management information
└── README.md               # This file
```

### Core Components

#### 1. Flask Application (`wildfire_app.py`)
- **Framework**: Flask 3.0.3
- **Purpose**: Web server that handles HTTP requests and serves the frontend
- **Key Features**:
  - Serves static files and templates from the frontend directory
  - Processes search queries for wildfire Q&A data
  - Renders the main application interface

#### 2. Data Layer (`data/data.json`)
- **Format**: JSON array containing Q&A pairs
- **Content**: Comprehensive wildfire management information including:
  - Prescribed burning techniques and benefits
  - Regulatory and permitting information
  - Cultural burning practices (e.g., Karuk Tribe)
  - Federal agency guidelines and procedures
- **Structure**: Each entry contains:
  ```json
  {
    "question": "Exact question text",
    "answer": "Detailed answer with HTML formatting"
  }
  ```

### Functionality

#### Search System
- **Exact Match**: Performs case-insensitive exact matching on question text
- **Query Processing**: Strips whitespace and converts to lowercase for consistent matching
- **Error Handling**: Gracefully handles file not found and JSON decode errors

#### API Endpoints
- **GET/POST `/`**: Main application route
  - GET: Displays the search interface
  - POST: Processes search queries and returns matching results

### Technical Implementation

#### Key Functions
1. **`load_wildfire_data(search_query)`**
   - Loads and searches the Q&A database
   - Returns matching results as a list
   - Handles file I/O and JSON parsing errors

2. **`index()`**
   - Main route handler for the application
   - Processes form submissions and renders results
   - Manages both GET and POST requests

#### Configuration
- **Template Folder**: `../frontend/templates`
- **Static Folder**: `../frontend/static`
- **Debug Mode**: Enabled for development
- **Port**: Default Flask port (5000)

### Dependencies
- **Flask 3.0.3**: Web framework for Python
- **JSON**: Built-in Python module for data handling
- **OS**: Built-in Python module for file operations

### Data Management

#### Adding New Q&A Entries
To add new wildfire management information:

1. Open `backend/data/data.json`
2. Add new entries in the following format:
   ```json
   {
     "question": "Your exact question here?",
     "answer": "Your detailed answer with <br> for line breaks and <strong> for bold text"
   }
   ```
3. Ensure questions are unique and specific for better search results

#### Data Validation
- Questions should be exact and specific
- Answers can include HTML formatting for better presentation
- Maintain consistent formatting across all entries

### Error Handling
- **File Not Found**: Returns empty list if data.json is missing
- **JSON Decode Error**: Returns empty list if data.json is corrupted
- **Search Errors**: Gracefully handles malformed search queries

### Performance Considerations
- **File Loading**: Data is loaded on each search request (suitable for small datasets)
- **Memory Usage**: Minimal memory footprint due to simple file-based storage
- **Response Time**: Fast response times for exact match searches

### Security Features
- **Input Sanitization**: Search queries are stripped and normalized
- **File Access**: Restricted to specific data directory
- **Error Information**: Limited error details exposed to prevent information leakage

### Development Notes
- **Debug Mode**: Enabled for development with detailed error messages
- **Hot Reload**: Flask development server supports automatic reloading
- **Cross-Origin**: Configured to serve frontend assets from different directory

### Future Enhancements
- Database integration for larger datasets
- Fuzzy search capabilities
- API endpoints for external integrations
- Caching mechanisms for improved performance
- User authentication and access control
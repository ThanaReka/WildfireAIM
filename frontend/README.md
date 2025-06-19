# Wildfire AIM - Frontend

## Overview
Wildfire AIM (AI Mitigation) is a wildfire mitigation and prevention system powered by Microsoft Azure AI Technologies, developed for the AI Innovation Challenge in June 2025.

## Frontend Architecture

### Project Structure
```
frontend/
├── templates/
│   └── index.html          # Main application template
├── static/
│   ├── css/
│   │   └── styles.css      # Custom styling
│   └── images/
│       ├── hero-image.png  # Hero section background
│       └── misty-forest-strip.png  # Page background
└── README.md               # This file
```

### Core Components

#### 1. HTML Template (`templates/index.html`)
- **Framework**: Bootstrap 5.3.0 (CDN)
- **Purpose**: Main user interface for the wildfire information portal
- **Key Features**:
  - Responsive design with Bootstrap components
  - Hero section with background image
  - Search form with exact query matching
  - Dynamic results display with card layout
  - Mobile-friendly interface

#### 2. Styling (`static/css/styles.css`)
- **Custom CSS**: Enhances Bootstrap with project-specific styling
- **Key Features**:
  - Hero image background with text overlay
  - Page background with misty forest theme
  - Semi-transparent content containers
  - Responsive design elements
  - Typography and spacing customization

#### 3. Assets (`static/images/`)
- **hero-image.png**: High-resolution background for the hero section
- **misty-forest-strip.png**: Background strip for the entire page
- **Purpose**: Creates immersive forest/wildfire theme

### User Interface Design

#### Hero Section
- **Background**: Full-width hero image with forest theme
- **Content**: Application title and description
- **Styling**: White text with shadow for readability
- **Responsive**: Adapts to different screen sizes

#### Search Interface
- **Form Design**: Bootstrap input group with search button
- **Placeholder Text**: Provides example search queries
- **Validation**: Requires exact question matching
- **User Feedback**: Clear instructions for search requirements

#### Results Display
- **Card Layout**: Bootstrap cards for clean presentation
- **Content Formatting**: Supports HTML formatting in answers
- **State Management**: Handles empty states and no results
- **Responsive**: Adapts to different screen sizes

### Functionality

#### Search System
- **Exact Matching**: Requires precise question text input
- **Case Insensitive**: Handles variations in capitalization
- **Real-time Display**: Shows results immediately after search
- **Error Handling**: Provides helpful feedback for no matches

#### Content Presentation
- **HTML Support**: Renders formatted answers with line breaks and bold text
- **Readable Layout**: Clean typography and spacing
- **Accessibility**: Semantic HTML structure
- **Cross-browser**: Compatible with modern browsers

### Technical Implementation

#### Template Engine
- **Jinja2**: Flask's default template engine
- **Variable Passing**: Receives search results and query from backend
- **Conditional Rendering**: Shows different content based on search state
- **Safe HTML**: Allows HTML content in answers

#### Responsive Design
- **Bootstrap Grid**: Mobile-first responsive layout
- **Flexible Images**: Background images scale appropriately
- **Touch-friendly**: Optimized for mobile devices
- **Cross-device**: Works on desktop, tablet, and mobile

#### Performance Optimization
- **CDN Resources**: Bootstrap loaded from CDN for faster loading
- **Optimized Images**: Compressed background images
- **Minimal CSS**: Lightweight custom styles
- **Fast Rendering**: Efficient template processing

### User Experience Features

#### Visual Design
- **Theme**: Forest/wildfire aesthetic with natural colors
- **Typography**: Clean, readable fonts with proper hierarchy
- **Spacing**: Consistent padding and margins throughout
- **Visual Hierarchy**: Clear distinction between sections

#### Interaction Design
- **Search Flow**: Intuitive search and results display
- **Feedback**: Clear messages for different states
- **Loading States**: Immediate response to user actions
- **Error Handling**: Helpful error messages and guidance

#### Accessibility
- **Semantic HTML**: Proper heading structure and landmarks
- **Alt Text**: Descriptive text for images
- **Keyboard Navigation**: Full keyboard accessibility
- **Screen Reader**: Compatible with assistive technologies

### Browser Compatibility
- **Modern Browsers**: Chrome, Firefox, Safari, Edge
- **Mobile Browsers**: iOS Safari, Chrome Mobile
- **Responsive**: Works on all screen sizes
- **Progressive Enhancement**: Graceful degradation for older browsers

### Customization Options

#### Styling Modifications
To customize the appearance:

1. **Colors**: Modify CSS variables in `styles.css`
2. **Typography**: Update font families and sizes
3. **Layout**: Adjust spacing and container widths
4. **Images**: Replace background images in `static/images/`

#### Content Updates
- **Hero Text**: Modify title and description in `index.html`
- **Search Placeholder**: Update example queries
- **Results Format**: Adjust card layout and styling

### Development Guidelines

#### Code Structure
- **Separation of Concerns**: HTML, CSS, and JavaScript are separated
- **Semantic HTML**: Use appropriate HTML elements
- **CSS Organization**: Logical grouping of styles
- **Comments**: Clear documentation of complex sections

#### Best Practices
- **Responsive Design**: Mobile-first approach
- **Performance**: Optimize images and minimize HTTP requests
- **Accessibility**: Follow WCAG guidelines
- **Maintainability**: Clean, well-documented code

### Future Enhancements
- **Advanced Search**: Fuzzy matching and autocomplete
- **Interactive Elements**: JavaScript-powered features
- **Dark Mode**: Alternative color scheme
- **Animations**: Smooth transitions and effects
- **Progressive Web App**: Offline functionality and app-like experience
- **Multi-language Support**: Internationalization features
- **Advanced Filtering**: Category-based search options
- **User Preferences**: Customizable interface settings


# Teaching Platform - Project Documentation

## Overview
This educational platform provides a secure environment for teachers to share video content with students using access codes. The platform includes comprehensive features for course management, video protection, and student tracking.

## Key Features

### Security Features
- **Access Code Protection**: Every video requires a unique access code
- **Time-Limited Access**: Access codes expire after 14 days
- **Video Protection**: Videos cannot be shared, downloaded, or accessed without proper authorization
- **YouTube Integration**: Secure embedding of YouTube videos with sharing prevention

### User Management
- **Student Profiles**: Students can view their accessible videos and track progress
- **Teacher Dashboard**: Teachers can manage courses, lessons, and videos
- **Admin Controls**: Comprehensive admin panel for platform management

### Content Management
- **Course Structure**: Organized by grades, courses, lessons, and videos
- **Bulk Code Generation**: Generate multiple access codes at once
- **Video Analytics**: Track student viewing time and completion

## Recent Improvements

### Video Player Enhancements
- Fixed video playback issues while maintaining security
- Improved fullscreen functionality
- Enhanced user interface for better usability
- Added proper YouTube API integration
- Implemented reliable play/pause controls

### Security Improvements
- Maintained strict access control while improving usability
- Added multiple layers of protection against unauthorized sharing
- Implemented proper event handling for secure video interaction

### User Experience Improvements
- Larger, more visible play buttons
- Better visual feedback for user interactions
- Improved overall look and feel of the video player

## Running the Platform
1. Use `start_server.bat` to start the Django server
2. Access the platform at http://127.0.0.1:8080/
3. Login with your credentials

## Technical Notes
- The platform is built with Django
- Frontend uses Bootstrap and custom JavaScript
- YouTube videos are embedded using the YouTube IFrame API
- Custom security layers prevent unauthorized access and sharing

## Maintenance
- Regular backups are recommended
- Monitor access code usage and student activity
- Update YouTube API integration as needed

## Contact
For support, contact Ammar Mahmoud via Telegram: @d_f_l

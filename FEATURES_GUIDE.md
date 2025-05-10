# Teaching Platform - New Features Guide

## Starting the Server

1. Double-click on `start_server.bat` to start the Django server
2. Access the platform at: http://127.0.0.1:8080/
3. Login with your credentials

## Teacher Dashboard

We've added a comprehensive teacher dashboard that allows teachers to manage their courses, lessons, and videos.

### Accessing the Teacher Dashboard

1. Login as a teacher
2. Click on the "لوحة تحكم المعلم" link in the navigation menu

### Features

- View all courses you teach
- See statistics about your videos and students
- Manage course content
- View recent student activity
- Edit your teacher profile

### Managing Courses

1. From the teacher dashboard, click on a course to view its details
2. Add new lessons or videos
3. View student statistics for the course

### Editing Your Profile

1. From the teacher dashboard, click on "تعديل الملف الشخصي"
2. Update your information and photo
3. Click "حفظ التغييرات" to save

## Time-Limited Video Access

Access codes now expire after 14 days from when they are first used.

### How It Works

1. When a student uses an access code, it starts a 14-day timer
2. After 14 days, the code expires and the student will need a new code to access the video
3. The student profile shows which videos they have access to and when the access expires

## Student Profile Enhancements

The student profile page now shows all videos the student has access to, along with their access codes.

### Viewing Your Accessible Videos

1. Login as a student
2. Go to your profile page
3. See the "الفيديوهات المتاحة لك" section
4. Click on any video to watch it

## Bulk Access Code Generation

Administrators can now generate multiple access codes at once.

### Generating Bulk Codes

1. Login as an administrator
2. Go to the admin dashboard
3. Click on "إنشاء أكواد وصول متعددة" or use the button in the "إدارة أكواد الوصول" card
4. Select a video or course
5. Specify the number of codes to generate (default: 100)
6. Click "إنشاء الأكواد"
7. Copy the generated codes for distribution

## Google Sheets Integration

Assignments and exams can now include links to Google Sheets and Google Forms.

### Adding Google Sheets to Assignments

1. Create or edit an assignment
2. Add the Google Sheets URL in the "رابط ملف Google Sheets" field
3. Add the Google Forms URL in the "رابط نموذج Google Forms" field
4. Save the assignment

## Troubleshooting

If you encounter any issues:

1. Make sure you're using the correct port (8080)
2. Check that your firewall isn't blocking the connection
3. Ensure you have the necessary permissions
4. Try restarting the server using `start_server.bat`

For any other issues, please contact the system administrator.

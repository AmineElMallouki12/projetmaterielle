# University Inventory Management System

A modern, web-based inventory management system designed for universities to track and manage laboratory equipment, tools, and other educational resources.

## Features

### 🏠 Dashboard
- Real-time statistics and overview
- Quick access to all system functions
- Recent activity tracking
- Visual status indicators

### 📦 Inventory Management
- Add, edit, and delete equipment
- Track equipment condition and status
- Search and filter functionality
- Bulk operations support
- Export data in multiple formats (CSV, JSON)

### 📅 Reservation System
- Create equipment reservations
- Approval workflow for reservations
- Calendar-based scheduling
- Reservation status tracking
- Conflict detection

### 📊 Reports & Analytics
- Comprehensive inventory reports
- Statistical analysis
- Usage tracking
- Export capabilities
- Visual data representation

### 🔐 User Management
- Role-based access control
- Secure authentication
- User session management
- Admin and staff roles

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Icons**: Font Awesome 6

## Installation

### Prerequisites

1. **Python 3.8+**
2. **MySQL Server**
3. **pip** (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd inventory-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL**
   - Create a new MySQL database named `inventory_db`
   - Update database configuration in `app.py`:
     ```python
     app.config['MYSQL_HOST'] = 'localhost'
     app.config['MYSQL_USER'] = 'your_username'
     app.config['MYSQL_PASSWORD'] = 'your_password'
     app.config['MYSQL_DB'] = 'inventory_db'
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Login with default credentials:
     - Username: `admin`
     - Password: `admin123`

## Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `password` (Hashed)
- `role` (admin/staff/teacher)
- `created_at` (Timestamp)

### Equipment Table
- `id` (Primary Key)
- `name` (Equipment name)
- `condition` (Good/Needs Repair/Bad/Old)
- `status` (Available/Unavailable)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

### Reservations Table
- `id` (Primary Key)
- `item_id` (Foreign Key to equipment)
- `user_name` (Reserver name)
- `start_date` (Reservation start)
- `end_date` (Reservation end)
- `status` (Pending/Active/Completed/Rejected)
- `created_at` (Timestamp)

## Usage Guide

### Adding Equipment
1. Navigate to "Add Equipment" from the dashboard
2. Fill in equipment details (name, condition, status)
3. Click "Add Equipment" to save

### Managing Inventory
1. Go to "Inventory" to view all equipment
2. Use search and filter options to find specific items
3. Click action buttons to edit, view, reserve, or delete items

### Creating Reservations
1. From inventory or reservations page, click "Make Reservation"
2. Select equipment, enter dates and user information
3. Submit the reservation request
4. Admins can approve/reject pending reservations

### Generating Reports
1. Navigate to "Reports" section
2. Select report type (Inventory, Statistics, Reservations)
3. Choose export format (PDF, CSV, JSON)
4. Download or view the generated report

## Security Features

- **Password Hashing**: All passwords are hashed using bcrypt
- **Session Management**: Secure session handling with Flask-Login
- **SQL Injection Protection**: Parameterized queries
- **CSRF Protection**: Built-in Flask CSRF protection
- **Input Validation**: Server-side validation for all inputs

## Customization

### Adding New Equipment Types
1. Modify the condition options in `add_item.html`
2. Update the database queries in `app.py`
3. Add corresponding CSS classes in `style.css`

### Customizing Reports
1. Edit the report templates in `templates/report.html`
2. Modify the report generation logic in `app.py`
3. Add new report types as needed

### Styling Changes
1. Modify `static/CSS/style.css` for visual changes
2. Update Bootstrap classes in templates
3. Add custom JavaScript in `static/JS/script.js`

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify MySQL is running
   - Check database credentials in `app.py`
   - Ensure database `inventory_db` exists

2. **Import Errors**
   - Activate virtual environment
   - Run `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

3. **Port Already in Use**
   - Change port in `app.py`: `app.run(debug=True, port=5001)`
   - Or kill existing process using port 5000

4. **Permission Errors**
   - Ensure proper file permissions
   - Run as administrator if needed (Windows)

### Performance Optimization

- Enable MySQL query caching
- Use database indexes for frequently queried columns
- Implement pagination for large datasets
- Optimize image sizes if adding equipment photos

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## Future Enhancements

- [ ] Equipment photo upload
- [ ] QR code generation for equipment
- [ ] Email notifications for reservations
- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] API for third-party integrations
- [ ] Equipment maintenance scheduling
- [ ] Barcode scanning functionality
- [ ] Advanced reporting with charts

---

**Version**: 1.0.0  
**Last Updated**: December 2024  
**Maintainer**: Development Team 
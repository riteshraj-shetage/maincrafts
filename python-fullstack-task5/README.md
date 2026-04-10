# Python Full Stack - Task 5

## Deployment Steps on Render

1. **Create a New Render Account**  
   If you haven't already, sign up for a new account on [Render](https://render.com).

2. **Create a New Web Service**
   - Navigate to the Render dashboard.
   - Click on the "New" button and select "Web Service".
   - Choose to connect your GitHub repository for the project.

3. **Configure Environment Variables**  
   In your Render settings, navigate to the "Environment" section and set the following variables:
   - `DATABASE_URL`: Your database connection URL.
   - `SECRET_KEY`: A secret key for your application.
   - `DEBUG`: Set to `false` for production.
   - Add any other environment variables needed for your application.

4. **Choose Your Build Command**  
   Configure the build command, e.g., `pip install -r requirements.txt`. This will ensure all dependencies are installed.

5. **Set the Start Command**  
   The start command should typically be defined as `gunicorn app:app` where `app` is your main application file.

6. **Deploy the Service**  
   Click on the "Create Web Service" button. Your application should now start building and deploying.

## Environment Variables

Here’s a list of environment variables you may need to configure:

- `DATABASE_URL`: The connection string for your database.
- `SECRET_KEY`: A key for securing your application (update this value).
- `DEBUG`: Boolean to enable or disable debug mode.
- Additional environment variables as required by the application.

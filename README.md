
# How to Run the Application Locally

This guide will help you set up and run the Streamlit application on your local machine.

## Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**  
   If you haven't already, clone the repository to your local machine.

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Dependencies**  
   Navigate to the directory containing `app.py` and install the required dependencies using `pip`. You can create a virtual environment if you prefer.

   ```bash
   # Create and activate a virtual environment (optional)
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   # Install dependencies
   pip install streamlit
   ```

3. **Run the Application**  
   Once the dependencies are installed, you can run the application using Streamlit.

   ```bash
   streamlit run app.py
   ```

4. **Access the Application**  
   After running the command, Streamlit will start a local server. You can access the application by opening the provided URL in your web browser, typically `http://localhost:8501`.

## Usage

- Enter a question into the text input field in the application.
- The app will provide a response based on the predefined answers.

## Troubleshooting

- If you encounter any issues, make sure all dependencies are installed correctly.
- Verify that your Python version is 3.7 or higher.

## Additional Notes

- This application uses Streamlit for the user interface.
- Ensure that you have a stable internet connection to download any necessary packages.

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes for Google Classroom API
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.me.readonly']

def authenticate_google_classroom():
    creds = None

    # Check if token.pickle exists (saved credentials)
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials, prompt the user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh expired credentials
            creds.refresh(Request())
        else:
            # Start the OAuth2 flow
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def main():
    # Authenticate and authorize
    creds = authenticate_google_classroom()

    # Build the Google Classroom API service
    service = build('classroom', 'v1', credentials=creds)

    # Example: Fetch the list of courses
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        for course in courses:
            print(course['name'])

if __name__ == '__main__':
    main()

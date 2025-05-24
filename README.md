# Mood of the Queue

A quick internal tool to log and visualize support team mood throughout the day.

## Features

- Select and log moods (😊 😠 😕 🎉) with optional notes
- Stores entries in a shared Google Sheet
- View an up-to-date bar chart showing today’s mood trend

## Setup

1. Clone the repo:

```bash
git clone https://github.com/swarba015/mochi.git
cd mochi

This app uses the Google Sheets API to read and write mood data. For security reasons, the credentials.json file (which contains private API keys) is not included in this repository. You need to create and configure your own to run the app.
```

## *Steps to set up your own credentials.json:*
1. Go to the Google Cloud Console.
2. Create a new project or select an existing one.
3. Enable the Google Sheets API and Google Drive API for the project.
4. Go to APIs & Services > Credentials.
5. Click "Create Credentials" → "Service Account".
6. After creating the service account, go to "Keys" → "Add Key" → "Create New Key" (JSON).
7. Download the generated file and save it as credentials.json in the same directory as app.py.


Once your service account is created, it will have an email like this:
```bash 
your-service-account@your-project.iam.gserviceaccount.com
Make sure to:
1. Open your Google Sheet.
2. Click Share.
3. Share the sheet with your service account email using Viewer or Editor access.


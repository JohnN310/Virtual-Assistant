# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START calendar_quickstart]
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
# [END calendar_quickstart]


# import requests

# def wolfram_alpha_query(query, app_id):
#     base_url = "http://api.wolframalpha.com/v2/query"
#     params = {
#         "input": query,
#         "format": "plaintext",
#         "output": "JSON",
#         "appid": app_id,
#     }

#     response = requests.get(base_url, params=params)
#     data = response.json()

#     return data

# # Replace 'YOUR_APP_ID' with the actual API key you obtained from Wolfram Alpha
# app_id = "JXWQV9-P9PQGYLW55"
# query = "Who is Elon Musk"

# result = wolfram_alpha_query(query, app_id)

# # Process the result
# if result["queryresult"]["success"]:
#     pods = result["queryresult"]["pods"]
#     if "subpods" in pods[1]:
#         subpods = pods[1]["subpods"]
#         for i in range(len(pods)):
#           if pods[i].get("title") == "Result":
#             print("The answer is "+ pods[i]["subpods"][0].get("plaintext"))
#           if pods[i].get("title") == "Wikipedia summary":
#             print("This is what I found on wikipedia "+pods[i]["subpods"][0].get("plaintext").split(". ")[0]+". "+pods[i]["subpods"][0].get("plaintext").split(". ")[1])
# else:
#     print("Query was not successful. Check your input or try again.")
#     print("Error:", result["queryresult"]["error"])

import datetime
import requests
import os
from dotenv import load_dotenv


class QaseMethods:
    load_dotenv()

    headers = {
        "Token": os.getenv("API_TOKEN"),
        "accept": "application/json",
        "content-type": "application/json"
    }

    def create_test_run(self, test_plan_id: int):
        """
            This method create new test run id. It accepts specific test plan id in integer format.
        """
        url = "https://api.qase.io/v1/run/EP"

        date = datetime.datetime.today().strftime("%d.%m.%Y(%H:%M)")

        payload = {
            "title": f"Debug_Darina_PlanetVPN_Extension_testing_{date}",
            "plan_id": test_plan_id
        }

        result_request = requests.post(url, json=payload, headers=self.headers)
        response_test = result_request.json()
        test_run_id = response_test['result']['id']
        return test_run_id

    def create_passed_result(self, case: int, test_run_id, time: int):
        """
            This method transfer positive result of execute test case. It accepts specific test run id, the test case id
            and time of execute the test case.
        """
        url = f"https://api.qase.io/v1/result/EP/{test_run_id}"

        payload = {
            "status": "passed",
            "case_id": case,
            "time_ms": f"{int(time)}"
        }

        response = requests.post(url, json=payload, headers=self.headers)
        print(response.text)
        return case

    def create_failed_result(self, case: int, test_run_id, time: int, comment):
        """
            This method transfer negative result of execute test case. It accepts specific test run id, the test case id
            and time of execute the test case.
        """
        url = f"https://api.qase.io/v1/result/EP/{test_run_id}"

        payload = {
            "status": "failed",
            "case_id": case,
            "time_ms": f"{int(time) * 1000}",
            "comment": comment

        }

        response = requests.post(url, json=payload, headers=self.headers)
        print(response.text)
        return case

    def update_publicity_test_run(self, test_run_id: int):
        """
            This method makes the test run public.
        """
        url = f"https://api.qase.io/v1/run/EP/{test_run_id}/public"

        payload = {
            "status": True
        }
        response = requests.patch(url, json=payload, headers=self.headers)
        response_json = response.json()
        public_test_run_url = response_json['result']['url']
        return public_test_run_url

    def send_test_run_url_to_slack(self, public_test_run_url: str, test_time, slack_channel) -> int:
        """
        This method sends the public URL with test run results to a specific Slack channel.
        """
        date = datetime.datetime.today().strftime("%d.%m.%Y")

        payload = {
            "channel": slack_channel,
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":gear: <{public_test_run_url}|*Debug_PlanetVPN_Extension_testing_{date}({test_time})*>\n "
                            f"В случае проблемы обращаться к <@U03LV5XPYCX>"
                }
            }]
        }

        headers = {
            "content-type": "application/json"
        }
        load_dotenv()
        slack_url = os.getenv("SLACK_URL_GIT")
        print(f"Sending report to channel: {slack_channel}, URL: {slack_url}")

        response = requests.post(slack_url, json=payload, headers=headers)
        return response.status_code






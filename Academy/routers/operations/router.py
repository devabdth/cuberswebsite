from flask import Flask, request
import os
import json


class OperationsRouter:
    def __init__(self, app: Flask, config):
        self.app = app
        self.database_helper = config.database_helper
        self.emailing_model = config.emailing

    def assign_routers(self):
        self.subscribe()
        self.notifications()

    def subscribe(self):
        @self.app.route('/subscriptions/', methods=["POST"])
        def subscripte():
            self.database_helper.subscriptions.load()
            data = dict(json.loads(request.data))
            try:
                emails = []
                for dict_ in self.database_helper.subscriptions.subscriptions_data.values():
                    emails.append(dict_["email"])

                if not data["email"] in emails:
                    self.database_helper.subscriptions.subscriptions_data["data"].append(
                        data)
                    self.database_helper.subscriptions.save()
                    return self.app.response_class(status=201)

                else:
                    return self.app.response_class(status=301)
            except Exception as e:
                print(e)
                return self.app.response_class(status=404)

    def notifications(self):
        @self.app.route('/notification/code/', methods=["POST"])
        def notifications_code():
            self.database_helper.subscriptions.load()
            recipients = []
            for dict_ in self.database_helper.subscriptions.subscriptions_data.values():
                recipients.append(dict_["email"])
            data = json.loads(request.data)
            print(dict(data))
            email_data: dict = {
                "subject": data["subject"],
                "recipients": recipients,
            }

            self.emailing_model.send_email_with_code(
                title=data["title"],
                desc=data["desc"],
                code=data["code"],
                email_data=email_data,
            )
            return self.app.response_class(status=200)

        @self.app.route('/notification/actions/', methods=["POST"])
        def notifications_actions():
            self.database_helper.subscriptions.load()
            recipients = []
            for dict_ in self.database_helper.subscriptions.subscriptions_data.values():
                recipients.append(dict_["email"])
            data = json.loads(request.data)
            print(dict(data))
            email_data: dict = {
                "subject": data["subject"],
                "recipients": recipients,
            }

            self.emailing_model.send_email_with_actions(
                title=data["title"],
                desc=data["desc"],
                primary_action_title=data["primary_action_title"],
                primary_action_href=data["primary_action_href"],
                second_action_title=data["second_action_title"],
                second_action_href=data["second_action_href"],
                email_data=email_data,
            )
            return self.app.response_class(status=200)

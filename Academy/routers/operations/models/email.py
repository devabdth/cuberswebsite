import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Emailing:
    def __init__(self, email, access_key):
        self.credentials: dict = {'email': email, 'access_key': access_key}
        self.temps = Temps()

    def send_email_with_code(self, title, desc, code, email_data: dict):
        temp = self.temps.code_container(
            title=title, desc=desc, code=code)

        session = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        session.login(self.credentials["email"],
                      self.credentials["access_key"])

        msg: MIMEMultipart = MIMEMultipart('alternative')
        msg["Subject"] = email_data["subject"]
        msg["From"] = self.credentials["email"]
        msg.attach(MIMEText(temp, 'html'))

        for recipient in email_data["recipients"]:
            try:
                print(self.credentials["email"])
                print(msg)
                msg["To"] = recipient
                print('Done1')
                session.sendmail(
                    from_addr=self.credentials["email"],
                    to_addrs=recipient,
                    msg=msg.as_string()
                )
                print('Sent')
            except Exception as e:
                print(e)

    def send_email_with_actions(self, title, desc, primary_action_title, primary_action_href, second_action_title, second_action_href, email_data):
        temp = self.temps.actions_container(
            title=title, desc=desc, primary_action_title=primary_action_title, primary_action_href=primary_action_href, second_action_href=second_action_href, second_action_title=second_action_title)

        session = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        session.login(self.credentials["email"],
                      self.credentials["access_key"])

        msg: MIMEMultipart = MIMEMultipart('alternative')
        msg["Subject"] = email_data["subject"]
        msg["From"] = self.credentials["email"]
        msg.attach(MIMEText(temp, 'html'))

        for recipient in email_data["recipients"]:
            try:
                print(self.credentials["email"])
                print(msg)
                msg["To"] = recipient
                print('Done1')
                session.sendmail(
                    from_addr=self.credentials["email"],
                    to_addrs=recipient,
                    msg=msg.as_string()
                )
                print('Sent')
            except Exception as e:
                print(e)


class Temps:
    def __init__(self):
        pass

    def code_container(self, title, desc, code):
        return r"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Cubers Academy</title>
                <style>
                    * {
                        box-sizing: border-box;
                        margin: 0;
                        padding: 0;
                    }
                    /* --accentColor: #4ea827; */
                    body {
                        background-color: #111;
                        display: flex;
                        height: 100%;
                        width: 100%;
                        flex-direction: column;
                        align-items: start;
                        justify-content: center;
                    }

                    h2 {
                        margin: 8px 16px;
                        font-weight: 900;
                        font-size: 48px;
                        font-family: "Agency FB";
                        color: white;
                    }

                    p {
                        margin: 8px 16px;
                        font-family: "Quicksand";
                        font-weight: 100;
                        color: rgba(255, 255, 255, 0.6);
                    }

                    a {
                        font-family: "Quicksand";
                        font-weight: 100;
                        color: rgba(255, 255, 255, 0.6);
                    }

                    .actions {
                        background-color: #222;
                        display: flex;
                        margin: 20% 0;
                        justify-content: center;
                        align-items: center;
                        border-radius: 12px;
                        margin: 32px 64px;
                        position: absolute;
                        left: 0;
                        right: 0;
                        bottom: 25%;
                    }

                    .actions > h1 {
                        color: white;
                        background-color: #4ea827;
                        border-radius: 12px;
                        padding: 32px 64px;
                        font-weight: 100;
                        font-family: "Agency FB";
                        margin: 48px 64px;
                    }

                    .main-button {
                        padding: 8px 16px;
                        margin: 48px 8px;
                        color: white;
                        font-family: "Quicksand";
                        font-weight: 100;
                        background-color: #4ea827;
                        font-size: 1.5em;
                        border-radius: 12px;
                        border: 1px #4ea827 solid;
                        transition: 500ms ease;
                    }

                    .main-button:hover {
                        background-color: transparent;
                        color: #4ea827;
                    }

                    .shadow-button {
                        padding: 8px 16px;
                        margin: 10vh 12px;
                        color: white;
                        font-family: "Quicksand";
                        font-weight: 100;
                        font-size: 0.75em;
                    }

                    footer {
                        position: absolute;
                        bottom: 0;
                        width: 100%;
                        height: 10%;
                        display: flex;
                        align-items: center;
                        justify-content: space-between;
                    }
                </style>
            </head>
            <body>
                <h2>"""+title+"""</h2>
                <p>&emsp;"""+desc+"""</p>
                <div class="actions">
                    <h1>"""+code+"""</h1>
                </div>
                <footer>
                <p>Phone: <a href="tel:+20 112 916 4522">+20 112 916 4522</a></p>
                <p>
                    Website:
                    <a href="https://academy.cubersio.com">https://academy.cubersio.com</a>
                </p>
                <p>
                    <a href="http://facebook.com/cuberacd" target="_blank">@cubersacd</a>
                </p>
                </footer>
            </body>
            </html>
        """

    def actions_container(self, title, desc, primary_action_title, primary_action_href, second_action_title, second_action_href):
        return r"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Cubers Academy</title>
                <style>
                    * {
                        box-sizing: border-box;
                        margin: 0;
                        padding: 0;
                    }
                    /* --accentColor: #4ea827; */
                    body {
                        background-color: #111;
                        display: flex;
                        height: 100%;
                        width: 100%;
                        flex-direction: column;
                        align-items: start;
                        justify-content: center;
                    }

                    h2 {
                        margin: 8px 16px;
                        font-weight: 900;
                        font-size: 48px;
                        font-family: "Agency FB";
                        color: white;
                    }

                    p {
                        margin: 8px 16px;
                        font-family: "Quicksand";
                        font-weight: 100;
                        color: rgba(255, 255, 255, 0.6);
                    }

                    a {
                        font-family: "Quicksand";
                        font-weight: 100;
                        color: rgba(255, 255, 255, 0.6);
                    }

                    .actions {
                        background-color: #222;
                        display: flex;
                        margin: 20% 0;
                        justify-content: center;
                        align-items: center;
                        border-radius: 12px;
                        margin: 32px 64px;
                        position: absolute;
                        left: 0;
                        right: 0;
                        bottom: 25%;
                    }

                    .actions > h1 {
                        color: white;
                        background-color: #4ea827;
                        border-radius: 12px;
                        padding: 32px 64px;
                        font-weight: 100;
                        font-family: "Agency FB";
                        margin: 48px 64px;
                    }

                    .main-button {
                        padding: 8px 16px;
                        margin: 48px 8px;
                        color: white;
                        font-family: "Quicksand";
                        font-weight: 100;
                        background-color: #4ea827;
                        font-size: 1.5em;
                        border-radius: 12px;
                        border: 1px #4ea827 solid;
                        transition: 500ms ease;
                    }

                    .main-button:hover {
                        background-color: transparent;
                        color: #4ea827;
                    }

                    .shadow-button {
                        padding: 8px 16px;
                        margin: 10vh 12px;
                        color: white;
                        font-family: "Quicksand";
                        font-weight: 100;
                        font-size: 0.75em;
                    }

                    footer {
                        position: absolute;
                        bottom: 0;
                        width: 100%;
                        height: 10%;
                        display: flex;
                        align-items: center;
                        justify-content: space-between;
                    }
                </style>
            </head>
            <body>
                <h2>"""+title+r"""</h2>
                <p>&emsp;"""+desc+r"""</p>
                <div class="actions">
                    <a href='"""+primary_action_href+r"""' class="main-button" style="text-decoration: none">"""+primary_action_title+r"""</a>
                    <a href='"""+second_action_href+r"""' class="shadow-button">"""+second_action_title+r"""</a>

                </div>
                <footer>
                <p>Phone: <a href="tel:+20 112 916 4522">+20 112 916 4522</a></p>
                <p>
                    Website:
                    <a href="https://academy.cubersio.com">https://academy.cubersio.com</a>
                </p>
                <p>
                    <a href="http://facebook.com/cuberacd" target="_blank">@cubersacd</a>
                </p>
                </footer>
            </body>
            </html>
        """

import datetime
from datetime import timezone


class EmailManager:

    def __init__(self):
        self.port = 587  # For starttls
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = "RNMmoneyprinter@gmail.com"
        self.receiver_email = "RNMmoneyprinter@gmail.com"
        self.password = "amddebyotxjrbjep"

    def send_email(self, symbol, amount, price, method="buy"):
        import smtplib, ssl

        time = datetime.datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        if method == "buy":
            SUBJECT = f"CryptBot just bought {symbol} for {price}"
            TEXT = f"""\
            The CryptoBot just bought {amount} units of {symbol} in GateIO.
            
            Buy price was {price}
            
            The execution time was {time} (UTC).
            """
        else:
            SUBJECT = f"CryptBot just sold {symbol} for {price}"
            TEXT = f"""\
            The CryptoBot just sold {amount} units of {symbol} in GateIO.
            
            Sell price was {price}
            
            The execution time was {time} (UTC).
            """
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message)


if __name__ == '__main__':
    x = EmailManager()
    x.send_email("Ron", "213", "100")
    x.send_email("Ron", "213", "120", method="sell")
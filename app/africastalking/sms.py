from app import app
import africastalking

africastalking.initialize(
    username=app.config["AFRICASTALKING_USERNAME"],
    api_key=app.config["AFRICASTALKING_API_KEY"]
)

# initialize africastalking SMS
sms = africastalking.SMS

class send_sms():
    def send(self, MSISDN, message):
        # Set the numbers in international format
        recipients = [MSISDN]
        # Set your shortCode or senderId
        sender = "SAVANNAH"
        try:
            response = sms.send(message, recipients, sender)
            app.logger.info (response)
        except Exception as err:
            app.logger.error(f"Unexpected {err=}")
            return type(err).__name__

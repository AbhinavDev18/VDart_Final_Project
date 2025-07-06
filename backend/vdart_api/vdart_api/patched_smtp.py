from django.core.mail.backends.smtp import EmailBackend as OriginalBackend

class PatchedEmailBackend(OriginalBackend):
    def open(self):
        """
        Patch for Python 3.12: avoid passing keyfile/certfile to starttls()
        """
        if self.connection:
            return False

        try:
            self.connection = self.connection_class(
                self.host,
                self.port,
                timeout=self.timeout
            )
        except Exception:
            if not self.fail_silently:
                raise
            return False

        # Identify ourselves to the SMTP server
        self.connection.ehlo()

        if self.use_tls:
            # FIX: Do not pass keyfile/certfile here
            self.connection.starttls()
            self.connection.ehlo()

        if self.username and self.password:
            try:
                self.connection.login(self.username, self.password)
            except Exception:
                if not self.fail_silently:
                    raise
                return False

        return True

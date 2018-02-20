import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("kushalgowda146@gmail.com","9113208970")
msg="hi how are you"
s.sendmail("kushalgowda146@gmail.com","kushal.17cs@cmr@edu.in",msg)
print("success")
s.quit()

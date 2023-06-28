import tkinter as tk
import smtplib
from tkinter import messagebox

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("Mail Application")
        master.config(background="lightgray")

        # Create the UI
        self.from_label = tk.Label(master, text="From:", background="lightgray")
        self.from_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)
        self.from_entry = tk.Entry(master, width=50)
        self.from_entry.grid(row=0, column=1, sticky="w", pady=10)

        self.pass_label = tk.Label(master, text="Password:", background="lightgray")
        self.pass_label.grid(row=1, column=0, sticky="w", padx=5, pady=10)
        self.pass_entry = tk.Entry(master, width=50, show="*")
        self.pass_entry.grid(row=1, column=1, sticky="w", pady=10)

        self.to_label = tk.Label(master, text="To:", background="lightgray")
        self.to_label.grid(row=2, column=0, sticky="w", padx=5, pady=10)
        self.to_entry = tk.Entry(master, width=50)
        self.to_entry.grid(row=2, column=1, sticky="w", pady=10)

        self.subject_label = tk.Label(master, text="Subject:", background="lightgray")
        self.subject_label.grid(row=3, column=0, sticky="w", padx=5, pady=10)
        self.subject_entry = tk.Entry(master, width=50)
        self.subject_entry.grid(row=3, column=1, sticky="w", pady=10)

        self.body_label = tk.Label(master, text="Body:", background="lightgray")
        self.body_label.grid(row=4, column=0, sticky="w", padx=5, pady=10)
        self.body_text = tk.Text(master, height=6, width=50)
        self.body_text.grid(row=4, column=1, sticky="w", pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_mail, width=16,
                                     background="Purple", foreground="White", font=("Helvetica", 12, "bold"))
        self.send_button.grid(row=5, column=0, columnspan=2, pady=20)

    def send_mail(self):
        # Get the email data from the UI
        from_address = self.from_entry.get()
        password = self.pass_entry.get()
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END).strip()

        # Validate the required fields
        if not from_address or not password or not to_address or not subject or not body:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        try:
            # Connect to the SMTP server
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_address, password)

            # Create the email message
            message = f"Subject: {subject}\n\n{body}"

            # Send the email
            server.sendmail(from_address, to_address, message)

            # Server clean up
            server.quit()

            messagebox.showinfo("Success", "Email sent successfully!")
            self.master.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.geometry("500x350")
root.config(background="lightgray")
mail_app = MailApp(root)
root.mainloop()

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time

class HealthDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Dashboard")
        self.root.geometry("600x800")
        self.root.configure(bg='#f0f8ff')


        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.file_var = tk.StringVar()
        self.progress_var = tk.DoubleVar()

      
        main_frame = tk.Frame(root, bg='#f0f8ff')
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

       
        form_card = tk.Frame(main_frame, bg='white', relief=tk.RAISED, borderwidth=1)
        form_card.pack(fill=tk.X, pady=(0, 20))


        title_label = tk.Label(
            form_card, 
            text="Health Dashboard", 
            font=('Arial', 20, 'bold'), 
            fg='#2563eb', 
            bg='white'
        )
        title_label.pack(pady=10)

       
        name_frame = tk.Frame(form_card, bg='white')
        name_frame.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(name_frame, text="Name", bg='white').pack(anchor='w')
        name_entry = tk.Entry(
            name_frame, 
            textvariable=self.name_var, 
            font=('Arial', 12), 
            width=50
        )
        name_entry.pack(fill=tk.X, pady=(0, 10))


        age_frame = tk.Frame(form_card, bg='white')
        age_frame.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(age_frame, text="Age", bg='white').pack(anchor='w')
        age_entry = tk.Entry(
            age_frame, 
            textvariable=self.age_var, 
            font=('Arial', 12), 
            width=50
        )
        age_entry.pack(fill=tk.X, pady=(0, 10))


        file_frame = tk.Frame(form_card, bg='white')
        file_frame.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(file_frame, text="Upload Health Records", bg='white').pack(anchor='w')
        file_entry = tk.Entry(
            file_frame, 
            textvariable=self.file_var, 
            font=('Arial', 12), 
            width=50, 
            state='readonly'
        )
        file_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

        file_button = tk.Button(
            file_frame, 
            text="Browse", 
            command=self.upload_file,
            bg='#2563eb',
            fg='white'
        )
        file_button.pack(side=tk.RIGHT)

        
        submit_button = tk.Button(
            form_card, 
            text="Submit Health Information", 
            command=self.submit_form,
            bg='#2563eb',
            fg='white',
            font=('Arial', 12)
        )
        submit_button.pack(padx=20, pady=20, fill=tk.X)

       
        self.progress_bar = ttk.Progressbar(
            form_card, 
            variable=self.progress_var, 
            maximum=100
        )
        self.progress_bar.pack(padx=20, pady=(0, 10), fill=tk.X)

 
        summary_card = tk.Frame(main_frame, bg='white', relief=tk.RAISED, borderwidth=1)
        summary_card.pack(fill=tk.X)

        tk.Label(
            summary_card, 
            text="Health Summary", 
            font=('Arial', 16, 'bold'), 
            fg='#2563eb', 
            bg='white'
        ).pack(pady=10)

        summary_details_frame = tk.Frame(summary_card, bg='white')
        summary_details_frame.pack(padx=20, pady=10, fill=tk.X)

       
        name_summary = tk.Frame(summary_details_frame, bg='#e3f2fd')
        name_summary.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        tk.Label(name_summary, text="Name", font=('Arial', 10, 'bold'), bg='#e3f2fd').pack(pady=(10,5))
        self.name_summary_label = tk.Label(
            name_summary, 
            text="Not provided", 
            bg='#e3f2fd'
        )
        self.name_summary_label.pack(pady=(0,10))

       
        age_summary = tk.Frame(summary_details_frame, bg='#e8f5e9')
        age_summary.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        tk.Label(age_summary, text="Age", font=('Arial', 10, 'bold'), bg='#e8f5e9').pack(pady=(10,5))
        self.age_summary_label = tk.Label(
            age_summary, 
            text="Not provided", 
            bg='#e8f5e9'
        )
        self.age_summary_label.pack(pady=(0,10))

        
        file_summary = tk.Frame(summary_details_frame, bg='#fff3e0')
        file_summary.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        tk.Label(file_summary, text="Uploaded File", font=('Arial', 10, 'bold'), bg='#fff3e0').pack(pady=(10,5))
        self.file_summary_label = tk.Label(
            file_summary, 
            text="No file uploaded", 
            bg='#fff3e0'
        )
        self.file_summary_label.pack(pady=(0,10))

    def upload_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_var.set(filename)

    def submit_form(self):
      
        if not self.name_var.get().strip():
            messagebox.showerror("Error", "Please enter your name")
            return

        try:
            age = int(self.age_var.get())
            if age < 0 or age > 120:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age between 0 and 120")
            return

    
        self.name_summary_label.config(text=self.name_var.get())
        self.age_summary_label.config(text=self.age_var.get())
        
        if self.file_var.get():
            self.file_summary_label.config(text=self.file_var.get().split('/')[-1])

   
        def simulate_submission():
            for i in range(11):
                self.progress_var.set(i * 10)
                time.sleep(0.2)
            
           
            self.root.after(0, self.reset_form)

        threading.Thread(target=simulate_submission, daemon=True).start()

    def reset_form(self):
        self.name_var.set('')
        self.age_var.set('')
        self.file_var.set('')
        self.progress_var.set(0)

def main():
    root = tk.Tk()
    app = HealthDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
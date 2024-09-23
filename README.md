 `README.md`

# BURSARY DISBURSEMENT APP

![BUDA Logo](./web_static/images/BUDA_logo.png)

## Project Description

The **Bursary Disbursement App** is designed to streamline the process of disbursing bursaries to eligible students from various institutions. The app facilitates the management of bursary applications, making the process more efficient, transparent, and accessible. Students can apply for financial aid, institutions can process applications, and administrators can easily manage the distribution of funds through a centralized system.

### Live Demo
- **Deployed Site**: [Bursary Disbursement App](https://your-deployed-site-link.com)
- **Final Blog Article**: [The Journey of Building the Bursary App](https://your-blog-link.com)
- **Author LinkedIn**: 
    - [Your Name](https://www.linkedin.com/in/engineerphil/)

## Features
- **Student Portal**: Students can register, apply for bursaries, and track their applications.
- **Institution Portal**: Institutions can verify and process applications.
- **Admin Panel**: Bursary administrators can review, approve, and allocate funds.
- **Custom Command Interpreter**: A built-in command-line tool for managing bursary applications, institutions, and students.

## Command Interpreter

The app includes a command interpreter to allow administrators to create, update, and manage bursary-related data directly via the console.

### How to Start the Command Interpreter

1. **Clone the Repository**: First, clone the repository from GitHub.
   ```bash
   git clone https://github.com/your-username/bursary-disbursement-app.git
   cd bursary-disbursement-app
   ```

2. **Set Up the Virtual Environment**:
   Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install all required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Command Interpreter**:
   ```bash
   ./bursary_interpreter.py
   ```

### How to Use the Command Interpreter

The command interpreter allows you to create, update, and manage bursary applications, institutions, and students.

#### Example Commands:

- **Create a new institution**:
   ```bash
   create Institution name="Institution Name" address="Institution Address" contact="Contact Info"
   ```

- **Create a new student**:
   ```bash
   create Student first_name="John" last_name="Doe" institution_id=1
   ```

- **Apply for a bursary**:
   ```bash
   create BursaryApplication student_id=1 amount_requested=50000 status="Pending"
   ```

### 📊 Examples
- **Creating an Institution**:
   ```bash
   $ create Institution name="Green Valley High School" address="123 Green Valley Road" contact="0712345678"
   Institution created with ID: 1
   ```

- **Creating a Student**:
   ```bash
   $ create Student first_name="John" last_name="Doe" institution_id=1
   Student created with ID: 1
   ```

## Installation

To install and run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/bursary-disbursement-app.git
   cd bursary-disbursement-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   Run migrations to set up the database:
   ```bash
   flask db upgrade
   ```

5. **Run the Flask app**:
   ```bash
   flask run
   ```

6. **Access the app**:
   The app will be running on `http://localhost:5000/`.

## Usage

Once installed, the Bursary Disbursement App allows students, institutions, and administrators to interact through different interfaces. Here’s a brief usage guide:

- **Students** can register, apply for bursaries, and check their application status.
- **Institutions** can manage and verify student applications.
- **Administrators** can review applications, allocate bursary funds, and track disbursement history.

### Screenshot of the Application

![Bursary App Screenshot](./images/screenshot.png)

## Contributing

Contributions are welcome! Here’s how you can get involved:

1. **Fork the repository** on GitHub.
2. **Create your feature branch**: 
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit your changes**: 
   ```bash
   git commit -m "Add a detailed commit message"
   ```
4. **Push to the branch**: 
   ```bash
   git push origin feature/your-feature
   ```
5. **Create a pull request**.

## Related Projects

- [AirBnB Clone](https://github.com/yourusername/AirBnB_clone): A project that inspired this app’s structure.
- [Flask App Template](https://github.com/yourusername/Flask_Template): Boilerplate code used to start this project.

## Licensing

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Resources

- **What Your Code Repository Says About You**: [Link](https://example.com)
- **Awesome List of READMEs**: [Link](https://example.com)

## Reflection and Challenges

The **Bursary Disbursement App** was created to address the need for a more efficient, transparent, and accessible way to manage bursary applications. 

### Challenges
1. **Database Integration**: Designing a flexible database that supports various institutions' different systems.
2. **Streamlining Bureaucratic Processes**: Getting buy-in from government officials to use the platform was a challenge due to manual processes that benefited some individuals.
3. **Real-Time Bursary Allocation**: Ensuring funds were allocated quickly and fairly based on student needs was technically challenging due to different income brackets and orphan status adjustments.

### Next Steps
1. **Automating Verification**: Integrating more government and institutional databases to automatically verify student details.
2. **Machine Learning**: Adding prediction models to recommend bursary amounts based on historical data.
3. **Mobile Application**: Developing a mobile-friendly version for easier access by students.

### Conclusion

The **Bursary Disbursement App** is an efficient and user-friendly solution that addresses real-world problems in bursary allocation. With future improvements and features in the pipeline, it will further enhance the accessibility and transparency of bursary management systems.

![Additional Screenshot](./images/additional-screenshot.png)
```

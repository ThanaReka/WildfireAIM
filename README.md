# Wildire AIM

![Alt text for image](https://github.com/ThanaReka/WildfireAIM/blob/main/assets/screenshot1.png)

## Wildfire AIM (AI Mitigation)
* Wildire mitigation and prevention system, powered by Microsoft Azure AI Technologies
* Developed for the AI Innovation Challenge in June 2025

### About
* Wildfire AIM was built as a RAG (Retrieval Augmented Generation) Search Chat Application.
* Its focus is on promoting prescribed burning as a wildfire prevention and mitigation method, as practiced by the Karuk Tribe of Northern California.
* Our system provides culturally sensitive guidelines for US government agencies to expand the use of prescribed burning in cooperation with native tribes.

### Tech Stack
* Frontend: Python, Bootstrap
* Backend: Python, Flask
* Azure AI Backend: Configured through Azure Portal (see `ai-backend` for details)

### Project Presentation
* https://speakerdeck.com/vuinguyen/wildfire-aim-ai-mitigation

### Demo Video
* https://bit.ly/WildfireAIM-Demo

### Running our project
Wildfire AIM is a one-page web application built with Flask and Bootstrap to provide information on wildfire management, specifically focusing on prescribed burning. Users can search through a Q&A database to learn about wildfire management techniques.
Project Structure
WildfireAIM/
├── backend/
│   ├── wildfire_app.py
│   └── data/
│       └── data.json
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── styles.css
├── README.md
└── requirements.txt

Setup Instructions

Clone the Repository:
git clone https://github.com/ThanaRekan/WildfireAIM.git
cd WildfireAIM


Set up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the Application:
python backend/wildfire_app.py

Open a browser and navigate to http://127.0.0.1:5000.

Using the Application:

The homepage features a hero image and a search bar.
Enter terms like "prescribed burning" or "regulatory" to filter Q&A content.
Results are displayed in an accordion format, with questions as headers and answers expandable.

![Alt text for image](https://github.com/ThanaReka/WildfireAIM/blob/main/assets/screenshot2.png)

Data Customization

Edit backend/data/data.json to add more Q&A pairs in the format:{
    "question": "Your question here",
    "answer": "Your answer here with <br> for line breaks"
}



Dependencies

Flask: Backend web framework
Bootstrap 5.3.0: Frontend styling (loaded via CDN)

Contributing

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make changes and commit: git commit -m "Description of changes".
Push to the branch: git push origin feature-branch.
Create a pull request on GitHub.

License
MIT License

### For questions, contact our team:
- [Vui Nguyen](https://github.com/vuinguyen)
- [Reka Thanabalan](https://github.com/ThanaReka)

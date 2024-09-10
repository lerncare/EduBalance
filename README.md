# EduBalance

EduBalance is an AI-driven platform for teacher well-being and professional development using Flask and Vanilla JS.

## Features

- KI-gesteuertes persönliches Coaching (AI-driven personal coaching)
- Immersive Lernumgebungen (Immersive learning environments)
- Kollaboratives Problemlösen (Collaborative problem-solving)
- Adaptive Ressourcenbibliothek (Adaptive resource library)
- Biofeedback und Stressmanagement (Biofeedback and stress management)
- Community-basierte Unterstützung (Community-based support)
- Datengesteuerte Schulentwicklung (Data-driven school development)
- Integriertes Zeitmanagement (Integrated time management)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/lerncare/EduBalance.git
   cd EduBalance
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following variables:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

4. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```
   python app.py
   ```

The application will be available at `http://localhost:5000`.

## Project Structure

- `app.py`: Main application file
- `config.py`: Configuration settings
- `extensions.py`: Flask extensions
- `models/`: Database models
- `routes/`: Application routes
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)
- `utils/`: Utility functions

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

from app import app, calculate_team_scores

# Ensure the app context is available for database operations
with app.app_context():
    calculate_team_scores()
    print("Weekly team scores calculated and updated.")
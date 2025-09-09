import random
from datetime import datetime, timedelta
from flask import Flask, render_template_string

# Initialisation de l'application Flask
app = Flask(__name__)

# --- Variables globales pour conserver l'état de l'application ---
current_response = None
expiration_time = None

# --- Liste des réponses possibles ---
DELIGHTED_RESPONSES = [
    "Yes, I'm absolutely delighted today!", 
    "Indeed, I am!",
    "Delighted is an understatement.", 
    "Very much so, thank you for asking.", 
    "100% delighted.",
    "Yes, and I hope you are too!", 
    "Of course!",
    "Positively delighted.", 
    "Absolutely, unequivocally delighted.", 
    "I'm not so delighted.", "No, I'm not.",
    "Far from it, actually.", 
    "Ask me again tomorrow.",
    "I've felt more delighted on other occasions.", 
    "The opposite of delighted, whatever that is.",
    "Unfortunately, not today.", 
    "I'm running low on delight.",
    "I'm feeling rather neutral, to be honest.", 
    "Define 'delighted'.",
    "That's a complex question.", 
    "Perhaps.",
    "Maybe a little bit.", 
    "I'm in a state of non-delightedness.",
    "Slightly delighted.", 
    "It's complicated.",
    "I'm as delighted as a Monday morning.", 
    "My delight comes and goes.",
    "Sometimes I am, sometimes I'm not.",
    "That's personal.", 
    "I could be, for the right price.",
    "My delight is immeasurable.",
    "I'm so delighted today!",
    "Not feeling very delighted at all.",
    "My delight seems to have vanished.",
    "I couldn't be more delighted.",
    "I am not delighted in the slightest.",
    "Yes, I feel truly delighted.",
    "Absolutely, I am delighted!",
    "Pure delight is what I feel.",
    "Delight is a foreign concept to me right now.",
    "I'm far from delighted.",
    "My heart is so full of delight.",
    "I'm feeling rather the opposite of delighted.",
    "Delighted and ready for the day!",
    "Unfortunately, no delight here.",
    "I'm completely devoid of delight.",
    "Delight has not visited me today.",
    "This makes me so delighted.",
    "I can't say I'm delighted.",
    "Yes, it's a feeling of pure delight.",
    "I'm completely delighted.",
    "My delight has taken a vacation.",
    "This is the least delightful I've ever felt.",
    "Feeling pretty delighted, thanks for asking.",
    "There is no delight to be found.",
    "Delighted to be alive.",
    "Everything feels quite the opposite of delightful.",
    "I am quite delighted.",
    "Delighted? Hardly.",
    "I'm not in a state of delight.",
    "I am not even a little bit delighted.",
    "I am in a state of delight.",
    "I wish I could say I was delighted.",
    "My delight knows no bounds.",
    "Not at all delighted.",
    "I am absolutely not delighted."
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Are you delighted?</title>
    <style>
        :root {
            --color-background: #121212;
            --color-surface: #1e1e1e;
            --color-primary: #BB86FC;
            --color-secondary: #03DAC6;
            --color-text: #e0e0e0;
            --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --border-radius: 8px;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: var(--font-family);
            background-color: var(--color-background);
            color: var(--color-text);
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
        .navbar { background-color: var(--color-surface); padding: 1rem 0; border-bottom: 1px solid #333; }
        .navbar .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.5rem; font-weight: bold; color: var(--color-primary); text-decoration: none; }
        main {
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .hero h1 {
            font-size: 3.5rem;
            font-weight: 300;
            padding: 2rem;
            border-radius: var(--border-radius);
            background-color: var(--color-surface);
            box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3);
            max-width: 800px;
        }
        .footer { background-color: var(--color-surface); text-align: center; padding: 2rem 0; border-top: 1px solid #333; color: #888; }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
        }
    </style>
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="container">
                <a href="/" class="logo">AreYouDelighted?</a>
            </div>
        </nav>
    </header>
    <main>
        <section class="hero">
            <div class="container">
                <h1>{{ message }}</h1>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>&copy; {{ year }} - Une réponse à la fois.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def are_you_delighted():
    global current_response, expiration_time
    if expiration_time is None or datetime.now() > expiration_time:
        current_response = random.choice(DELIGHTED_RESPONSES)
        random_duration_seconds = random.randint(60, 86400) # 60s à 24h
        expiration_time = datetime.now() + timedelta(seconds=random_duration_seconds)
        
        print(f"--- NOUVELLE RÉPONSE SÉLECTIONNÉE ---")
        print(f"Réponse: '{current_response}'")
        print(f"Expire à: {expiration_time.strftime('%Y-%m-%d %H:%M:%S')}")

    return render_template_string(
        HTML_TEMPLATE, 
        message=current_response, 
        year=datetime.now().year
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


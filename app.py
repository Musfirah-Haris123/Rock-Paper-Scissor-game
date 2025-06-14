from flask import Flask, render_template, request, redirect, url_for, session
import random

app= Flask(__name__)
app.secret_key="your_secret_key_here"
def determine_result(player,computer):
    if player == computer:
        return "Draw"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
         return "You Win"
    else:
        return "Computer Win"
    
          
    
@app.route('/', methods=['GET','POST'])
def index():
    if 'score' not in session:
        session['score'] = {'player' : 0, 'computer': 0, 'draw' : 0, 'rounds': 0}
    player_choice = None
    computer_choice = None
    result = None


    if request.method == 'POST':
        player_choice = request.form['player_choice']
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result =determine_result (player_choice,computer_choice)
        if result == "Draw":
            session['score']['draw'] +=1
        elif result == "You Win":
            session['score']['player'] +=1
        else:
             session['score']['computer'] +=1
             session['score']['rounds']+=1
             session.modified=True
          
        
             
    return render_template('index.html', player_choice=player_choice, computer_choice=computer_choice,result=result,score=session["score"])

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)


    
       
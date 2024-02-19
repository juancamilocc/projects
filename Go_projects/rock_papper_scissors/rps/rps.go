package rps

import (
	"math/rand"
	"strconv"
)

const (
	ROCK     = 0 // Rock. Beats scissors. (scissors + 1) %3 = 0
	PAPER    = 1 // Paper. Beats rock. (rock + 1) %3 = 1
	SCISSORS = 2 // Scissors. Beats paper. (paper + 1) %3 = 2
)

// Structure for giving each result per round
type Round struct {
	Message           string `json:"message"`
	ComputerChoice    string `json:"computer_choice"`
	RoundResult       string `json:"round_result"`
	ComputerChoiceInt int    `json:"computer_choice_int"`
	ComputerScore     string `json:"computer_score"`
	PlayerScore       string `json:"player_score"`
}

// Win message
var winMessage = []string{
	"Well Done!",
	"Good Job",
	"You must buy a lottery ticket",
}

// Lose message
var loseMessage = []string{
	"What a Pity!",
	"Try Again!",
	"Today is just not your day!",
}

// Draw message
var drawMessage = []string{
	"Greats mind think alike",
	"Or not. Try Again.",
	"Nobody wins, but you can try again.",
}

// Score variables
var ComputerScore, PlayerScore int

func PlayRound(playerValue int) Round {
	computerValue := rand.Intn(3)

	var computerChoice, roundResult string
	var computerChoiceInt int

	switch computerValue {
	case ROCK:
		computerChoiceInt = ROCK
		computerChoice = "The computer chose ROCK"

	case PAPER:
		computerChoiceInt = PAPER
		computerChoice = "The computer chose PAPER"

	case SCISSORS:
		computerChoiceInt = SCISSORS
		computerChoice = "The computer chose SCISSORS"
	}

	messageInt := rand.Intn(3)

	var message string
	// Possibilities to win
	if playerValue == computerValue {
		roundResult = "Is a draw!!"
		message = drawMessage[messageInt]

	} else if playerValue == (computerValue+1)%3 {
		PlayerScore++
		roundResult = "Player wins!!"
		message = winMessage[messageInt]

	} else {
		ComputerScore++
		roundResult = "Comuter wins!!"
		message = loseMessage[messageInt]
	}

	return Round{
		Message:           message,
		ComputerChoice:    computerChoice,
		RoundResult:       roundResult,
		ComputerChoiceInt: computerChoiceInt,
		ComputerScore:     strconv.Itoa(ComputerScore),
		PlayerScore:       strconv.Itoa(PlayerScore),
	}
}

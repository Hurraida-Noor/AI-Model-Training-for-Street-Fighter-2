import csv
import os
from datetime import datetime
import logging

class DataCollector:
    def __init__(self):
        self.csv_file = f"p2_test_training_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.setup_csv()
        
    def setup_csv(self):
        try:
            # Create CSV file with headers
            headers = [
                'timestamp',
                # Player 1 state
                'player1_x',
                'player1_y',
                'player1_health',
                'player1_is_jumping',
                'player1_is_crouching',
                'player1_is_in_move',
                'player1_move_id',
                # Player 2 state
                'player2_x',
                'player2_y',
                'player2_health',
                'player2_is_jumping',
                'player2_is_crouching',
                'player2_is_in_move',
                'player2_move_id',
                # Game state
                'distance',
                'action_sequence',
                'action_index'
            ]
            
            with open(self.csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
        except Exception as e:
            logging.error(f"Error setting up CSV file: {str(e)}")
    
    def record_action(self, game_state, action_sequence, action_index):
        try:
            # Calculate distance between players
            distance = game_state.player2.x_coord - game_state.player1.x_coord
            
            # Record the data
            data = {
                'timestamp': datetime.now().isoformat(),
                # Player 1 state
                'player1_x': game_state.player1.x_coord,
                'player1_y': game_state.player1.y_coord,
                'player1_health': game_state.player1.health,
                'player1_is_jumping': game_state.player1.is_jumping,
                'player1_is_crouching': game_state.player1.is_crouching,
                'player1_is_in_move': game_state.player1.is_player_in_move,
                'player1_move_id': game_state.player1.move_id,
                # Player 2 state
                'player2_x': game_state.player2.x_coord,
                'player2_y': game_state.player2.y_coord,
                'player2_health': game_state.player2.health,
                'player2_is_jumping': game_state.player2.is_jumping,
                'player2_is_crouching': game_state.player2.is_crouching,
                'player2_is_in_move': game_state.player2.is_player_in_move,
                'player2_move_id': game_state.player2.move_id,
                # Game state
                'distance': distance,
                'action_sequence': ','.join(action_sequence),
                'action_index': action_index
            }
            
            with open(self.csv_file, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writerow(data)
        except Exception as e:
            # Log error but don't interrupt game flow
            logging.error(f"Error recording action: {str(e)}")
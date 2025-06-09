
# goal_aware_shift_engine.py

import logging
from utils.database import get_user_progress, shift_to_preservation

class GoalAwareShiftEngine:
    def __init__(self, user_id, goal_amount):
        self.user_id = user_id
        self.goal_amount = goal_amount

    def evaluate_and_shift(self):
        progress = get_user_progress(self.user_id)
        if progress['balance'] >= self.goal_amount * 0.95:
            shift_to_preservation(self.user_id)
            logging.info(f"[GoalAwareShift] User {self.user_id} shifted to preservation mode.")
            return True
        return False

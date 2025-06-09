
# audit_logger.py

import logging
from datetime import datetime
from utils.database import persist_audit_log

class AuditLogger:
    def __init__(self, user_id):
        self.user_id = user_id

    def log_action(self, action_type, metadata=None):
        log_entry = {
            "user_id": self.user_id,
            "action": action_type,
            "metadata": metadata or {},
            "timestamp": datetime.utcnow().isoformat()
        }
        persist_audit_log(log_entry)
        logging.info(f"[AuditLogger] Logged action: {action_type} for user {self.user_id}")
        return log_entry

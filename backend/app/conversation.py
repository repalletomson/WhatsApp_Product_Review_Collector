from typing import Dict, Optional
from .models import ConversationState

# In-memory storage for conversation states
# In production, use Redis or database
conversation_states: Dict[str, ConversationState] = {}

class ConversationManager:
    @staticmethod
    def get_state(contact_number: str) -> Optional[ConversationState]:
        return conversation_states.get(contact_number)
    
    @staticmethod
    def set_state(contact_number: str, state: ConversationState):
        conversation_states[contact_number] = state
    
    @staticmethod
    def clear_state(contact_number: str):
        if contact_number in conversation_states:
            del conversation_states[contact_number]
    
    @staticmethod
    def process_message(contact_number: str, message: str) -> str:
        state = ConversationManager.get_state(contact_number)
        
        if not state:
            # Start new conversation
            state = ConversationState(
                contact_number=contact_number,
                step="ask_product"
            )
            ConversationManager.set_state(contact_number, state)
            return "Hi! Which product is this review for?"
        
        if state.step == "ask_product":
            state.product_name = message.strip()
            state.step = "ask_name"
            ConversationManager.set_state(contact_number, state)
            return "What's your name?"
        
        elif state.step == "ask_name":
            state.user_name = message.strip()
            state.step = "ask_review"
            ConversationManager.set_state(contact_number, state)
            return f"Please send your review for {state.product_name}."
        
        elif state.step == "ask_review":
            # This is the review - we'll handle saving in the main handler
            return {
                "message": f"Thanks {state.user_name} -- your review for {state.product_name} has been recorded.",
                "review_data": {
                    "contact_number": contact_number,
                    "user_name": state.user_name,
                    "product_name": state.product_name,
                    "product_review": message.strip()
                }
            }
        
        return "I didn't understand. Please start over by sending any message."
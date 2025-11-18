import React from 'react';
import { MessageSquare } from 'lucide-react';

const EmptyState = () => {
  return (
    <div className="empty-state">
      <MessageSquare className="empty-state-icon" />
      <h3>No reviews yet</h3>
      <p>
        Reviews will appear here once users start submitting them via WhatsApp. 
        Send a message to your WhatsApp number to test the flow!
      </p>
    </div>
  );
};

export default EmptyState;
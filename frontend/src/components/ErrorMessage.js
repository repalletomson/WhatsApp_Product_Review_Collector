import React from 'react';
import { AlertCircle } from 'lucide-react';

const ErrorMessage = ({ message, onRetry }) => {
  return (
    <div className="error-container">
      <AlertCircle size={48} color="#dc2626" />
      <h3>Something went wrong</h3>
      <p className="error-message">{message}</p>
      {onRetry && (
        <button 
          onClick={onRetry}
          className="retry-button"
          style={{
            marginTop: '1rem',
            padding: '0.5rem 1rem',
            backgroundColor: 'var(--primary-600)',
            color: 'white',
            border: 'none',
            borderRadius: 'var(--radius-md)',
            cursor: 'pointer'
          }}
        >
          Try Again
        </button>
      )}
    </div>
  );
};

export default ErrorMessage;
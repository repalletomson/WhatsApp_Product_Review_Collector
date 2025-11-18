import React from 'react';
import { Package, User } from 'lucide-react';
import { format } from 'date-fns';

const ReviewCard = ({ review }) => {
  const formatDate = (dateString) => {
    try {
      return format(new Date(dateString), 'MMM dd, yyyy • h:mm a');
    } catch (error) {
      return 'Invalid date';
    }
  };

  const getInitials = (name) => {
    return name
      .split(' ')
      .map(word => word.charAt(0))
      .join('')
      .toUpperCase()
      .slice(0, 2);
  };

  const formatPhoneNumber = (phone) => {
    // Simple phone number formatting
    if (phone.startsWith('+')) {
      return phone.replace(/(\+\d{1,3})(\d{3})(\d{3})(\d{4})/, '$1 $2-$3-$4');
    }
    return phone;
  };

  return (
    <div className="review-card">
      <div className="review-header">
        <div className="review-user">
          <div className="user-avatar">
            {getInitials(review.user_name)}
          </div>
          <div className="user-info">
            <h4>{review.user_name}</h4>
            <div className="contact">{formatPhoneNumber(review.contact_number)}</div>
          </div>
        </div>
        <div className="review-date">
          {formatDate(review.created_at)}
        </div>
      </div>
      
      <div className="product-name">
        <Package className="product-icon" />
        {review.product_name}
      </div>
      
      <p className="review-text">
        "{review.product_review}"
      </p>
    </div>
  );
};

export default ReviewCard;
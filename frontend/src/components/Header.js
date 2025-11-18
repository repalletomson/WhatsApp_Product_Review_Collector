import React from 'react';
import { MessageCircle } from 'lucide-react';

const Header = ({ stats }) => {
  return (
    <header className="header">
      <div className="header-content">
        <div className="header-title">
          <MessageCircle className="header-icon" />
          <h1>Review Dashboard</h1>
        </div>
        
        {stats && (
          <div className="stats-container">
            <div className="stat-item">
              <span className="stat-number">{stats.total_reviews}</span>
              <span className="stat-label">Total Reviews</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">{stats.unique_products}</span>
              <span className="stat-label">Products</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">{stats.unique_users}</span>
              <span className="stat-label">Users</span>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
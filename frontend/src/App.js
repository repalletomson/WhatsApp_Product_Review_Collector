import React, { useState, useEffect, useCallback } from 'react';
import { RefreshCw } from 'lucide-react';

import Header from './components/Header';
import ReviewCard from './components/ReviewCard';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import EmptyState from './components/EmptyState';
import { reviewsAPI } from './services/api';

function App() {
  const [reviews, setReviews] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [refreshing, setRefreshing] = useState(false);

  const fetchData = useCallback(async (isRefresh = false) => {
    try {
      if (isRefresh) {
        setRefreshing(true);
      } else {
        setLoading(true);
      }
      setError(null);

      const [reviewsData, statsData] = await Promise.all([
        reviewsAPI.getReviews(),
        reviewsAPI.getStats()
      ]);

      setReviews(reviewsData);
      setStats(statsData);
    } catch (err) {
      console.error('Error fetching data:', err);
      setError(err.message || 'Failed to load data');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleRefresh = () => {
    fetchData(true);
  };

  const handleRetry = () => {
    fetchData();
  };

  if (loading) {
    return (
      <div className="app">
        <Header />
        <main className="main-content">
          <LoadingSpinner />
        </main>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <Header />
        <main className="main-content">
          <ErrorMessage message={error} onRetry={handleRetry} />
        </main>
      </div>
    );
  }

  return (
    <div className="app">
      <Header stats={stats} />
      
      <main className="main-content">
        {reviews.length === 0 ? (
          <EmptyState />
        ) : (
          <div className="reviews-grid">
            {reviews.map((review) => (
              <ReviewCard key={review.id} review={review} />
            ))}
          </div>
        )}
      </main>

      <button
        className={`refresh-button ${refreshing ? 'spinning' : ''}`}
        onClick={handleRefresh}
        disabled={refreshing}
        title="Refresh reviews"
      >
        <RefreshCw className="refresh-icon" />
      </button>
    </div>
  );
}

export default App;